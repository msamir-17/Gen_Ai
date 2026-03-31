from dotenv import load_dotenv
import os


load_dotenv()

from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint

llm = HuggingFaceEndpoint(
    repo_id="deepseek-ai/DeepSeek-R1"
)
model = ChatHuggingFace(llm=llm)


res = model.invoke("What is the capital of France?")
print(res.content)