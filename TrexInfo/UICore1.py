# import streamlit as st
# from dotenv import load_dotenv
# import os

# from langchain_core.prompts import ChatPromptTemplate
# from langchain_core.output_parsers import PydanticOutputParser
# from langchain_mistralai import ChatMistralAI

# from pydantic import BaseModel
# from typing import List, Optional

# # Load env
# load_dotenv()
# def show():
#     st.markdown('<div class="title">🎬 Movie Info Extractor</div>', unsafe_allow_html=True)
#     # ---------------- UI CONFIG ----------------
#     # st.set_page_config(
#     #     page_title="🎬 Movie Info Extractor",
#     #     page_icon="🎥",
#     #     layout="centered"
#     # )

#     # Custom CSS for better UI
#     st.markdown("""
#         <style>
#         .main {
#             background-color: #0f172a;
#         }
#         .title {
#             color: #38bdf8;
#             text-align: center;
#             font-size: 40px;
#             font-weight: bold;
#         }
#         .sub {
#             text-align: center;
#             color: #94a3b8;
#             margin-bottom: 20px;
#         }
#         .stButton>button {
#             background-color: #38bdf8;
#             color: black;
#             font-weight: bold;
#             border-radius: 10px;
#         }
#         </style>
#     """, unsafe_allow_html=True)

#     st.markdown('<div class="sub">Extract structured movie data from any paragraph</div>', unsafe_allow_html=True)

#     # ---------------- MODEL ----------------
#     model = ChatMistralAI(model="mistral-small-2603")

#     # ---------------- SCHEMA ----------------
#     class Movie(BaseModel):
#         title: str
#         genre: str
#         director: str
#         cast: List[str]
#         release_date: str
#         language: str
#         country: str
#         duration: str
#         rating: Optional[float]
#         themes: List[str]
#         key_highlights: List[str]
#         summary: str

#     parser = PydanticOutputParser(pydantic_object=Movie)

#     # ---------------- PROMPT ----------------
#     prompt = ChatPromptTemplate.from_messages([
#         ("system", """
#     Extract Movie Information from the paragraph.

#     Return ONLY valid JSON.

#     {format_instructions}
#     """),
#         ("human", "{paragraph}")
#     ])

#     # ---------------- INPUT ----------------
#     paragraph = st.text_area(
#         "📄 Enter Movie Paragraph:",
#         height=200,
#         placeholder="Example: Avengers is a superhero film directed by Joss Whedon..."
#     )

#     # ---------------- BUTTON ----------------
#     if st.button("✨ Extract Information"):
#         if paragraph.strip() == "":
#             st.warning("⚠️ Please enter some text")
#         else:
#             with st.spinner("Processing... 🚀"):
#                 try:
#                     final_prompt = prompt.invoke({
#                         "paragraph": paragraph,
#                         "format_instructions": parser.get_format_instructions()
#                     })

#                     res = model.invoke(final_prompt)

#                     # Parse to structured JSON
#                     movie_data = parser.parse(res.content)

#                     # ---------------- OUTPUT ----------------
#                     st.success("✅ Extraction Successful!")

#                     st.subheader("📊 Structured Output (JSON)")
#                     st.json(movie_data.dict())

#                 except Exception as e:
#                     st.error("❌ Error occurred")
#                     st.code(str(e))


import streamlit as st
from dotenv import load_dotenv
load_dotenv()

from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from langchain_mistralai import ChatMistralAI
from pydantic import BaseModel
from typing import List, Optional


def show():
    st.markdown("""
    <style>
    /* Text area */
    .stTextArea textarea {
        background: #ffffff !important;
        border: 1.5px solid #e4e4f0 !important;
        border-radius: 12px !important;
        color: #1a1a2e !important;
        font-family: 'Inter', sans-serif !important;
        font-size: 0.88rem !important;
        line-height: 1.7 !important;
        box-shadow: 0 1px 4px rgba(0,0,0,0.05) !important;
        padding: 0.9rem 1rem !important;
    }
    .stTextArea textarea:focus {
        border-color: #6366f1 !important;
        box-shadow: 0 0 0 3px rgba(99,102,241,0.1) !important;
    }
    .stTextArea textarea::placeholder { color: #c8c8e0 !important; }
    .stTextArea label { display: none !important; }

    /* Extract button */
    .main .stButton > button {
        background: #6366f1 !important;
        border: none !important;
        border-radius: 10px !important;
        color: #ffffff !important;
        font-family: 'Inter', sans-serif !important;
        font-size: 0.82rem !important;
        font-weight: 600 !important;
        padding: 0.65rem 2rem !important;
        box-shadow: 0 4px 14px rgba(99,102,241,0.35) !important;
        transition: all 0.18s ease !important;
        letter-spacing: 0.02em !important;
    }
    .main .stButton > button:hover {
        background: #4f46e5 !important;
        box-shadow: 0 6px 20px rgba(99,102,241,0.45) !important;
        transform: translateY(-1px) !important;
    }

    /* Result card */
    .result-card {
        background: #ffffff;
        border: 1.5px solid #e4e4f0;
        border-radius: 16px;
        padding: 1.6rem;
        box-shadow: 0 2px 12px rgba(0,0,0,0.06);
        margin-top: 1.5rem;
    }
    .result-top {
        display: flex; align-items: center; gap: 0.5rem;
        padding-bottom: 1rem; margin-bottom: 1.2rem;
        border-bottom: 1px solid #f0f0f8;
    }
    .green-dot {
        width: 8px; height: 8px; border-radius: 50%;
        background: #22c55e;
    }
    .result-ok {
        font-size: 0.62rem; color: #16a34a;
        letter-spacing: 0.14em; text-transform: uppercase; font-weight: 600;
    }

    /* Fields grid */
    .fgrid {
        display: grid;
        grid-template-columns: repeat(auto-fill, minmax(170px, 1fr));
        gap: 0.65rem; margin-bottom: 1.2rem;
    }
    .fcard {
        background: #f8f8fd; border: 1px solid #eeeef8;
        border-radius: 10px; padding: 0.7rem 0.9rem;
    }
    .fcard.hi { background: #eef2ff; border-color: #c7d2fe; }
    .fkey {
        font-size: 0.57rem; color: #b0b0d0;
        letter-spacing: 0.12em; text-transform: uppercase;
        margin-bottom: 0.25rem; font-weight: 600;
    }
    .fval {
        font-size: 0.84rem; color: #2a2a4a; font-weight: 500;
        line-height: 1.4; word-break: break-word;
    }
    .fcard.hi .fval { color: #3730a3; }

    /* Tags */
    .trow { display: flex; flex-wrap: wrap; gap: 0.4rem; margin: 0.3rem 0 1rem; }
    .tag {
        background: #f0f0fa; border: 1px solid #e0e0f0;
        border-radius: 20px; padding: 0.18rem 0.75rem;
        font-size: 0.72rem; color: #6060b0; font-weight: 500;
    }

    /* Summary */
    .sumbox {
        background: #f8f8fd; border: 1px solid #eeeef8;
        border-radius: 10px; padding: 0.9rem 1.1rem;
        font-size: 0.85rem; color: #5050a0; line-height: 1.8;
        margin-top: 0.25rem;
    }

    /* Expander */
    details { margin-top: 0.8rem !important; }
    summary {
        font-size: 0.72rem !important; color: #a0a0c0 !important;
        font-family: 'Inter', sans-serif !important;
    }

    .stAlert { border-radius: 10px !important; }
    .stSpinner > div { border-top-color: #6366f1 !important; }
    </style>
    """, unsafe_allow_html=True)

    # ── HEADER ────────────────────────────────────────────────────────────────
    st.markdown('<p class="page-title">Movie Extractor</p>', unsafe_allow_html=True)
    st.markdown('<p class="page-sub">Structured data from any movie description</p>', unsafe_allow_html=True)

    # ── MODEL + SCHEMA ────────────────────────────────────────────────────────
    llm = ChatMistralAI(model="mistral-small-2603")

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

    prompt_tmpl = ChatPromptTemplate.from_messages([
        ("system", "Extract Movie Information from the paragraph.\nReturn ONLY valid JSON.\n{format_instructions}"),
        ("human", "{paragraph}")
    ])

    # ── INPUT ─────────────────────────────────────────────────────────────────
    st.markdown('<p class="section-label">Movie Paragraph</p>', unsafe_allow_html=True)
    paragraph = st.text_area(
        "paragraph",
        height=160,
        placeholder="e.g. Avengers: Endgame is a 2019 superhero film directed by the Russo brothers, starring Robert Downey Jr…",
        label_visibility="collapsed"
    )

    st.markdown('<div style="height:0.4rem"></div>', unsafe_allow_html=True)
    clicked = st.button("✦  Extract Information")

    # ── RESULTS ───────────────────────────────────────────────────────────────
    if clicked:
        if not paragraph.strip():
            st.warning("Please paste a movie paragraph first.")
        else:
            with st.spinner("Extracting…"):
                try:
                    final_prompt = prompt_tmpl.invoke({
                        "paragraph": paragraph,
                        "format_instructions": parser.get_format_instructions()
                    })
                    res = llm.invoke(final_prompt)
                    movie = parser.parse(res.content)

                    st.markdown('<div class="result-card">', unsafe_allow_html=True)
                    st.markdown("""
                    <div class="result-top">
                        <div class="green-dot"></div>
                        <div class="result-ok">Extraction Successful</div>
                    </div>
                    """, unsafe_allow_html=True)

                    # Field grid
                    fields = [
                        ("Title", movie.title, True),
                        ("Genre", movie.genre, False),
                        ("Director", movie.director, False),
                        ("Release Date", movie.release_date, False),
                        ("Language", movie.language, False),
                        ("Country", movie.country, False),
                        ("Duration", movie.duration, False),
                        ("Rating", str(movie.rating) if movie.rating else "—", False),
                    ]
                    html = '<div class="fgrid">'
                    for key, val, hi in fields:
                        cls = "fcard hi" if hi else "fcard"
                        html += f'<div class="{cls}"><div class="fkey">{key}</div><div class="fval">{val}</div></div>'
                    html += '</div>'
                    st.markdown(html, unsafe_allow_html=True)

                    # Cast
                    st.markdown('<p class="section-label">Cast</p>', unsafe_allow_html=True)
                    cast_html = '<div class="trow">' + "".join(f'<span class="tag">{c}</span>' for c in movie.cast) + '</div>'
                    st.markdown(cast_html, unsafe_allow_html=True)

                    # Themes
                    st.markdown('<p class="section-label">Themes</p>', unsafe_allow_html=True)
                    theme_html = '<div class="trow">' + "".join(f'<span class="tag">{t}</span>' for t in movie.themes) + '</div>'
                    st.markdown(theme_html, unsafe_allow_html=True)

                    # Key Highlights
                    st.markdown('<p class="section-label">Key Highlights</p>', unsafe_allow_html=True)
                    hl_html = '<div class="trow">' + "".join(f'<span class="tag">{h}</span>' for h in movie.key_highlights) + '</div>'
                    st.markdown(hl_html, unsafe_allow_html=True)

                    # Summary
                    st.markdown('<p class="section-label">Summary</p>', unsafe_allow_html=True)
                    safe_summary = movie.summary.replace("<", "&lt;").replace(">", "&gt;")
                    st.markdown(f'<div class="sumbox">{safe_summary}</div>', unsafe_allow_html=True)

                    st.markdown('</div>', unsafe_allow_html=True)  # close result-card

                    with st.expander("View raw JSON"):
                        st.json(movie.dict())

                except Exception as e:
                    st.error(f"Extraction failed: {str(e)}")