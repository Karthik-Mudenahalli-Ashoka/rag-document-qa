from dotenv import load_dotenv
import os
from langchain_google_genai import GoogleGenerativeAIEmbeddings

load_dotenv()

embeddings = GoogleGenerativeAIEmbeddings(model="models/gemini-embedding-001")
result = embeddings.embed_query("What is machine learning?")
print(f"✅ Setup working! Embedding size: {len(result)}")