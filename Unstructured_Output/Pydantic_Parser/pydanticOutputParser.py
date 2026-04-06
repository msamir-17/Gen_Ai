from dotenv import load_dotenv
import os
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser 
from pydantic import BaseModel , Field , Optional , Literal
load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="deepseek-ai/DeepSeek-R1"
)

model = ChatHuggingFace(llm=llm)

class Person(BaseModel):
    name: Optional[str] = Field(None, description="The name of the person")
    age:  Optional[int] = Field(None, gt=18,description="The age of the person" ,lt=99)
    city: Optional[str] = Field(None, description="The city where the person lives")

parser = PydanticOutputParser()

template = PromptTemplate(
    template= " Generate the  name , age and city of a fictional person  \n {person} ",
    input_variables=['place'],
    partial_variables={"format_instruction": parser.get_format_instructions() }
)

# prompt = template.invoke({'place': "New York"})
# print(prompt)
# res = model.invoke(prompt)

# fres = parser.parse(res)
chain = template | model | parser

fres = chain.invoke({'place': "New York"})  
print(fres)