from dotenv import load_dotenv
import google.generativeai as genai
import os

load_dotenv()

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# List all models that support generateContent
for model in genai.list_models():
    if "generateContent" in model.supported_generation_methods:
        print(model.name)