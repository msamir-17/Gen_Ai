from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate 
import os 
load_dotenv()

from langchain_mistralai import ChatMistralAI

model = ChatMistralAI(model="mistral-small-2603", max_tokens=100)

prompt = ChatPromptTemplate.from_messages([ ("system", """
You are an intelligent information extraction assistant.

Your task is to read the given paragraph and extract all important information in a clean, well-structured format, along with a short summary.

---------------------
INPUT PARAGRAPH:
{paragraph}
---------------------

INSTRUCTIONS:

1. Extract key information:
   - Title
   - Genre
   - Director
   - Cast
   - Release Date
   - Language
   - Country
   - Duration
   - Themes
   - Key Highlights

2. If any information is missing, write: Not Mentioned

3. Keep output clean using bullet points

4. Also generate a 2–4 line summary

5. Do NOT add anything outside the format

---------------------

OUTPUT FORMAT:

📌 Extracted Information:

- Title:
- Genre:
- Director:
- Cast:
- Release Date:
- Language:
- Country:
- Duration:
- Themes:
- Key Highlights:

📌 Summary:
"""),

(
    "human",
    """ 
Extract information and summarize from the paragraph:

{paragraph}
 """
)]
)

para = input("Enter the paragraph to extract information from : ")
final_Prompt = prompt.invoke(
    {
        "paragraph" : para  
    }
)

res = model.invoke(final_Prompt)

print(res.content)