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

# ── GLOBAL STYLES ─────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Space+Grotesk:wght@500;600;700&display=swap');

/* Reset & base */
html, body { margin: 0; padding: 0; }

[data-testid="stAppViewContainer"] {
    background-color: #f5f4f0 !important;
    font-family: 'Inter', sans-serif;
}

/* Hide Streamlit chrome */
[data-testid="stHeader"] { background: transparent !important; height: 0 !important; }
[data-testid="stToolbar"], #MainMenu, footer { display: none !important; }

/* ── SIDEBAR ── */
[data-testid="stSidebar"] {
    background-color: #1a1a2e !important;
    border-right: none !important;
    min-width: 230px !important;
}

/* Hide collapse arrow */
[data-testid="stSidebarCollapseButton"],
[data-testid="collapsedControl"],
section[data-testid="stSidebarCollapsedControl"],
button[data-testid="baseButton-header"] {
    display: none !important;
}

[data-testid="stSidebar"] .block-container { padding: 0 !important; }
[data-testid="stSidebar"] > div:first-child { padding: 2rem 1.4rem; }

/* Sidebar brand */
.sb-logo {
    font-family: 'Space Grotesk', sans-serif;
    font-weight: 700;
    font-size: 1.2rem;
    color: #ffffff;
    letter-spacing: -0.02em;
    margin-bottom: 0.2rem;
}
.sb-tagline {
    font-size: 0.65rem;
    color: #4a4a7a;
    letter-spacing: 0.12em;
    text-transform: uppercase;
    margin-bottom: 2rem;
}
.sb-section {
    font-size: 0.6rem;
    color: #3a3a5a;
    letter-spacing: 0.14em;
    text-transform: uppercase;
    margin-bottom: 0.6rem;
    font-family: 'Inter', sans-serif;
}

/* Nav radio */
div[data-testid="stRadio"] > label { display: none !important; }
div[data-testid="stRadio"] > div {
    display: flex !important;
    flex-direction: column !important;
    gap: 0.2rem !important;
}
div[data-testid="stRadio"] > div > label {
    display: flex !important;
    align-items: center !important;
    border-radius: 8px !important;
    padding: 0.6rem 0.9rem !important;
    border: 1px solid transparent !important;
    background: transparent !important;
    transition: all 0.15s ease !important;
    cursor: pointer !important;
}
div[data-testid="stRadio"] > div > label:hover {
    background: rgba(255,255,255,0.06) !important;
}
div[data-testid="stRadio"] > div > label:has(input:checked) {
    background: rgba(99,102,241,0.18) !important;
    border-color: rgba(99,102,241,0.35) !important;
}
div[data-testid="stRadio"] > div > label > div:first-child { display: none !important; }
div[data-testid="stRadio"] > div > label > div > p {
    font-family: 'Inter', sans-serif !important;
    font-size: 0.8rem !important;
    color: #6060a0 !important;
    margin: 0 !important;
}
div[data-testid="stRadio"] > div > label:has(input:checked) > div > p {
    color: #a5b4fc !important;
    font-weight: 500 !important;
}

.sb-divider { height: 1px; background: #22223a; margin: 1.5rem 0; }
.sb-footer {
    font-size: 0.58rem;
    color: #2a2a48;
    letter-spacing: 0.1em;
    text-transform: uppercase;
}

/* ── MAIN CONTENT AREA ── */
.main .block-container {
    padding: 2.5rem 3rem 8rem !important;
    max-width: 900px !important;
    margin: 0 auto !important;
}
</style>
""", unsafe_allow_html=True)

# ── SIDEBAR ───────────────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown('<div class="sb-logo">⚡ Multi-Aura Hub</div>', unsafe_allow_html=True)
    st.markdown('<div class="sb-tagline">AI Workspace</div>', unsafe_allow_html=True)
    st.markdown('<div class="sb-section">Pages</div>', unsafe_allow_html=True)

    page = st.radio(
        label="nav",
        options=[
            "🤖  Multi-Model Chat",
            "✨  Aura Chat",
            "🎬  Movie Extractor",
        ],
        label_visibility="collapsed"
    )

    st.markdown('<div class="sb-divider"></div>', unsafe_allow_html=True)
    st.markdown('<div class="sb-footer">v1.0 · LangChain powered</div>', unsafe_allow_html=True)

# ── PAGE ROUTING ──────────────────────────────────────────────────────────────
if "Multi-Model" in page:
    from chatModels import Multimodel_Chatbot
    Multimodel_Chatbot.show()
elif "Aura" in page:
    from chatModels import UI_ChatBot
    UI_ChatBot.show()
elif "Movie" in page:
    from TrexInfo import UICore1
    UICore1.show()