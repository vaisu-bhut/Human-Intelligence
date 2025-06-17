import json
from datetime import datetime
from typing import Any, Dict

def timestamp() -> str:
    return datetime.now().isoformat(sep=" ", timespec="seconds")

def save_session_to_disk(session_data: Dict[str, Any], path: str = "sessions"):
    """Persist session data for later analysis"""
    os.makedirs(path, exist_ok=True)
    filename = f"{path}/session_{session_data['session_id']}.json"
    
    with open(filename, 'w') as f:
        json.dump(session_data, f, indent=2)

def load_prompt_templates() -> Dict[str, str]:
    """Load creative prompt templates (extend for production)"""
    return {
        "genre_blend": "Combine {input} with {genre} elements",
        "what_if": "What if {input} happened in {condition}?",
        "character_focus": "Tell the story from the perspective of {character}"
    }