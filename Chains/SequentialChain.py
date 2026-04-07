from langchain_mistralai import ChatMistralAI
from dotenv import load_dotenv
import os
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

prompt = PromptTemplate(
    template="Generate a joke on given topic {topic} ",
    input_variables=["topic"]
)

prompt1 = PromptTemplate(
    template="Generate a motivational quote on given topic {text} ",
    input_variables=["text"]
)


model = ChatMistralAI(model="mistral-small-2603", temperature=0.9, max_tokens=100)

parser = StrOutputParser()

chain = prompt | model | parser | prompt1 | model | parser

chain.invoke({"topic": "India"})