from google.cloud import storage
import json
import os

def save_to_gcs(data: dict, filename: str) -> str:
    """Save JSON output to Google Cloud Storage"""
    bucket_name = os.getenv("GCS_BUCKET_NAME")
    
    if not bucket_name:
        raise ValueError("GCS_BUCKET_NAME environment variable is not set")
    
    try:
        client = storage.Client()
        bucket = client.bucket(bucket_name)
        blob = bucket.blob(filename)
        
        blob.upload_from_string(
            data=json.dumps(data, indent=2),
            content_type="application/json"
        )
        
        return f"gs://{bucket_name}/{filename}"
    except Exception as e:
        raise Exception(f"Failed to save to GCS: {e}. Please check your GCS credentials and bucket configuration.")