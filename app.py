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
    background: #0c0c10 !important;
    font-family: 'DM Mono', monospace;
    color: #c0c0d0;
}

/* ── Always show sidebar, hide collapse toggle ── */
[data-testid="stSidebar"] {
    display: block !important;
    min-width: 220px !important;
    max-width: 240px !important;
}
section[data-testid="stSidebarCollapsedControl"] { display: none !important; }
[data-testid="collapsedControl"] { display: none !important; }
button[kind="header"] { display: none !important; }

[data-testid="stHeader"], header { background: transparent !important; }
[data-testid="stToolbar"], #MainMenu, footer { display: none !important; }

/* ── SIDEBAR ── */
[data-testid="stSidebar"] {
    background: #0f0f14 !important;
    border-right: 1px solid #18181f !important;
}
[data-testid="stSidebar"] > div:first-child {
    padding: 2rem 1.3rem 1.5rem;
}

/* Brand */
.sb-brand {
    font-family: 'Syne', sans-serif;
    font-weight: 800;
    font-size: 1.05rem;
    letter-spacing: -0.02em;
    color: #d8d8e8;
    margin-bottom: 0.25rem;
}
.sb-tag {
    font-size: 0.58rem;
    color: #28283a;
    letter-spacing: 0.16em;
    text-transform: uppercase;
    margin-bottom: 2rem;
}

/* Nav label */
.sb-nav-label {
    font-size: 0.56rem;
    color: #28283a;
    letter-spacing: 0.18em;
    text-transform: uppercase;
    margin-bottom: 0.5rem;
    font-family: 'DM Mono', monospace;
}

/* Radio nav items */
div[data-testid="stRadio"] > label { display: none !important; }
div[data-testid="stRadio"] > div {
    display: flex !important;
    flex-direction: column !important;
    gap: 0.25rem !important;
}
div[data-testid="stRadio"] > div > label {
    display: flex !important;
    align-items: center !important;
    border-radius: 8px !important;
    padding: 0.55rem 0.85rem !important;
    border: 1px solid transparent !important;
    background: transparent !important;
    transition: all 0.18s ease !important;
    cursor: pointer !important;
}
div[data-testid="stRadio"] > div > label:hover {
    background: #141418 !important;
    border-color: #1e1e28 !important;
}
div[data-testid="stRadio"] > div > label:has(input:checked) {
    background: #1a1828 !important;
    border-color: #30285a !important;
}
div[data-testid="stRadio"] > div > label > div:first-child { display: none !important; }
div[data-testid="stRadio"] > div > label > div > p {
    font-family: 'DM Mono', monospace !important;
    font-size: 0.75rem !important;
    color: #404058 !important;
    margin: 0 !important;
}
div[data-testid="stRadio"] > div > label:has(input:checked) > div > p {
    color: #9090c0 !important;
}

.sb-divider { height: 1px; background: #14141a; margin: 1.5rem 0; }

.sb-footer {
    font-size: 0.56rem;
    color: #202028;
    letter-spacing: 0.1em;
    text-transform: uppercase;
    margin-top: 1.5rem;
    font-family: 'DM Mono', monospace;
}
</style>
""", unsafe_allow_html=True)

# ── SIDEBAR ───────────────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown('<div class="sb-brand">⚡ Multi-Aura Hub</div>', unsafe_allow_html=True)
    st.markdown('<div class="sb-tag">AI Workspace</div>', unsafe_allow_html=True)
    st.markdown('<div class="sb-nav-label">Navigation</div>', unsafe_allow_html=True)

    page = st.radio(
        label="nav",
        options=["⬡  Multi-Model Chat", "◈  Aura Chat", "▣  Movie Extractor"],
        label_visibility="collapsed"
    )

    st.markdown('<div class="sb-divider"></div>', unsafe_allow_html=True)
    st.markdown('<div class="sb-footer">v1.0 · Powered by LangChain</div>', unsafe_allow_html=True)

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