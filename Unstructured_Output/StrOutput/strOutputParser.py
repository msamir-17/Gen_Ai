from dotenv import load_dotenv
import os
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_core.prompts import PromptTemplate
load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="deepseek-ai/DeepSeek-R1"
)
model = ChatHuggingFace(llm=llm)

template1 = PromptTemplate(
    template="What is the capital of {topic}?",
    input_variables=["topic"]
)

template2 = PromptTemplate(
    template="Write a 5 line summary of {text}?",
    input_variables=["text"]
)

prompt1 = template1.invoke({"topic":"France"})
res1 = model.invoke(prompt1)
print(res1.content)

prompt2 = template2.invoke({"text":res1.content})
res2 = model.invoke(prompt2)
print(res2.content)

# res = model.invoke("What is the capital of France?")
# print(res.content)