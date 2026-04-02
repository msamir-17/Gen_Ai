import streamlit as st
from dotenv import load_dotenv
import os

from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from langchain_mistralai import ChatMistralAI

from pydantic import BaseModel
from typing import List, Optional

# Load env
load_dotenv()
def show():
    st.markdown('<div class="title">🎬 Movie Info Extractor</div>', unsafe_allow_html=True)
    # ---------------- UI CONFIG ----------------
    st.set_page_config(
        page_title="🎬 Movie Info Extractor",
        page_icon="🎥",
        layout="centered"
    )

    # Custom CSS for better UI
    st.markdown("""
        <style>
        .main {
            background-color: #0f172a;
        }
        .title {
            color: #38bdf8;
            text-align: center;
            font-size: 40px;
            font-weight: bold;
        }
        .sub {
            text-align: center;
            color: #94a3b8;
            margin-bottom: 20px;
        }
        .stButton>button {
            background-color: #38bdf8;
            color: black;
            font-weight: bold;
            border-radius: 10px;
        }
        </style>
    """, unsafe_allow_html=True)

    st.markdown('<div class="title">🎬 Movie Info Extractor</div>', unsafe_allow_html=True)
    st.markdown('<div class="sub">Extract structured movie data from any paragraph</div>', unsafe_allow_html=True)

    # ---------------- MODEL ----------------
    model = ChatMistralAI(model="mistral-small-2603")

    # ---------------- SCHEMA ----------------
    class Movie(BaseModel):
        title: str
        genre: str
        director: str
        cast: List[str]
        release_date: str
        language: str
        country: str
        duration: str
        rating: Optional[float]
        themes: List[str]
        key_highlights: List[str]
        summary: str

    parser = PydanticOutputParser(pydantic_object=Movie)

    # ---------------- PROMPT ----------------
    prompt = ChatPromptTemplate.from_messages([
        ("system", """
    Extract Movie Information from the paragraph.

    Return ONLY valid JSON.

    {format_instructions}
    """),
        ("human", "{paragraph}")
    ])

    # ---------------- INPUT ----------------
    paragraph = st.text_area(
        "📄 Enter Movie Paragraph:",
        height=200,
        placeholder="Example: Avengers is a superhero film directed by Joss Whedon..."
    )

    # ---------------- BUTTON ----------------
    if st.button("✨ Extract Information"):
        if paragraph.strip() == "":
            st.warning("⚠️ Please enter some text")
        else:
            with st.spinner("Processing... 🚀"):
                try:
                    final_prompt = prompt.invoke({
                        "paragraph": paragraph,
                        "format_instructions": parser.get_format_instructions()
                    })

                    res = model.invoke(final_prompt)

                    # Parse to structured JSON
                    movie_data = parser.parse(res.content)

                    # ---------------- OUTPUT ----------------
                    st.success("✅ Extraction Successful!")

                    st.subheader("📊 Structured Output (JSON)")
                    st.json(movie_data.dict())

                except Exception as e:
                    st.error("❌ Error occurred")
                    st.code(str(e))