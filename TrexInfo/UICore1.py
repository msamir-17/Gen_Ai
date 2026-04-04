import streamlit as st
from dotenv import load_dotenv

from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from langchain_mistralai import ChatMistralAI

from pydantic import BaseModel
from typing import List, Optional

load_dotenv()

# ── SCHEMA ────────────────────────────────────────────────────────────────────
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

def show():

    # ── CSS ───────────────────────────────────────────────────────────────────
    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Syne:wght@700;800&family=DM+Sans:wght@400;500&display=swap');

    /* Text area */
    .stTextArea textarea {
        background: rgba(255,255,255,0.04) !important;
        border: 1px solid rgba(124,58,237,0.3) !important;
        border-radius: 12px !important;
        color: #f1f0ff !important;
        font-family: 'DM Sans', sans-serif !important;
        font-size: 0.9rem !important;
        resize: vertical !important;
        transition: border-color 0.2s ease !important;
    }
    .stTextArea textarea:focus {
        border-color: #7c3aed !important;
        box-shadow: 0 0 0 2px rgba(124,58,237,0.18) !important;
    }
    .stTextArea textarea::placeholder { color: #8b8aab !important; }
    .stTextArea label {
        color: #c4c3e0 !important;
        font-family: 'DM Sans', sans-serif !important;
        font-size: 0.85rem !important;
        font-weight: 500 !important;
    }

    /* Extract button */
    .stButton > button {
        background: linear-gradient(135deg, #7c3aed, #a855f7) !important;
        color: #fff !important;
        font-family: 'DM Sans', sans-serif !important;
        font-weight: 600 !important;
        font-size: 0.92rem !important;
        border: none !important;
        border-radius: 12px !important;
        padding: 10px 28px !important;
        box-shadow: 0 4px 18px rgba(124,58,237,0.4) !important;
        transition: all 0.2s ease !important;
        cursor: pointer !important;
    }
    .stButton > button:hover {
        transform: translateY(-2px) !important;
        box-shadow: 0 6px 26px rgba(124,58,237,0.6) !important;
    }
    .stButton > button:active { transform: translateY(0) !important; }

    /* Success / warning / error */
    [data-testid="stAlert"] {
        border-radius: 12px !important;
        font-family: 'DM Sans', sans-serif !important;
    }

    /* JSON output */
    [data-testid="stJson"] {
        background: rgba(255,255,255,0.03) !important;
        border: 1px solid rgba(124,58,237,0.2) !important;
        border-radius: 12px !important;
    }

    /* Divider */
    hr { border-color: rgba(124,58,237,0.2) !important; }

    /* Result cards */
    .result-card {
        background: rgba(255,255,255,0.03);
        border: 1px solid rgba(124,58,237,0.2);
        border-radius: 14px;
        padding: 16px 20px;
        margin-bottom: 12px;
        font-family: 'DM Sans', sans-serif;
    }
    .result-card-title {
        font-size: 0.6rem;
        font-weight: 700;
        letter-spacing: 0.13em;
        text-transform: uppercase;
        color: #8b8aab;
        margin-bottom: 6px;
    }
    .result-card-value {
        font-size: 0.92rem;
        color: #f1f0ff;
        line-height: 1.5;
    }
    .tag {
        display: inline-block;
        background: rgba(124,58,237,0.18);
        border: 1px solid rgba(124,58,237,0.3);
        border-radius: 99px;
        padding: 2px 12px;
        font-size: 0.75rem;
        color: #c084fc;
        margin: 2px 3px 2px 0;
    }
    .tag-cyan {
        background: rgba(6,182,212,0.12);
        border-color: rgba(6,182,212,0.3);
        color: #67e8f9;
    }
    .rating-star {
        font-size: 1.4rem;
        color: #f59e0b;
    }
    .highlight-item {
        display: flex;
        align-items: flex-start;
        gap: 8px;
        margin-bottom: 5px;
        font-size: 0.88rem;
        color: #c4c3e0;
    }
    .highlight-dot {
        width: 6px; height: 6px;
        min-width: 6px;
        background: #7c3aed;
        border-radius: 50%;
        margin-top: 6px;
    }
    </style>
    """, unsafe_allow_html=True)

    # ── HEADER ────────────────────────────────────────────────────────────────
    st.markdown("""
    <div style="padding: 8px 0 4px 0;">
        <div style="
            font-family: 'Syne', sans-serif;
            font-size: 2rem;
            font-weight: 800;
            background: linear-gradient(135deg, #06b6d4, #a855f7, #ec4899);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            line-height: 1.2;
            margin-bottom: 4px;">
            🎬 Movie Info Extractor
        </div>
        <div style="color:#8b8aab; font-size:0.82rem; letter-spacing:0.04em;">
            Paste any movie paragraph — get clean structured data instantly
        </div>
    </div>
    <hr style="margin: 14px 0 20px 0;">
    """, unsafe_allow_html=True)

    # ── INPUT ─────────────────────────────────────────────────────────────────
    st.markdown("""
    <div style="font-size:0.6rem;font-weight:700;letter-spacing:0.13em;
                text-transform:uppercase;color:#8b8aab;margin-bottom:6px;">
        📄 Enter Movie Paragraph
    </div>""", unsafe_allow_html=True)

    paragraph = st.text_area(
        label="Movie Paragraph",
        label_visibility="collapsed",
        height=180,
        placeholder="Example: Avengers is a superhero film directed by Joss Whedon, released in 2012..."
    )

    st.markdown("<div style='height:6px'></div>", unsafe_allow_html=True)

    col1, col2, col3 = st.columns([1, 1.4, 1])
    with col2:
        extract_clicked = st.button("✨  Extract Information", use_container_width=True)

    # ── EXTRACT ───────────────────────────────────────────────────────────────
    if extract_clicked:
        if not paragraph.strip():
            st.warning("⚠️ Please enter some movie text first.")
        else:
            model  = ChatMistralAI(model="mistral-small-2603")
            parser = PydanticOutputParser(pydantic_object=Movie)
            prompt = ChatPromptTemplate.from_messages([
                ("system", "Extract Movie Information from the paragraph.\nReturn ONLY valid JSON.\n{format_instructions}"),
                ("human", "{paragraph}")
            ])

            with st.spinner("Extracting movie data..."):
                try:
                    final_prompt = prompt.invoke({
                        "paragraph": paragraph,
                        "format_instructions": parser.get_format_instructions()
                    })
                    res        = model.invoke(final_prompt)
                    movie_data = parser.parse(res.content)

                    # ── RESULTS ───────────────────────────────────────────────
                    st.markdown("<hr style='margin: 20px 0 18px 0;'>", unsafe_allow_html=True)
                    st.markdown("""
                    <div style="font-family:'Syne',sans-serif;font-size:1.1rem;
                                font-weight:700;color:#f1f0ff;margin-bottom:14px;">
                        ✅ Extraction Complete
                    </div>""", unsafe_allow_html=True)

                    # Row 1: Title + Rating
                    c1, c2 = st.columns([2, 1])
                    with c1:
                        st.markdown(f"""
                        <div class="result-card">
                            <div class="result-card-title">🎬 Title</div>
                            <div style="font-family:'Syne',sans-serif;font-size:1.3rem;
                                        font-weight:800;background:linear-gradient(135deg,#a855f7,#ec4899);
                                        -webkit-background-clip:text;-webkit-text-fill-color:transparent;
                                        background-clip:text;">
                                {movie_data.title}
                            </div>
                        </div>""", unsafe_allow_html=True)
                    with c2:
                        rating_val = movie_data.rating if movie_data.rating else "N/A"
                        stars = int(round(movie_data.rating / 2)) if movie_data.rating else 0
                        star_str = "⭐" * stars + "☆" * (5 - stars)
                        st.markdown(f"""
                        <div class="result-card" style="text-align:center;">
                            <div class="result-card-title">⭐ Rating</div>
                            <div style="font-size:1.5rem;font-weight:800;color:#f59e0b;">
                                {rating_val}
                            </div>
                            <div style="font-size:0.75rem;color:#8b8aab;">{star_str}</div>
                        </div>""", unsafe_allow_html=True)

                    # Row 2: Director, Genre, Language, Country, Duration, Release
                    meta = [
                        ("🎥 Director",     movie_data.director),
                        ("🎭 Genre",        movie_data.genre),
                        ("🌐 Language",     movie_data.language),
                        ("🗺️ Country",      movie_data.country),
                        ("⏱️ Duration",     movie_data.duration),
                        ("📅 Release Date", movie_data.release_date),
                    ]
                    m1, m2, m3 = st.columns(3)
                    for idx, (label, value) in enumerate(meta):
                        col = [m1, m2, m3][idx % 3]
                        with col:
                            st.markdown(f"""
                            <div class="result-card">
                                <div class="result-card-title">{label}</div>
                                <div class="result-card-value">{value}</div>
                            </div>""", unsafe_allow_html=True)

                    # Row 3: Cast
                    cast_tags = "".join([f'<span class="tag">🎭 {c}</span>' for c in movie_data.cast])
                    st.markdown(f"""
                    <div class="result-card">
                        <div class="result-card-title">🎬 Cast</div>
                        <div style="margin-top:4px">{cast_tags}</div>
                    </div>""", unsafe_allow_html=True)

                    # Row 4: Themes
                    theme_tags = "".join([f'<span class="tag tag-cyan">{t}</span>' for t in movie_data.themes])
                    st.markdown(f"""
                    <div class="result-card">
                        <div class="result-card-title">💡 Themes</div>
                        <div style="margin-top:4px">{theme_tags}</div>
                    </div>""", unsafe_allow_html=True)

                    # Row 5: Key Highlights
                    highlights_html = "".join([
                        f'<div class="highlight-item"><div class="highlight-dot"></div><span>{h}</span></div>'
                        for h in movie_data.key_highlights
                    ])
                    st.markdown(f"""
                    <div class="result-card">
                        <div class="result-card-title">✨ Key Highlights</div>
                        <div style="margin-top:6px">{highlights_html}</div>
                    </div>""", unsafe_allow_html=True)

                    # Row 6: Summary
                    st.markdown(f"""
                    <div class="result-card" style="border-color:rgba(6,182,212,0.25);
                        background:rgba(6,182,212,0.04);">
                        <div class="result-card-title" style="color:#67e8f9;">📝 Summary</div>
                        <div class="result-card-value" style="color:#cbd5e1;line-height:1.7;">
                            {movie_data.summary}
                        </div>
                    </div>""", unsafe_allow_html=True)

                    # Raw JSON toggle
                    with st.expander("🔍 View Raw JSON"):
                        st.json(movie_data.dict())

                except Exception as e:
                    st.error("❌ Extraction failed. Check your input or API key.")
                    with st.expander("Error details"):
                        st.code(str(e))