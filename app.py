# import streamlit as st

# # 1. Set Page Config ONLY ONCE here in the main file
# st.set_page_config(page_title="AI Portfolio Hub", page_icon="🚀", layout="wide")

# st.sidebar.title("🚀 My AI Portfolio")
# page = st.sidebar.radio("Go to:", ["Multi-Model Chatbot", "Aura Chat (Single)", "Movie Data Extractor"])

# if page == "Multi-Model Chatbot":
#     from chatModels import Multimodel_Chatbot
#     Multimodel_Chatbot.show() # <--- This calls the function inside the file

# elif page == "Aura Chat (Single)":
#     from chatModels import UI_ChatBot
#     UI_ChatBot.show() # <--- This calls the function inside the file

# elif page == "Movie Data Extractor":
#     from TrexInfo import UICore1
#     UICore1.show() # <--- This calls the function inside the file   


import streamlit as st

st.set_page_config(
    page_title="Multi-Aura Hub",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Space+Grotesk:wght@600;700&display=swap');

/* Global font + background */
html, body, [data-testid="stAppViewContainer"] {
    font-family: 'Inter', sans-serif !important;
    background-color: #f0efeb !important;
}

/* Hide Streamlit UI chrome */
[data-testid="stHeader"] { display: none !important; }
[data-testid="stToolbar"] { display: none !important; }
#MainMenu { display: none !important; }
footer { display: none !important; }

/* ─── SIDEBAR ─────────────────────────────────────────── */
[data-testid="stSidebar"] {
    background-color: #1c1b2e !important;
}
[data-testid="stSidebar"] > div:first-child {
    padding-top: 2rem !important;
    padding-left: 1.25rem !important;
    padding-right: 1.25rem !important;
}

/* Sidebar text overrides */
[data-testid="stSidebar"] p,
[data-testid="stSidebar"] span,
[data-testid="stSidebar"] label {
    color: #7070a0 !important;
    font-family: 'Inter', sans-serif !important;
}

/* Sidebar radio options */
[data-testid="stSidebar"] [data-testid="stRadio"] label {
    color: #7070a0 !important;
    font-size: 0.85rem !important;
}
[data-testid="stSidebar"] [data-testid="stRadio"] > div > label:hover p {
    color: #b0b0d8 !important;
}

/* ─── MAIN CONTENT ────────────────────────────────────── */
.main .block-container {
    padding: 2.5rem 3rem 8rem !important;
    max-width: 850px !important;
}

/* Page titles */
.page-title {
    font-family: 'Space Grotesk', sans-serif;
    font-weight: 700;
    font-size: 2.1rem;
    color: #1a1a2e;
    letter-spacing: -0.03em;
    margin-bottom: 0.2rem;
    line-height: 1.1;
}
.page-sub {
    font-size: 0.7rem;
    color: #b0b0c8;
    letter-spacing: 0.12em;
    text-transform: uppercase;
    margin-bottom: 2rem;
}
.section-label {
    font-size: 0.62rem;
    color: #b8b8d0;
    letter-spacing: 0.15em;
    text-transform: uppercase;
    margin-bottom: 0.6rem;
    font-weight: 600;
}

/* ─── PERSONA / MODE RADIO (main area) ──────────────────
   We style radio as horizontal cards                      */
[data-testid="stRadio"] > label { display: none !important; }
[data-testid="stRadio"] > div[role="radiogroup"] {
    display: flex !important;
    flex-direction: row !important;
    gap: 0.6rem !important;
    flex-wrap: wrap !important;
}
[data-testid="stRadio"] > div[role="radiogroup"] > label {
    flex: 1 1 120px !important;
    background: #ffffff !important;
    border: 1.5px solid #e4e4ee !important;
    border-radius: 14px !important;
    padding: 1rem 0.6rem !important;
    cursor: pointer !important;
    transition: all 0.18s ease !important;
    display: flex !important;
    flex-direction: column !important;
    align-items: center !important;
    justify-content: center !important;
    text-align: center !important;
    min-height: 90px !important;
    box-shadow: 0 1px 4px rgba(0,0,0,0.06) !important;
}
[data-testid="stRadio"] > div[role="radiogroup"] > label:hover {
    border-color: #6366f1 !important;
    background: #f8f8ff !important;
    box-shadow: 0 4px 16px rgba(99,102,241,0.12) !important;
    transform: translateY(-1px) !important;
}
[data-testid="stRadio"] > div[role="radiogroup"] > label:has(input:checked) {
    border-color: #6366f1 !important;
    background: #eef2ff !important;
    box-shadow: 0 4px 20px rgba(99,102,241,0.18) !important;
}
/* Hide radio circle dot */
[data-testid="stRadio"] > div[role="radiogroup"] > label > div:first-child {
    display: none !important;
}
/* Radio label text */
[data-testid="stRadio"] > div[role="radiogroup"] > label > div:last-child p {
    color: #5050a0 !important;
    font-size: 0.8rem !important;
    font-weight: 600 !important;
    font-family: 'Inter', sans-serif !important;
    margin: 0 !important;
    line-height: 1.5 !important;
}
[data-testid="stRadio"] > div[role="radiogroup"] > label:has(input:checked) > div:last-child p {
    color: #3730a3 !important;
}

/* ─── STATUS PILLS ───────────────────────────────────── */
.pill-row {
    display: flex; gap: 0.5rem; flex-wrap: wrap;
    margin: 0.9rem 0 0.5rem;
}
.pill {
    display: inline-flex; align-items: center; gap: 0.3rem;
    background: #eef2ff; border: 1px solid #c7d2fe;
    border-radius: 20px; padding: 0.22rem 0.8rem;
    font-size: 0.65rem; color: #4f46e5;
    font-weight: 500; letter-spacing: 0.03em;
}

/* ─── DIVIDER ────────────────────────────────────────── */
.divider { height: 1px; background: #e4e4ee; margin: 0.5rem 0 1.5rem; }

/* ─── CHAT MESSAGES ──────────────────────────────────── */
[data-testid="stChatMessage"] {
    border-radius: 12px !important;
    margin-bottom: 0.6rem !important;
    padding: 0.75rem 1rem !important;
}
[data-testid="stChatMessage"]:has([data-testid="chatAvatarIcon-user"]) {
    background: #eef2ff !important;
    border: 1px solid #e0e7ff !important;
}
[data-testid="stChatMessage"]:has([data-testid="chatAvatarIcon-assistant"]) {
    background: #ffffff !important;
    border: 1px solid #f0f0f8 !important;
    box-shadow: 0 1px 4px rgba(0,0,0,0.05) !important;
}

/* ─── CHAT INPUT ─────────────────────────────────────── */
[data-testid="stChatInput"] textarea {
    background: #ffffff !important;
    border: 1.5px solid #e0e0f0 !important;
    border-radius: 12px !important;
    color: #1a1a2e !important;
    font-family: 'Inter', sans-serif !important;
    font-size: 0.88rem !important;
    box-shadow: 0 2px 8px rgba(0,0,0,0.05) !important;
}
[data-testid="stChatInput"] textarea:focus {
    border-color: #6366f1 !important;
    box-shadow: 0 0 0 3px rgba(99,102,241,0.1), 0 2px 8px rgba(0,0,0,0.05) !important;
}
[data-testid="stChatInput"] textarea::placeholder { color: #c8c8e0 !important; }
[data-testid="stChatInputSubmitButton"] svg { fill: #6366f1 !important; }

/* ─── MAIN BUTTONS (clear etc.) ──────────────────────── */
.main .stButton > button {
    background: #ffffff !important;
    border: 1.5px solid #e0e0f0 !important;
    border-radius: 8px !important;
    color: #8080b0 !important;
    font-family: 'Inter', sans-serif !important;
    font-size: 0.75rem !important;
    font-weight: 500 !important;
    padding: 0.35rem 1rem !important;
    transition: all 0.15s !important;
    box-shadow: none !important;
}
.main .stButton > button:hover {
    border-color: #6366f1 !important;
    color: #4f46e5 !important;
}

/* ─── SELECTBOX (sidebar model picker) ───────────────── */
[data-testid="stSidebar"] .stSelectbox > div > div {
    background: #252440 !important;
    border: 1px solid #363560 !important;
    border-radius: 8px !important;
    color: #a0a0d0 !important;
    font-family: 'Inter', sans-serif !important;
    font-size: 0.82rem !important;
}

/* ─── SIDEBAR BUTTON ─────────────────────────────────── */
[data-testid="stSidebar"] .stButton > button {
    background: #252440 !important;
    border: 1px solid #363560 !important;
    border-radius: 8px !important;
    color: #6060a0 !important;
    font-family: 'Inter', sans-serif !important;
    font-size: 0.75rem !important;
    width: 100% !important;
    padding: 0.45rem !important;
    box-shadow: none !important;
    transition: all 0.15s !important;
}
[data-testid="stSidebar"] .stButton > button:hover {
    border-color: #6366f1 !important;
    color: #a5b4fc !important;
}

/* Sidebar info box */
[data-testid="stSidebar"] .stAlert {
    background: #1e1d38 !important;
    border: 1px solid #2e2d55 !important;
    border-radius: 8px !important;
    font-size: 0.72rem !important;
}
[data-testid="stSidebar"] .stAlert p { color: #5a5a90 !important; }

/* Spinner */
.stSpinner > div { border-top-color: #6366f1 !important; }

/* Empty hint */
.empty-hint {
    text-align: center;
    padding: 4rem 0 2rem;
    color: #c8c8e0;
    font-size: 0.82rem;
    font-family: 'Inter', sans-serif;
}
</style>
""", unsafe_allow_html=True)

# ── SIDEBAR ───────────────────────────────────────────────────────────────────
with st.sidebar:
    # Brand
    st.markdown("""
    <div style="margin-bottom:0.2rem">
        <span style="font-family:'Space Grotesk',sans-serif;font-weight:700;font-size:1.1rem;color:#e8e8f8;letter-spacing:-0.02em;">⚡ Multi-Aura Hub</span>
    </div>
    <div style="font-size:0.6rem;color:#2e2e50;letter-spacing:0.15em;text-transform:uppercase;margin-bottom:2rem;">AI Workspace</div>
    <div style="font-size:0.6rem;color:#2e2e50;letter-spacing:0.15em;text-transform:uppercase;margin-bottom:0.5rem;">Navigation</div>
    """, unsafe_allow_html=True)

    page = st.radio(
        "nav",
        ["🤖  Multi-Model Chat", "✨  Aura Chat", "🎬  Movie Extractor"],
        label_visibility="collapsed"
    )

    st.markdown("""
    <div style="height:1px;background:#22223a;margin:1.5rem 0;"></div>
    <div style="font-size:0.58rem;color:#22223a;letter-spacing:0.1em;text-transform:uppercase;">v1.0 · LangChain</div>
    """, unsafe_allow_html=True)

# ── ROUTING ───────────────────────────────────────────────────────────────────
if "Multi-Model" in page:
    from chatModels import Multimodel_Chatbot
    Multimodel_Chatbot.show()
elif "Aura" in page:
    from chatModels import UI_ChatBot
    UI_ChatBot.show()
elif "Movie" in page:
    from TrexInfo import UICore1
    UICore1.show()