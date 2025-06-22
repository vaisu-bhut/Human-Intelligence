import PyPDF2
import docx
import io
import os
from google.cloud import documentai_v1 as documentai

def extract_text(file_bytes: bytes, content_type: str, filename: str) -> str:
    """Extract text from different file types"""
    # PDF files
    if content_type == "application/pdf" or filename.lower().endswith(".pdf"):
        reader = PyPDF2.PdfReader(io.BytesIO(file_bytes))
        return "\n".join([page.extract_text() for page in reader.pages])
    
    # Word documents
    elif (content_type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document" or 
          filename.lower().endswith(".docx")):
        doc = docx.Document(io.BytesIO(file_bytes))
        return "\n".join([para.text for para in doc.paragraphs])
    
    # Text files
    elif content_type == "text/plain" or filename.lower().endswith(".txt"):
        return file_bytes.decode('utf-8', errors='ignore')
    
    # Use Document AI for complex documents
    else:
        return extract_with_documentai(file_bytes, content_type)

def extract_with_documentai(file_bytes: bytes, mime_type: str) -> str:
    """Process document using GCP Document AI"""
    client = documentai.DocumentProcessorServiceClient()
    project_id = os.getenv("GCP_PROJECT_ID")
    location = os.getenv("DOCAI_LOCATION", "us")
    processor_id = os.getenv("DOCAI_PROCESSOR_ID")
    
    name = f"projects/{project_id}/locations/{location}/processors/{processor_id}"
    document = {"content": file_bytes, "mime_type": mime_type}
    
    request = {"name": name, "raw_document": document}
    result = client.process_document(request=request)
    return result.document.text