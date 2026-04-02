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

st.set_page_config(page_title="Multi-Aura Hub", page_icon="⚡", layout="wide")

# ── GLOBAL CSS ────────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Syne:wght@600;700;800&family=DM+Mono:wght@300;400;500&display=swap');

html, body, [data-testid="stAppViewContainer"] {
    background: #0e0e11 !important;
    font-family: 'DM Mono', monospace;
    color: #c9c9d3;
}

[data-testid="stAppViewContainer"] {
    background: #0e0e11 !important;
}

[data-testid="stHeader"], header { background: transparent !important; }
[data-testid="stToolbar"], #MainMenu, footer { display: none !important; }

/* ── SIDEBAR ── */
[data-testid="stSidebar"] {
    background: #111116 !important;
    border-right: 1px solid rgba(255,255,255,0.06) !important;
}

[data-testid="stSidebar"] > div:first-child {
    padding: 2rem 1.2rem;
}

/* Sidebar title */
.sidebar-brand {
    font-family: 'Syne', sans-serif;
    font-weight: 800;
    font-size: 1.15rem;
    letter-spacing: -0.02em;
    color: #e8e8f0;
    margin-bottom: 0.3rem;
    display: flex;
    align-items: center;
    gap: 0.5rem;
}
.sidebar-tagline {
    font-size: 0.62rem;
    color: #454552;
    letter-spacing: 0.14em;
    text-transform: uppercase;
    margin-bottom: 2rem;
}

/* Radio nav */
div[data-testid="stRadio"] > label { display: none !important; }
div[data-testid="stRadio"] > div {
    display: flex !important;
    flex-direction: column !important;
    gap: 0.3rem !important;
}
div[data-testid="stRadio"] > div > label {
    display: flex !important;
    align-items: center !important;
    border-radius: 8px !important;
    padding: 0.6rem 0.9rem !important;
    border: 1px solid transparent !important;
    background: transparent !important;
    transition: all 0.18s ease !important;
    cursor: pointer !important;
}
div[data-testid="stRadio"] > div > label:hover {
    background: rgba(255,255,255,0.04) !important;
    border-color: rgba(255,255,255,0.07) !important;
}
div[data-testid="stRadio"] > div > label:has(input:checked) {
    background: rgba(180,170,255,0.08) !important;
    border-color: rgba(180,170,255,0.22) !important;
}
div[data-testid="stRadio"] > div > label > div:first-child { display: none !important; }
div[data-testid="stRadio"] > div > label > div > p {
    font-family: 'DM Mono', monospace !important;
    font-size: 0.78rem !important;
    color: #8888a0 !important;
    margin: 0 !important;
}
div[data-testid="stRadio"] > div > label:has(input:checked) > div > p {
    color: #c8c4f8 !important;
}

/* Sidebar divider */
.sidebar-divider {
    height: 1px;
    background: rgba(255,255,255,0.05);
    margin: 1.5rem 0;
}

/* Sidebar footer */
.sidebar-footer {
    font-size: 0.58rem;
    color: #333340;
    letter-spacing: 0.1em;
    text-transform: uppercase;
    margin-top: 2rem;
}
</style>
""", unsafe_allow_html=True)

# ── SIDEBAR ───────────────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown('<div class="sidebar-brand">⚡ Multi-Aura Hub</div>', unsafe_allow_html=True)
    st.markdown('<div class="sidebar-tagline">AI Workspace</div>', unsafe_allow_html=True)

    page = st.radio(
        label="nav",
        options=["⬡  Multi-Model Chat", "◈  Aura Chat", "▣  Movie Extractor"],
        label_visibility="collapsed"
    )

    st.markdown('<div class="sidebar-divider"></div>', unsafe_allow_html=True)
    st.markdown('<div class="sidebar-footer">v1.0 · Powered by LangChain</div>', unsafe_allow_html=True)

# ── ROUTING ───────────────────────────────────────────────────────────────────
if "Multi-Model" in page:
    from chatModels import Multimodel_Chatbot
    Multimodel_Chatbot.show()

elif "Aura Chat" in page:
    from chatModels import UI_ChatBot
    UI_ChatBot.show()

elif "Movie" in page:
    from TrexInfo import UICore1
    UICore1.show()