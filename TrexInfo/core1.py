from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate 
from pydantic import BaseModel
from typing import List , Optional
from langchain_core.output_parsers import PydanticOutputParser

import os 
load_dotenv()

from langchain_mistralai import ChatMistralAI

model = ChatMistralAI(model="mistral-small-2603")

# Schema for the extracted information
class Movie(BaseModel):
    title : str
    genre : str
    director : str
    cast : List[str]
    release_date : str
    language : str
    country : str
    duration : str
    rating : Optional[float]
    themes : List[str]
    key_highlights : List[str]
    summary : str


parser = PydanticOutputParser(pydantic_object=Movie)

prompt = ChatPromptTemplate.from_messages([
    ("system", """
Extract Movie Infromation From The Paragraph
     {format_instructions}

"""),
(
    "human",
    "{paragraph}"
)]
)

para = input("Enter the paragraph to extract information from : ")
final_Prompt = prompt.invoke(
    {
        "paragraph" : para ,
        'format_instructions' : parser.get_format_instructions() 
    }
)

res = model.invoke(final_Prompt)
# movie_data = parser.parse(res.content)
print(res.content)