# from typing import TypedDict
# from dotenv import load_dotenv
# from langchain_google_genai import ChatGoogleGenerativeAI

# load_dotenv()

# model = ChatGoogleGenerativeAI(model="gemini-2.5-flash-lite")

# class Review(TypedDict):
#     Summery:str
#     sentinment:str

# review_model = model.with_structured_output(Review)

# res = review_model.invoke("I recently bought a new smartphone and overall I am very happy with its performance. The battery life is excellent and it lasts all day without charging. The camera quality is also very good, especially in daylight. However, the phone heats up a bit during gaming, which is slightly disappointing. Still, considering the price, it is a great value for money.")

# print(res['Summery'])
# print(res['sentinment'])


from typing import TypedDict , Annotated , Optional , Literal
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from pydantic import BaseModel , Field , Optional
load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-2.5-flash-lite")

class Review(BaseModel):
    Summery: Optional[str] = Field(None, description="A brief summary of the review")
    key_themes: Optional[str] = Field(None, description="The key themes or aspects mentioned in the review, such as performance, battery life, camera quality, etc.")
    sentinment: Optional[Literal['pos','neg']] = Field(None, description="The overall sentiment of the review, either positive, negative, or neutral")
    pros: Optional[list[str] ]= Field(None, description="The positive aspects of the product mentioned in the review")
    cons: Optional[list[str]] = Field(None, description="The negative aspects of the product mentioned in the review")

    

review_model = model.with_structured_output(Review)

res = review_model.invoke("I recently bought a new smartphone and overall I am very happy with its performance. The battery life is excellent and it lasts all day without charging. The camera quality is also very good, especially in daylight. However, the phone heats up a bit during gaming, which is slightly disappointing. Still, considering the price, it is a great value for money.")

print(res)