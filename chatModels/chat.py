from dotenv import load_dotenv
import os


load_dotenv()

# gemine model
from langchain_google_genai import ChatGoogleGenerativeAI
model = ChatGoogleGenerativeAI(model="gemini-2.5-flash-lite")
# from langchain.chat_models import init_chat_model

# model = init_chat_model("google_genai:gemini-2.5-flash-lite")

# # print(model)

res = model.invoke("What is the capital of France?")
print(res.response_metadata)



# groq model
# from langchain.chat_models import init_chat_model
# model = init_chat_model("meta-llama/llama-4-scout-17b-16e-instruct", model_provider="groq")

# res = model.invoke("What is the capital of austrial? and speciallity hinglish ")
# print(res.content)

# 2nd method
# from langchain_groq import ChatGroq                                                    
# model = ChatGroq(model="meta-llama/llama-4-scout-17b-16e-instruct")

# res = model.invoke("write a short para on the capital of India? in hinglish")
# print(res.content)


# Mistral model
# from langchain.chat_models import init_chat_model
# model = init_chat_model(model = "mistral-small-2603")

# res = model.invoke("i am from japan and i want to know about cricket in india? write in hinglish")
# print(res.content)

# method 2nd for mistral
from langchain_mistralai import ChatMistralAI
model = ChatMistralAI(model="mistral-small-2603", temperature=0.9, max_tokens=100)

res = model.invoke("write a sayri on AI in hinglish")
print(res.content)