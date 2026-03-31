from dotenv import load_dotenv
import os
load_dotenv()


from langchain_mistralai import ChatMistralAI
from langchain_core.messages import HumanMessage , AIMessage , SystemMessage
model = ChatMistralAI(model="mistral-small-2603", temperature=0.9, max_tokens=100)

message = [
    SystemMessage(content="You are a helpful and funny assistant."),
]

print("__________________________Welcome to the Chatbot! Type 0 To Exit___________________________")
while True:
    user = input("You : ")
    message.append(HumanMessage(content=user))
    if user == "0":
        break
    res = model.invoke(message)
    message.append(AIMessage(content=res.content))
    print("Bot : ",res.content)

print(message)