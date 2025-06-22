OUTPUT_SCHEMA = {
    "type": "object",
    "properties": {
        "metadata": {
            "type": "object",
            "properties": {
                "subject": {"type": "string"},
                "from": {"type": "string"},
                "to": {"type": "string"},
                "date": {"type": "string"},
                "attachments": {
                    "type": "array",
                    "items": {"type": "string"}
                }
            },
            "required": ["subject", "from", "date"]
        },
        "summary": {"type": "string"},
        "key_points": {
            "type": "object",
            "properties": {
                "parties": {
                    "type": "array",
                    "items": {"type": "string"}
                },
                "dates": {
                    "type": "array",
                    "items": {"type": "string"}
                },
                "obligations": {
                    "type": "array",
                    "items": {"type": "string"}
                },
                "financial_terms": {
                    "type": "array",
                    "items": {"type": "string"}
                }
            }
        },
        "potential_issues": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "type": {"type": "string"},
                    "quote": {"type": "string"},
                    "explanation": {"type": "string"},
                    "suggested_actions": {"type": "string"}
                },
                "required": ["type", "explanation"]
            }
        }
    },
    "required": ["metadata", "summary", "key_points", "potential_issues"]
}