from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
import os
load_dotenv()

import streamlit as st
from langchain_mistralai import ChatMistralAI

st.set_page_config(page_title="Extract AI", page_icon="📌", layout="centered")

# ── Model ─────────────────────────────────────────────────────────────────────
@st.cache_resource
def get_model():
    return ChatMistralAI(model="mistral-small-2603", max_tokens=500)
model = get_model()

# ── Prompt (unchanged from original) ─────────────────────────────────────────
prompt = ChatPromptTemplate.from_messages([
    ("system", """
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
    ("human", """
Extract information and summarize from the paragraph:

{paragraph}
""")
])

# ── CSS ───────────────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;500;600;700&family=Fira+Code:wght@300;400;500&display=swap');

:root {
    --bg:        #080b12;
    --surface:   rgba(255,255,255,0.03);
    --border:    rgba(255,255,255,0.07);
    --accent:    #6366f1;
    --accent2:   #a855f7;
    --teal:      #2dd4bf;
    --text:      #e2e8f0;
    --muted:     #64748b;
    --faint:     #1e293b;
}

html, body, [data-testid="stAppViewContainer"] {
    background: var(--bg) !important;
    font-family: 'Fira Code', monospace;
}
[data-testid="stAppViewContainer"] {
    background:
        radial-gradient(ellipse 80% 50% at 50% -8%, rgba(99,102,241,0.18) 0%, transparent 60%),
        radial-gradient(ellipse 40% 30% at 95% 90%, rgba(168,85,247,0.12) 0%, transparent 50%),
        var(--bg) !important;
}
[data-testid="stHeader"], header { background: transparent !important; }
[data-testid="stToolbar"], #MainMenu, footer { display: none !important; }
.main .block-container { max-width: 740px; padding: 3rem 2rem 6rem; margin: auto; }

/* ── TOP BAR ── */
.topbar {
    display: flex;
    align-items: center;
    justify-content: space-between;
    margin-bottom: 2.8rem;
}
.topbar-logo {
    display: flex;
    align-items: center;
    gap: 0.6rem;
}
.logo-dot {
    width: 34px; height: 34px;
    border-radius: 9px;
    background: linear-gradient(135deg, var(--accent), var(--accent2));
    display: flex; align-items: center; justify-content: center;
    font-size: 1rem;
    box-shadow: 0 0 18px rgba(99,102,241,0.4);
}
.logo-name {
    font-family: 'Space Grotesk', sans-serif;
    font-weight: 700;
    font-size: 1.1rem;
    color: var(--text);
    letter-spacing: -0.02em;
}
.topbar-tag {
    font-size: 0.6rem;
    letter-spacing: 0.14em;
    text-transform: uppercase;
    color: var(--muted);
    border: 1px solid var(--border);
    border-radius: 20px;
    padding: 0.22rem 0.7rem;
}

/* ── HERO ── */
.hero {
    margin-bottom: 2.5rem;
}
.hero-title {
    font-family: 'Space Grotesk', sans-serif;
    font-weight: 700;
    font-size: 2.6rem;
    letter-spacing: -0.04em;
    line-height: 1.1;
    color: var(--text);
    margin-bottom: 0.6rem;
}
.hero-title em {
    font-style: normal;
    background: linear-gradient(120deg, var(--accent), var(--accent2));
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
}
.hero-desc {
    font-size: 0.78rem;
    color: var(--muted);
    line-height: 1.7;
    max-width: 480px;
    letter-spacing: 0.02em;
}

/* ── INPUT CARD ── */
.input-card {
    background: var(--surface);
    border: 1px solid var(--border);
    border-radius: 16px;
    padding: 1.5rem 1.6rem 1.4rem;
    margin-bottom: 1.2rem;
    position: relative;
    overflow: hidden;
}
.input-card::before {
    content: '';
    position: absolute;
    inset: 0;
    border-radius: 16px;
    padding: 1px;
    background: linear-gradient(135deg, rgba(99,102,241,0.3), transparent 60%);
    -webkit-mask: linear-gradient(#fff 0 0) content-box, linear-gradient(#fff 0 0);
    -webkit-mask-composite: xor;
    mask-composite: exclude;
    pointer-events: none;
}
.field-label {
    font-size: 0.62rem;
    letter-spacing: 0.18em;
    text-transform: uppercase;
    color: var(--accent);
    margin-bottom: 0.7rem;
    display: flex;
    align-items: center;
    gap: 0.4rem;
}
.field-label::before { content: '//'; color: var(--muted); }

[data-testid="stTextArea"] label { display: none !important; }
[data-testid="stTextArea"] textarea {
    background: rgba(0,0,0,0.25) !important;
    border: 1px solid rgba(255,255,255,0.06) !important;
    border-radius: 10px !important;
    color: var(--text) !important;
    font-family: 'Fira Code', monospace !important;
    font-size: 0.83rem !important;
    line-height: 1.75 !important;
    padding: 1rem 1.1rem !important;
    transition: border-color 0.2s, box-shadow 0.2s !important;
    resize: vertical !important;
}
[data-testid="stTextArea"] textarea:focus {
    border-color: rgba(99,102,241,0.45) !important;
    box-shadow: 0 0 0 3px rgba(99,102,241,0.10) !important;
    outline: none !important;
}
[data-testid="stTextArea"] textarea::placeholder { color: #2d3748 !important; }

/* char count */
.char-pill {
    display: inline-flex;
    align-items: center;
    gap: 0.3rem;
    background: rgba(99,102,241,0.08);
    border: 1px solid rgba(99,102,241,0.15);
    border-radius: 20px;
    padding: 0.18rem 0.65rem;
    font-size: 0.6rem;
    color: var(--accent);
    letter-spacing: 0.08em;
    margin-top: 0.6rem;
    float: right;
}

/* ── BUTTON ── */
.stButton button {
    background: linear-gradient(135deg, var(--accent), var(--accent2)) !important;
    border: none !important;
    border-radius: 10px !important;
    color: #fff !important;
    font-family: 'Space Grotesk', sans-serif !important;
    font-size: 0.82rem !important;
    font-weight: 600 !important;
    letter-spacing: 0.04em !important;
    padding: 0.62rem 1.8rem !important;
    transition: all 0.2s !important;
    cursor: pointer !important;
    box-shadow: 0 4px 20px rgba(99,102,241,0.3) !important;
}
.stButton button:hover {
    transform: translateY(-2px) !important;
    box-shadow: 0 8px 28px rgba(99,102,241,0.45) !important;
}
.stButton button:active { transform: translateY(0) !important; }

/* ── RESULT ── */
.result-wrap {
    margin-top: 1.6rem;
    animation: fadeUp 0.35s ease both;
}
@keyframes fadeUp {
    from { opacity: 0; transform: translateY(12px); }
    to   { opacity: 1; transform: translateY(0); }
}
.result-topbar {
    display: flex;
    align-items: center;
    justify-content: space-between;
    margin-bottom: 0.8rem;
}
.result-title {
    font-family: 'Space Grotesk', sans-serif;
    font-size: 0.65rem;
    font-weight: 600;
    letter-spacing: 0.18em;
    text-transform: uppercase;
    color: var(--teal);
}
.result-badge {
    font-size: 0.58rem;
    letter-spacing: 0.1em;
    text-transform: uppercase;
    color: var(--muted);
    background: var(--faint);
    border-radius: 4px;
    padding: 0.18rem 0.55rem;
}
.result-box {
    background: rgba(0,0,0,0.3);
    border: 1px solid rgba(45,212,191,0.14);
    border-radius: 14px;
    padding: 1.6rem 1.8rem;
    position: relative;
    overflow: hidden;
}
.result-box::before {
    content: '';
    position: absolute;
    top: 0; left: 0; right: 0;
    height: 2px;
    background: linear-gradient(90deg, var(--accent), var(--teal), transparent);
    border-radius: 14px 14px 0 0;
}
.result-text {
    font-family: 'Fira Code', monospace;
    font-size: 0.83rem;
    line-height: 1.9;
    color: #cbd5e1;
    white-space: pre-wrap;
    word-break: break-word;
}

/* ── WARNING ── */
[data-testid="stAlert"] {
    background: rgba(245,158,11,0.08) !important;
    border: 1px solid rgba(245,158,11,0.2) !important;
    border-radius: 10px !important;
    color: #fbbf24 !important;
    font-family: 'Fira Code', monospace !important;
    font-size: 0.78rem !important;
}
</style>
""", unsafe_allow_html=True)

# ── TOP BAR ──────────────────────────────────────────────────────────────────
st.markdown("""
<div class="topbar">
    <div class="topbar-logo">
        <div class="logo-dot">📌</div>
        <div class="logo-name">ExtractAI</div>
    </div>
    <div class="topbar-tag">Powered by Mistral</div>
</div>
""", unsafe_allow_html=True)

# ── HERO ─────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="hero">
    <div class="hero-title">Paste text.<br><em>Get structure.</em></div>
    <div class="hero-desc">Drop any paragraph — a movie blurb, news article, book synopsis — and instantly extract key details with an AI summary.</div>
</div>
""", unsafe_allow_html=True)

# ── INPUT CARD ────────────────────────────────────────────────────────────────
st.markdown('<div class="input-card"><div class="field-label">Input Paragraph</div>', unsafe_allow_html=True)

para = st.text_area(
    label="paragraph",
    placeholder="e.g.  Inception is a 2010 science-fiction thriller directed by Christopher Nolan...",
    height=190,
    label_visibility="collapsed",
)

if para:
    st.markdown(f'<div class="char-pill">⬡ {len(para)} chars</div>', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)  # close input-card

# ── BUTTON ───────────────────────────────────────────────────────────────────
_, btn_col, _ = st.columns([1, 2, 1])
with btn_col:
    extract = st.button("📌 Extract Information", use_container_width=True)

# ── OUTPUT ───────────────────────────────────────────────────────────────────
if extract:
    if not para.strip():
        st.warning("Please paste a paragraph before extracting.")
    else:
        with st.spinner("Analyzing paragraph…"):
            final_prompt = prompt.invoke({"paragraph": para})
            res = model.invoke(final_prompt)

        st.markdown(f"""
<div class="result-wrap">
    <div class="result-topbar">
        <div class="result-title">✦ Extracted Output</div>
        <div class="result-badge">AI Generated</div>
    </div>
    <div class="result-box">
        <div class="result-text">{res.content}</div>
    </div>
</div>
""", unsafe_allow_html=True)