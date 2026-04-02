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
import os

from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from langchain_mistralai import ChatMistralAI

from pydantic import BaseModel
from typing import List, Optional

load_dotenv()


def show():
    # ── CSS ───────────────────────────────────────────────────────────────────
    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Space+Grotesk:wght@500;600;700&display=swap');

    [data-testid="stAppViewContainer"] { background-color: #f5f4f0 !important; }

    .mx-title {
        font-family: 'Space Grotesk', sans-serif;
        font-weight: 700;
        font-size: 2rem;
        color: #1a1a2e;
        letter-spacing: -0.03em;
        line-height: 1.1;
        margin-bottom: 0.25rem;
    }
    .mx-sub {
        font-size: 0.72rem;
        color: #9090a8;
        letter-spacing: 0.1em;
        text-transform: uppercase;
        margin-bottom: 2rem;
    }
    .section-label {
        font-size: 0.65rem;
        color: #a0a0b8;
        letter-spacing: 0.14em;
        text-transform: uppercase;
        margin-bottom: 0.6rem;
        font-family: 'Inter', sans-serif;
        font-weight: 500;
    }

    /* Input card */
    .input-card {
        background: #ffffff;
        border: 1.5px solid #e8e8f0;
        border-radius: 16px;
        padding: 1.5rem;
        box-shadow: 0 2px 8px rgba(0,0,0,0.05);
        margin-bottom: 1.25rem;
    }

    /* Text area */
    .stTextArea textarea {
        background: #fafafa !important;
        border: 1.5px solid #e8e8f4 !important;
        border-radius: 10px !important;
        color: #1a1a2e !important;
        font-family: 'Inter', sans-serif !important;
        font-size: 0.88rem !important;
        line-height: 1.7 !important;
    }
    .stTextArea textarea:focus {
        border-color: #6366f1 !important;
        box-shadow: 0 0 0 3px rgba(99,102,241,0.08) !important;
    }
    .stTextArea textarea::placeholder { color: #c8c8e0 !important; }
    .stTextArea label { display: none !important; }

    /* Extract button */
    .stButton > button {
        background: #6366f1 !important;
        border: none !important;
        border-radius: 10px !important;
        color: #ffffff !important;
        font-family: 'Inter', sans-serif !important;
        font-size: 0.82rem !important;
        font-weight: 600 !important;
        padding: 0.65rem 1.8rem !important;
        transition: all 0.18s ease !important;
        letter-spacing: 0.02em !important;
        box-shadow: 0 4px 14px rgba(99,102,241,0.3) !important;
    }
    .stButton > button:hover {
        background: #4f46e5 !important;
        box-shadow: 0 6px 20px rgba(99,102,241,0.4) !important;
        transform: translateY(-1px) !important;
    }
    .stButton > button:active { transform: translateY(0px) !important; }

    /* ── Results ── */
    .results-wrapper {
        background: #ffffff;
        border: 1.5px solid #e8e8f0;
        border-radius: 16px;
        padding: 1.5rem;
        box-shadow: 0 2px 8px rgba(0,0,0,0.05);
        margin-top: 1.5rem;
    }
    .result-header {
        display: flex;
        align-items: center;
        gap: 0.6rem;
        margin-bottom: 1.2rem;
        padding-bottom: 0.8rem;
        border-bottom: 1px solid #f0f0f8;
    }
    .result-dot {
        width: 8px; height: 8px;
        border-radius: 50%;
        background: #22c55e;
        box-shadow: 0 0 6px rgba(34,197,94,0.4);
    }
    .result-label {
        font-family: 'Inter', sans-serif;
        font-size: 0.65rem;
        color: #22c55e;
        letter-spacing: 0.14em;
        text-transform: uppercase;
        font-weight: 600;
    }

    /* Field grid */
    .field-grid {
        display: grid;
        grid-template-columns: repeat(auto-fill, minmax(185px, 1fr));
        gap: 0.7rem;
        margin-bottom: 1.2rem;
    }
    .field-card {
        background: #f8f8fc;
        border: 1px solid #eeeef8;
        border-radius: 10px;
        padding: 0.75rem 0.9rem;
    }
    .field-card.highlight {
        background: #eef2ff;
        border-color: #c7d2fe;
    }
    .field-key {
        font-size: 0.58rem;
        color: #a0a0c0;
        letter-spacing: 0.12em;
        text-transform: uppercase;
        margin-bottom: 0.3rem;
        font-family: 'Inter', sans-serif;
        font-weight: 500;
    }
    .field-val {
        font-family: 'Inter', sans-serif;
        font-size: 0.85rem;
        color: #2a2a4a;
        font-weight: 500;
        line-height: 1.4;
        word-break: break-word;
    }
    .field-card.highlight .field-val { color: #3730a3; }

    /* Tags */
    .tag-row { display: flex; flex-wrap: wrap; gap: 0.4rem; margin-top: 0.3rem; margin-bottom: 0.8rem; }
    .tag {
        background: #f0f0fa;
        border: 1px solid #e0e0f0;
        border-radius: 20px;
        padding: 0.2rem 0.75rem;
        font-size: 0.72rem;
        color: #6060a0;
        font-family: 'Inter', sans-serif;
        font-weight: 500;
    }

    /* Summary */
    .summary-box {
        background: #f8f8fc;
        border: 1px solid #eeeef8;
        border-radius: 10px;
        padding: 0.9rem 1.1rem;
        margin-top: 0.3rem;
    }
    .summary-text {
        font-family: 'Inter', sans-serif;
        font-size: 0.85rem;
        color: #5050a0;
        line-height: 1.8;
    }

    /* JSON expander */
    .stExpander {
        background: #fafafa !important;
        border: 1px solid #eeeef0 !important;
        border-radius: 10px !important;
        margin-top: 0.8rem !important;
    }

    /* Warning / error */
    .stAlert { border-radius: 10px !important; font-family: 'Inter', sans-serif !important; font-size: 0.8rem !important; }
    .stSpinner > div { border-top-color: #6366f1 !important; }

    .page-divider { height: 1px; background: #e8e8f0; margin: 0.5rem 0 1.5rem; }
    </style>
    """, unsafe_allow_html=True)

    # ── HEADER ────────────────────────────────────────────────────────────────
    st.markdown('<div class="mx-title">Movie Extractor</div>', unsafe_allow_html=True)
    st.markdown('<div class="mx-sub">Structured data from any movie paragraph</div>', unsafe_allow_html=True)

    # ── MODEL + SCHEMA ────────────────────────────────────────────────────────
    model = ChatMistralAI(model="mistral-small-2603")

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

    prompt_template = ChatPromptTemplate.from_messages([
        ("system", "Extract Movie Information from the paragraph.\n\nReturn ONLY valid JSON.\n\n{format_instructions}"),
        ("human", "{paragraph}")
    ])

    # ── INPUT CARD ────────────────────────────────────────────────────────────
    st.markdown('<div class="input-card">', unsafe_allow_html=True)
    st.markdown('<div class="section-label">Movie Paragraph</div>', unsafe_allow_html=True)

    paragraph = st.text_area(
        label="paragraph",
        height=160,
        placeholder="e.g. Avengers: Endgame is a 2019 superhero film directed by the Russo brothers, starring Robert Downey Jr., Chris Evans…",
        label_visibility="collapsed"
    )
    st.markdown('<div style="height:0.5rem"></div>', unsafe_allow_html=True)
    extract_clicked = st.button("✦  Extract Information")
    st.markdown('</div>', unsafe_allow_html=True)

    # ── EXTRACT + RENDER ──────────────────────────────────────────────────────
    if extract_clicked:
        if not paragraph.strip():
            st.warning("Please enter a movie paragraph first.")
        else:
            with st.spinner("Extracting structured data…"):
                try:
                    final_prompt = prompt_template.invoke({
                        "paragraph": paragraph,
                        "format_instructions": parser.get_format_instructions()
                    })
                    res = model.invoke(final_prompt)
                    movie = parser.parse(res.content)

                    # ── Results card ──────────────────────────────────────────
                    st.markdown('<div class="results-wrapper">', unsafe_allow_html=True)
                    st.markdown("""
                    <div class="result-header">
                        <div class="result-dot"></div>
                        <div class="result-label">Extraction successful</div>
                    </div>
                    """, unsafe_allow_html=True)

                    # Field grid
                    fields = {
                        "Title":        (movie.title, True),
                        "Genre":        (movie.genre, False),
                        "Director":     (movie.director, False),
                        "Release Date": (movie.release_date, False),
                        "Language":     (movie.language, False),
                        "Country":      (movie.country, False),
                        "Duration":     (movie.duration, False),
                        "Rating":       (str(movie.rating) if movie.rating else "—", False),
                    }

                    cards_html = '<div class="field-grid">'
                    for key, (val, hi) in fields.items():
                        cls = "field-card highlight" if hi else "field-card"
                        cards_html += f'<div class="{cls}"><div class="field-key">{key}</div><div class="field-val">{val}</div></div>'
                    cards_html += '</div>'
                    st.markdown(cards_html, unsafe_allow_html=True)

                    # Cast
                    st.markdown('<div class="section-label">Cast</div>', unsafe_allow_html=True)
                    cast_tags = "".join([f'<span class="tag">{c}</span>' for c in movie.cast])
                    st.markdown(f'<div class="tag-row">{cast_tags}</div>', unsafe_allow_html=True)

                    # Themes
                    st.markdown('<div class="section-label">Themes</div>', unsafe_allow_html=True)
                    theme_tags = "".join([f'<span class="tag">{t}</span>' for t in movie.themes])
                    st.markdown(f'<div class="tag-row">{theme_tags}</div>', unsafe_allow_html=True)

                    # Key Highlights
                    st.markdown('<div class="section-label">Key Highlights</div>', unsafe_allow_html=True)
                    hl_tags = "".join([f'<span class="tag">{h}</span>' for h in movie.key_highlights])
                    st.markdown(f'<div class="tag-row">{hl_tags}</div>', unsafe_allow_html=True)

                    # Summary
                    st.markdown('<div class="section-label" style="margin-top:0.5rem">Summary</div>', unsafe_allow_html=True)
                    summary_safe = movie.summary.replace("<", "&lt;").replace(">", "&gt;")
                    st.markdown(f'<div class="summary-box"><div class="summary-text">{summary_safe}</div></div>', unsafe_allow_html=True)

                    st.markdown('</div>', unsafe_allow_html=True)  # close results-wrapper

                    # Raw JSON
                    with st.expander("View raw JSON"):
                        st.json(movie.dict())

                except Exception as e:
                    st.error(f"Extraction failed: {str(e)}")