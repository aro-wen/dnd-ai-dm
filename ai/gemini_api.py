# ai/gemini_api.py

import os
import google.generativeai as genai
from dotenv import load_dotenv

# Load API config from .env
load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
GEMINI_MODEL = os.getenv("MODEL_NAME", "models/gemini-pro")

if not GEMINI_API_KEY:
    raise ValueError("❌ GEMINI_API_KEY not found in environment variables.")

# Configure the Gemini client
genai.configure(api_key=GEMINI_API_KEY)

# Model instantiation
try:
    model = genai.GenerativeModel(model_name=GEMINI_MODEL)
except Exception as e:
    raise RuntimeError(f"❌ Failed to load Gemini model '{GEMINI_MODEL}': {str(e)}")

# Chat sessions for memory
chat_sessions = {}

# Generate response from Gemini using custom prompt
def generate_response(prompt: str, session_id: str = "default") -> str:
    if session_id not in chat_sessions:
        chat_sessions[session_id] = model.start_chat(history=[])
    try:
        response = chat_sessions[session_id].send_message(prompt)
        return response.text
    except Exception as e:
        return f"❌ Gemini API Error: {str(e)}"

# Needed for app.py
def init_gemini_model():
    return model
