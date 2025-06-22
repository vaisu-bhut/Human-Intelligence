import json
import re
from schemas.output_schema import OUTPUT_SCHEMA

def format_to_json(raw_analysis: str, raw_issues: str, email_data: dict) -> dict:
    """Format Gemini responses into structured JSON"""
    # Extract JSON-like content
    def extract_json(text):
        match = re.search(r'\{.*\}', text, re.DOTALL)
        return json.loads(match.group(0)) if match else {}
    
    analysis = extract_json(raw_analysis)
    issues = extract_json(raw_issues)
    
    # Build final output
    output = {
        "metadata": {
            "subject": email_data["subject"],
            "from": email_data["from"],
            "to": email_data["to"],
            "date": email_data["date"],
            "attachments": [a["filename"] for a in email_data["attachments"]]
        },
        "summary": analysis.get("summary", ""),
        "key_points": {
            "parties": analysis.get("parties", []),
            "dates": analysis.get("important_dates", []),
            "obligations": analysis.get("obligations", []),
            "financial_terms": analysis.get("financial_terms", [])
        },
        "potential_issues": issues.get("issues", [])
    }
    
    # Validate against schema
    return validate_against_schema(output)

def validate_against_schema(data: dict) -> dict:
    """Simple schema validation (in production, use a validation library)"""
    for key in OUTPUT_SCHEMA["required"]:
        if key not in data:
            raise ValueError(f"Missing required field: {key}")
    return data