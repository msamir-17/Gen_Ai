from dotenv import load_dotenv
import os
load_dotenv()

from langchain_huggingface import HuggingFaceEmbeddings

embeddings = HuggingFaceEmbeddings(
    model_name = "sentence-transformers/all-MiniLM-L6-v2"

)
texts = ["i am new", "i am sam"]
vector = embeddings.embed_documents(texts)
print(vector)