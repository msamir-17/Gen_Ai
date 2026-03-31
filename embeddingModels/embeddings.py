from dotenv import load_dotenv
import os 
load_dotenv()

from langchain_google_genai import GoogleGenerativeAIEmbeddings

embeddings = GoogleGenerativeAIEmbeddings(
    model="gemini-embedding-001",
    dimensions=20
)
texts = ["What is the capital of France?", "What is the capital of Germany?"]
vector = embeddings.embed_documents(texts)
print(vector)