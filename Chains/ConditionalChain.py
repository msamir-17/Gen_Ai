from langchain_mistralai import ChatMistralAI
from dotenv import load_dotenv
import os
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_groq import ChatGroq  
from langchain_core.runnables  import RunnableParallel , RunnableBranch , RunnableLambda                                          
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel ,   Field
from typing import Literal

load_dotenv()


model = ChatMistralAI(model="mistral-small-2603", temperature=0.9, max_tokens=100)

parser = StrOutputParser()

class Feedback(BaseModel):
    sentiment:Literal['Positive', 'Negative'] = Field(description="Give the sentiment of the feedback")

parser1 = PydanticOutputParser(pydantic_object=Feedback)


prompt = PromptTemplate(
    template="Classify the Sentiment of the following Feedback as Positive, Negative or Neutral \n {feedback} \n {format_instruction}.",

    input_variables=["feedback"],

    partial_variables={"format_instruction": parser1.get_format_instructions()}
)

chain_classifeid = prompt | model | parser1  

# res =chain_classifeid.invoke({"feedback": "The product is really good and I am satisfied with the quality."})

# print(res)


# now we are going to create branch of chains 

prompt1 = PromptTemplate(
    template = 'Write a appropriate response to the following Positive feedback \n {feedback} ',
    input_variables=['feedback']
)

prompt2 = PromptTemplate(
    template = 'Write a appropriate response to the following Negative feedback \n {feedback} ',
    input_variables=['feedback']
)

branch_chain = RunnableBranch(
    (lambda x:x.sentiment == 'Positive' ,  prompt1 | model | parser),
    (lambda x:x.sentiment == 'Negative' , prompt2 | model | parser),
    RunnableLambda(lambda x: "Neutral feedback received, no response needed.")
)

chain = chain_classifeid | branch_chain

res = chain.invoke({"feedback": "The product is really not good and I am not  satisfied with the quality."})