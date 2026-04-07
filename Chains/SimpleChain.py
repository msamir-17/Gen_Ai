from langchain_mistralai import ChatMistralAI
from dotenv import load_dotenv
import os
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

prompt = PromptTemplate(
    template='Generate 5 interesting fact about {topic} in hinglish',
    input_variables=['topic']
)

model = ChatMistralAI(model="mistral-small-2603", temperature=0.9, max_tokens=100)

parser = StrOutputParser()

chain = prompt | model | parser 

res = chain.invoke({'topic':'Ai'})

print(res)

# to visualize the chain we can use the following code

chain.get_graph().print_ascii()

# res = model.invoke("write a sayri on AI in hinglish")
# print(res.content)