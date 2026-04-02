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
    @import url('https://fonts.googleapis.com/css2?family=Syne:wght@700;800&family=DM+Mono:wght@300;400;500&display=swap');

    .mx-title {
        font-family: 'Syne', sans-serif;
        font-weight: 800;
        font-size: 1.9rem;
        letter-spacing: -0.03em;
        color: #e8e8f0;
        line-height: 1.1;
    }
    .mx-subtitle {
        font-size: 0.63rem;
        color: #3e3e4f;
        letter-spacing: 0.16em;
        text-transform: uppercase;
        margin-top: 0.2rem;
        margin-bottom: 2rem;
    }
    .section-label {
        font-size: 0.6rem;
        color: #3e3e4f;
        letter-spacing: 0.16em;
        text-transform: uppercase;
        margin-bottom: 0.6rem;
    }

    /* ── Text area ── */
    .stTextArea textarea {
        background: rgba(255,255,255,0.03) !important;
        border: 1px solid rgba(255,255,255,0.08) !important;
        border-radius: 10px !important;
        color: #c9c9d3 !important;
        font-family: 'DM Mono', monospace !important;
        font-size: 0.82rem !important;
        line-height: 1.7 !important;
        resize: vertical !important;
    }
    .stTextArea textarea:focus {
        border-color: rgba(180,170,255,0.3) !important;
        box-shadow: 0 0 0 3px rgba(180,170,255,0.06) !important;
    }
    .stTextArea textarea::placeholder { color: #2e2e3a !important; }
    .stTextArea label {
        font-family: 'DM Mono', monospace !important;
        font-size: 0.68rem !important;
        color: #3e3e4f !important;
        letter-spacing: 0.14em !important;
        text-transform: uppercase !important;
    }

    /* ── Extract button ── */
    .stButton > button {
        background: rgba(180,170,255,0.1) !important;
        border: 1px solid rgba(180,170,255,0.25) !important;
        border-radius: 9px !important;
        color: #c8c4f8 !important;
        font-family: 'DM Mono', monospace !important;
        font-size: 0.78rem !important;
        font-weight: 500 !important;
        padding: 0.55rem 1.4rem !important;
        transition: all 0.18s ease !important;
        letter-spacing: 0.05em !important;
    }
    .stButton > button:hover {
        background: rgba(180,170,255,0.18) !important;
        border-color: rgba(180,170,255,0.4) !important;
    }
    .stButton > button:active {
        transform: scale(0.98) !important;
    }

    /* ── Output area ── */
    .output-header {
        display: flex;
        align-items: center;
        gap: 0.6rem;
        margin: 1.8rem 0 0.8rem;
    }
    .output-label {
        font-size: 0.6rem;
        color: #3e3e4f;
        letter-spacing: 0.16em;
        text-transform: uppercase;
    }
    .output-dot {
        width: 6px; height: 6px;
        border-radius: 50%;
        background: #4a9a6a;
    }

    /* JSON viewer */
    .stJson {
        background: rgba(255,255,255,0.02) !important;
        border: 1px solid rgba(255,255,255,0.07) !important;
        border-radius: 10px !important;
        font-family: 'DM Mono', monospace !important;
        font-size: 0.78rem !important;
    }

    /* Field cards */
    .field-grid {
        display: grid;
        grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
        gap: 0.6rem;
        margin-bottom: 1.5rem;
    }
    .field-card {
        background: rgba(255,255,255,0.02);
        border: 1px solid rgba(255,255,255,0.06);
        border-radius: 8px;
        padding: 0.65rem 0.85rem;
    }
    .field-key {
        font-size: 0.58rem;
        color: #3e3e4f;
        letter-spacing: 0.12em;
        text-transform: uppercase;
        margin-bottom: 0.25rem;
    }
    .field-val {
        font-family: 'DM Mono', monospace;
        font-size: 0.78rem;
        color: #c8c4f8;
        line-height: 1.4;
        word-break: break-word;
    }
    .field-card.accent {
        border-color: rgba(180,170,255,0.15);
        background: rgba(180,170,255,0.05);
    }

    /* Tag list */
    .tag-row { display: flex; flex-wrap: wrap; gap: 0.4rem; margin-top: 0.25rem; }
    .tag {
        background: rgba(255,255,255,0.04);
        border: 1px solid rgba(255,255,255,0.08);
        border-radius: 20px;
        padding: 0.15rem 0.6rem;
        font-size: 0.65rem;
        color: #888898;
    }

    /* Alerts */
    .stAlert {
        background: rgba(255,255,255,0.02) !important;
        border-radius: 8px !important;
        font-family: 'DM Mono', monospace !important;
        font-size: 0.75rem !important;
    }
    .stSpinner > div { border-top-color: #9e9ac8 !important; }

    .divider-line {
        height: 1px;
        background: linear-gradient(90deg, transparent, rgba(255,255,255,0.05), transparent);
        margin: 0.5rem 0 1.5rem;
    }
    </style>
    """, unsafe_allow_html=True)

    # ── HEADER ────────────────────────────────────────────────────────────────
    st.markdown("""
    <div class="mx-title">Movie Extractor</div>
    <div class="mx-subtitle">Structured data from any movie paragraph</div>
    """, unsafe_allow_html=True)

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

    prompt = ChatPromptTemplate.from_messages([
        ("system", "Extract Movie Information from the paragraph.\n\nReturn ONLY valid JSON.\n\n{format_instructions}"),
        ("human", "{paragraph}")
    ])

    # ── INPUT ─────────────────────────────────────────────────────────────────
    st.markdown('<div class="section-label">Movie Paragraph</div>', unsafe_allow_html=True)

    paragraph = st.text_area(
        label="Movie Paragraph",
        height=180,
        placeholder="e.g. Avengers: Endgame is a 2019 superhero film directed by the Russo brothers…",
        label_visibility="collapsed"
    )

    st.markdown('<div style="height:0.5rem"></div>', unsafe_allow_html=True)
    extract_clicked = st.button("⬡  Extract Information")

    # ── EXTRACT ───────────────────────────────────────────────────────────────
    if extract_clicked:
        if paragraph.strip() == "":
            st.warning("Enter a movie paragraph first.")
        else:
            with st.spinner("Extracting…"):
                try:
                    final_prompt = prompt.invoke({
                        "paragraph": paragraph,
                        "format_instructions": parser.get_format_instructions()
                    })
                    res = model.invoke(final_prompt)
                    movie = parser.parse(res.content)

                    st.markdown('<div class="divider-line"></div>', unsafe_allow_html=True)
                    st.markdown("""
                    <div class="output-header">
                        <div class="output-dot"></div>
                        <div class="output-label">Extraction Complete</div>
                    </div>
                    """, unsafe_allow_html=True)

                    # ── Visual field cards ────────────────────────────────────
                    simple_fields = {
                        "Title": movie.title,
                        "Genre": movie.genre,
                        "Director": movie.director,
                        "Release Date": movie.release_date,
                        "Language": movie.language,
                        "Country": movie.country,
                        "Duration": movie.duration,
                        "Rating": str(movie.rating) if movie.rating else "—",
                    }

                    cards_html = '<div class="field-grid">'
                    for key, val in simple_fields.items():
                        accent = "accent" if key == "Title" else ""
                        cards_html += f"""
                        <div class="field-card {accent}">
                            <div class="field-key">{key}</div>
                            <div class="field-val">{val}</div>
                        </div>"""
                    cards_html += '</div>'
                    st.markdown(cards_html, unsafe_allow_html=True)

                    # Cast
                    st.markdown('<div class="section-label" style="margin-top:0.5rem">Cast</div>', unsafe_allow_html=True)
                    tags = "".join([f'<span class="tag">{c}</span>' for c in movie.cast])
                    st.markdown(f'<div class="tag-row">{tags}</div>', unsafe_allow_html=True)

                    # Themes
                    st.markdown('<div class="section-label" style="margin-top:1rem">Themes</div>', unsafe_allow_html=True)
                    theme_tags = "".join([f'<span class="tag">{t}</span>' for t in movie.themes])
                    st.markdown(f'<div class="tag-row">{theme_tags}</div>', unsafe_allow_html=True)

                    # Key highlights
                    st.markdown('<div class="section-label" style="margin-top:1rem">Key Highlights</div>', unsafe_allow_html=True)
                    hl_tags = "".join([f'<span class="tag">{h}</span>' for h in movie.key_highlights])
                    st.markdown(f'<div class="tag-row">{hl_tags}</div>', unsafe_allow_html=True)

                    # Summary
                    st.markdown('<div class="section-label" style="margin-top:1.2rem">Summary</div>', unsafe_allow_html=True)
                    st.markdown(f"""
                    <div class="field-card" style="max-width:100%">
                        <div class="field-val" style="color:#9898b0;font-size:0.8rem">{movie.summary}</div>
                    </div>
                    """, unsafe_allow_html=True)

                    # Raw JSON toggle
                    st.markdown('<div style="height:1rem"></div>', unsafe_allow_html=True)
                    with st.expander("View raw JSON"):
                        st.json(movie.dict())

                except Exception as e:
                    st.error(f"Extraction failed: {str(e)}")