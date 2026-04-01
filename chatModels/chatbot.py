from dotenv import load_dotenv
import os
load_dotenv()


from langchain_mistralai import ChatMistralAI
from langchain_core.messages import HumanMessage , AIMessage , SystemMessage
model = ChatMistralAI(model="mistral-small-2603", temperature=0.9, max_tokens=100)
print("Choose Your Model Behavior : \n 1. Helpful and Funny Assistant \n 2. Professional and Concise Assistant \n 3. Creative and Imaginative Assistant")

choice = input("Enter your choice (1, 2, or 3): ")
if choice == "1":
    mode = "You are a helpful and funny assistant."
elif choice == "2":
    mode = "You are a professional and concise assistant."
elif choice == "3":
    mode = "You are a creative and imaginative assistant."
message = [
    SystemMessage(content=mode),
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