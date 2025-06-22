import os
import argparse
from dotenv import load_dotenv
from agents.email_ingestion_agent import parse_email
from agents.text_extraction_agent import extract_text
# from agents.semantic_analysis_agent import analyze_content
# from agents.loophole_detection_agent import detect_issues
# from agents.json_formatter_agent import format_to_json
# from agents.storage_agent import save_to_gcs

load_dotenv()  # Load environment variables

def process_email(email_path: str, output_name: str):
    # Step 1: Parse email
    email_data = parse_email(email_path)
    print(email_data)
    
    # Step 2: Extract text from attachments
    for attachment in email_data["attachments"]:
        attachment["text"] = extract_text(
            attachment["payload"],
            attachment["content_type"],
            attachment["filename"]
        )

    print(email_data["attachments"][0]["text"])
    
    # # Step 3: Analyze content
    # analysis = analyze_content(email_data)
    
    # # Step 4: Detect issues
    # issues = detect_issues(analysis, email_data)
    
    # # Step 5: Format to JSON
    # json_output = format_to_json(analysis, issues, email_data)
    
    # # Step 6: Save to GCS
    # gcs_uri = save_to_gcs(json_output, f"{output_name}.json")
    
    # print(f"Processing complete. Results saved to: {gcs_uri}")
    # print(f"Summary: {json_output['summary'][:200]}...")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Process email for critical insights")
    parser.add_argument("email_path", help="Path to email file (.eml)")
    parser.add_argument("--output", default="analysis_result", help="Output filename prefix")
    args = parser.parse_args()
    
    process_email(args.email_path, args.output)