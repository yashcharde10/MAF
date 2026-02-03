from agent_framework.openai import OpenAIChatClient
import os 
from dotenv import load_dotenv

# load .env file 
load_dotenv()

def groq_ai_client(model_id = "llama-3.3-70b-versatile"):
    api_key = os.getenv("GROQ_API_KEY")
    if not api_key:
        print("Error: GROQ_API_KEY not found in environment!")
    return OpenAIChatClient(
        model_id=model_id,
        base_url="https://api.groq.com/openai/v1", 
        api_key=api_key
    )