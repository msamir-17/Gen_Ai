from dotenv import load_dotenv
import os
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="deepseek-ai/DeepSeek-R1"
)

model = ChatHuggingFace(llm=llm)

parser = JsonOutputParser()

template = PromptTemplate(
    template= " Give me  the  name , age and city of a fictional person  \n {format_instruction} ",
    input_variables=[],
    partial_variables={"format_instruction": parser.get_format_instructions() }
)

# prompt = template.format()

# res = model.invoke(prompt)

# fres = parser.parse(res)

# print(fres)

# chain 

# Chain: Prompt → Model → Parser
chain = template | model | parser 

res = chain.invoke({ })
# Empty {} because no input variables

print(res)


# in json we can not take output in the from of a dictionary 