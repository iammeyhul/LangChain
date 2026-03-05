import os
import google.generativeai as genai
from dotenv import load_dotenv
load_dotenv()

# Configure the API key
api_key = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=api_key)

result = genai.embed_content(
    model="models/embedding-001",  # Use the correct model name for Gemini embeddings
    content="What is the meaning of life?"
)

print(result['embedding'])