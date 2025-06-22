import email
from email import policy
import os

def parse_email(email_file_path: str):
    """Parse email file and extract content with attachments"""
    with open(email_file_path, 'rb') as f:
        msg = email.message_from_binary_file(f, policy=policy.default)
    
    email_data = {
        "subject": msg['subject'],
        "from": msg['from'],
        "to": msg['to'],
        "date": msg['date'],
        "body": "",
        "attachments": []
    }
    
    # Extract body and attachments
    for part in msg.walk():
        content_type = part.get_content_type()
        content_disposition = str(part.get("Content-Disposition"))
        
        if "attachment" in content_disposition:
            filename = part.get_filename()
            if filename:
                payload = part.get_payload(decode=True)
                email_data["attachments"].append({
                    "filename": filename,
                    "content_type": content_type,
                    "payload": payload
                })
        
        elif content_type == "text/plain":
            charset = part.get_content_charset() or 'utf-8'
            email_data["body"] += part.get_payload(decode=True).decode(charset, errors="ignore")
    
    return email_data