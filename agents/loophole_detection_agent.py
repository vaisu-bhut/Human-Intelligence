import google.generativeai as genai
import os

def detect_issues(analysis: str, email_content: dict) -> dict:
    """Detect hidden clauses and loopholes using Gemini API"""
    genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
    model = genai.GenerativeModel('gemini-1.5-flash')
    
    response = model.generate_content(
        f"""Based on this analysis:
        {analysis}
        
        Identify potential issues:
        1. Hidden clauses or obligations
        2. Ambiguous language
        3. Unfavorable terms
        4. Auto-renewal clauses
        5. Termination penalties
        6. Unilateral rights
        7. Data usage rights
        
        For each issue found:
        - Categorize the issue type
        - Quote the relevant text
        - Explain why it might be problematic
        - Suggest questions to ask
        
        Format as JSON-ready output."""
    )
    
    return response.text