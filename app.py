import streamlit as st

# ─── Page Config ────────────────────────────────────────────────────────────────
st.set_page_config(page_title="AI Portfolio Hub", page_icon="🚀", layout="wide")

# ─── CSS ────────────────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Syne:wght@700;800&family=DM+Sans:wght@400;500&display=swap');

/* ── Base ── */
html, body, [data-testid="stAppViewContainer"] {
    background: #0d0d14 !important;
    color: #f1f0ff;
    font-family: 'DM Sans', sans-serif;
}
#MainMenu, footer { visibility: hidden; }

/* ════════════ SIDEBAR ════════════ */
[data-testid="stSidebar"] {
    background: #11111c !important;
    border-right: 1px solid rgba(124,58,237,0.25) !important;
}

/* Rainbow top stripe */
[data-testid="stSidebar"]::before {
    content: '';
    display: block;
    height: 3px;
    background: linear-gradient(90deg, #7c3aed, #ec4899, #06b6d4);
    width: 100%;
}

/* ── Brand title — reduce top gap ── */
[data-testid="stSidebar"] h1 {
    font-family: 'Syne', sans-serif !important;
    font-size: 1.1rem !important;
    font-weight: 800 !important;
    background: linear-gradient(135deg, #a855f7, #ec4899);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    margin-top: 0.6rem !important;
    margin-bottom: 0.4rem !important;
    padding-top: 0 !important;
    line-height: 1.2 !important;
}

/* ── Model Settings & other sidebar headings — reduce gap ── */
[data-testid="stSidebar"] h2,
[data-testid="stSidebar"] h3,
[data-testid="stSidebar"] .stMarkdown h2,
[data-testid="stSidebar"] .stMarkdown h3 {
    margin-top: 0.5rem !important;
    margin-bottom: 0.25rem !important;
    padding-top: 0 !important;
    line-height: 1.2 !important;
}

/* ════════════ NAV ITEMS ════════════ */

/* Hide the auto-generated radio label */
[data-testid="stSidebar"] .stRadio > label {
    display: none !important;
}

/* Radio wrapper */
[data-testid="stSidebar"] .stRadio > div {
    display: flex !important;
    flex-direction: column !important;
    gap: 2px !important;
}

/* Every nav row — ALL items get identical pill styling */
[data-testid="stSidebar"] .stRadio > div > label {
    display: flex !important;
    flex-direction: row !important;
    align-items: center !important;
    width: 100% !important;
    box-sizing: border-box !important;
    padding: 11px 14px !important;
    border-radius: 10px !important;
    border: 1px solid transparent !important;
    background: transparent !important;
    color: #8b8aab !important;
    font-size: 0.88rem !important;
    font-weight: 400 !important;
    font-family: 'DM Sans', sans-serif !important;
    cursor: pointer !important;
    transition: all 0.18s ease !important;
    white-space: nowrap !important;
    text-transform: none !important;
    text-decoration: none !important;
    line-height: 1.4 !important;
    min-height: 42px !important;
    /* Kill ANY underline/border-bottom Streamlit might add */
    border-bottom: 1px solid transparent !important;
    outline: none !important;
}

/* Kill any p/span inside label that could add underlines */
[data-testid="stSidebar"] .stRadio > div > label p,
[data-testid="stSidebar"] .stRadio > div > label span {
    text-decoration: none !important;
    border-bottom: none !important;
    margin: 0 !important;
    padding: 0 !important;
    font-size: inherit !important;
    color: inherit !important;
    font-weight: inherit !important;
}

/* Hover — all items same */
[data-testid="stSidebar"] .stRadio > div > label:hover {
    background: #1e1e32 !important;
    border-color: rgba(124,58,237,0.35) !important;
    color: #f1f0ff !important;
}

/* Active / selected — all items same pill */
[data-testid="stSidebar"] .stRadio > div > label:has(input[type="radio"]:checked) {
    background: linear-gradient(135deg, rgba(124,58,237,0.32), rgba(168,85,247,0.16)) !important;
    border-color: #7c3aed !important;
    color: #f1f0ff !important;
    font-weight: 600 !important;
    box-shadow: 0 0 0 0.5px rgba(124,58,237,0.5),
                0 2px 14px rgba(124,58,237,0.22) !important;
}

/* Hide native radio dot for ALL items */
[data-testid="stSidebar"] .stRadio > div > label input[type="radio"] {
    display: none !important;
    width: 0 !important;
    height: 0 !important;
}
[data-testid="stSidebar"] .stRadio > div > label > div:first-child {
    display: none !important;
    width: 0 !important;
}

/* ════════════ TOGGLE BUTTONS ════════════ */

/* Collapse button inside open sidebar */
[data-testid="stSidebarCollapseButton"] > button {
    background: rgba(124,58,237,0.15) !important;
    border: 1px solid rgba(124,58,237,0.3) !important;
    border-radius: 8px !important;
    color: #a855f7 !important;
}
[data-testid="stSidebarCollapseButton"] > button:hover {
    background: rgba(124,58,237,0.3) !important;
    color: #fff !important;
}

/* Reopen button when sidebar is CLOSED — always visible, glowing */
[data-testid="collapsedControl"] {
    display:         flex !important;
    visibility:      visible !important;
    opacity:         1 !important;
    pointer-events:  auto !important;
    position:        fixed !important;
    top:             16px !important;
    left:            16px !important;
    z-index:         999999 !important;
    width:           40px !important;
    height:          40px !important;
    align-items:     center !important;
    justify-content: center !important;
    background:      linear-gradient(135deg, #7c3aed, #a855f7) !important;
    border-radius:   10px !important;
    border:          none !important;
    box-shadow:      0 0 0 1px rgba(168,85,247,0.5),
                     0 4px 20px rgba(124,58,237,0.6) !important;
    cursor:          pointer !important;
    transition:      transform 0.2s ease, box-shadow 0.2s ease !important;
}
[data-testid="collapsedControl"]:hover {
    transform:  scale(1.1) !important;
    box-shadow: 0 0 0 2px rgba(168,85,247,0.7),
                0 6px 28px rgba(124,58,237,0.8) !important;
}
[data-testid="collapsedControl"] svg,
[data-testid="collapsedControl"] svg path {
    fill:   #fff !important;
    stroke: #fff !important;
    color:  #fff !important;
}

/* ════════════ MISC ════════════ */
[data-testid="stSidebar"] ::-webkit-scrollbar { width: 3px; }
[data-testid="stSidebar"] ::-webkit-scrollbar-thumb {
    background: #7c3aed;
    border-radius: 99px;
}
[data-testid="stSidebar"] hr {
    border-color: rgba(124,58,237,0.2) !important;
    margin: 4px 0 !important;
}

/* ════════════ MAIN CONTENT ════════════ */
.main .block-container {
    padding: 2rem 2.5rem !important;
    max-width: 100% !important;
}
@media (max-width: 768px) {
    .main .block-container { padding: 1rem !important; }
}
</style>
""", unsafe_allow_html=True)

# ─── Sidebar ────────────────────────────────────────────────────────────────────
st.sidebar.title("🚀 My AI Portfolio")

NAV_ITEMS = {
    "🤖  Multi-Model Chatbot":  "Multi-Model Chatbot",
    "⚡  Aura Chat (Single)":   "Aura Chat (Single)",
    "🎬  Movie Data Extractor": "Movie Data Extractor",
}

selection = st.sidebar.radio(
    label="Navigation",
    options=list(NAV_ITEMS.keys()),
    label_visibility="collapsed"
)

st.sidebar.markdown("---")
st.sidebar.markdown(
    '<div style="font-size:0.65rem;color:#8b8aab;text-align:center;padding:4px 0;">'
    '✦ AI Portfolio &nbsp;·&nbsp; v1.0'
    '</div>',
    unsafe_allow_html=True
)

# ─── Page routing ────────────────────────────────────────────────────────────────
page = NAV_ITEMS[selection]

if page == "Multi-Model Chatbot":
    from chatModels import Multimodel_Chatbot
    Multimodel_Chatbot.show()

elif page == "Aura Chat (Single)":
    from chatModels import UI_ChatBot
    UI_ChatBot.show()

elif page == "Movie Data Extractor":
    from TrexInfo import UICore1
    UICore1.show()