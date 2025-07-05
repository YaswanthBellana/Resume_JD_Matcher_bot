import os
import google.generativeai as genai

# Optional: Load from .env if using python-dotenv
try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass

# Configure Gemini with API key
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

def evaluate_with_gemini(prompt):
    try:
        model = genai.GenerativeModel("gemini-pro")
        response = model.generate_content(prompt)
        if response.prompt_feedback and response.prompt_feedback.block_reason:
            return f"Blocked: {response.prompt_feedback.block_reason}"
        return response.text.strip()
    except Exception as e:
        return f"Error: {str(e)}"