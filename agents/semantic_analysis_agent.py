import google.generativeai as genai
import os

def analyze_content(email_content: dict) -> dict:
    """Analyze email content using Gemini API"""
    genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
    model = genai.GenerativeModel('gemini-1.5-flash')
    
    # Prepare content for analysis
    content = f"""
    EMAIL SUBJECT: {email_content['subject']}
    FROM: {email_content['from']}
    TO: {email_content['to']}
    DATE: {email_content['date']}
    BODY: {email_content['body']}
    
    ATTACHMENTS:
    """
    
    for idx, attachment in enumerate(email_content['attachments']):
        content += f"\nATTACHMENT {idx+1} ({attachment['filename']}):\n{attachment['text']}\n"
    
    # Generate analysis
    response = model.generate_content(
        f"""Analyze this email and its attachments. Identify:
        1. Main purpose of the communication
        2. Key parties involved
        3. Important dates/deadlines
        4. Financial commitments
        5. Legal obligations
        6. Termination clauses
        
        Provide your analysis in JSON-ready format without markdown."""
        + content
    )
    
    return response.text