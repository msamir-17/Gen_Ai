import streamlit as st
from langchain_mistralai import ChatMistralAI
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage

# ── CONFIGURATION ──────────────────────────────────────────────────────────────
MODELS_CONFIG = {
    "Mistral (Small)": {"provider": "mistral", "model": "mistral-small-2603"},
    "Gemini (Flash)":  {"provider": "google",  "model": "gemini-2.5-flash-lite"},
    "Llama 3 (Groq)":  {"provider": "groq",    "model": "llama-3.3-70b-versatile"},
}

PERSONAS = {
    "Funny":        {"icon": "😄", "color": "#f59e0b", "prompt": "You are a hilarious and witty assistant. Crack jokes and keep things fun."},
    "Aggressive":   {"icon": "🔥", "color": "#ef4444", "prompt": "You are an aggressive, blunt assistant. No sugarcoating. Direct and intense."},
    "Socratic":     {"icon": "🧠", "color": "#06b6d4", "prompt": "You are a Socratic assistant. Guide users via thoughtful questions and philosophy."},
    "Creative":     {"icon": "🎨", "color": "#a855f7", "prompt": "You are a wildly creative assistant. Use vivid metaphors and poetic language."},
    "Professional": {"icon": "💼", "color": "#10b981", "prompt": "You are a professional, concise, and formal corporate assistant."},
}

@st.cache_resource
def load_llm(model_option):
    config = MODELS_CONFIG[model_option]
    if config["provider"] == "mistral":
        return ChatMistralAI(model=config["model"], temperature=0.8)
    elif config["provider"] == "google":
        return ChatGoogleGenerativeAI(model=config["model"], temperature=0.8)
    elif config["provider"] == "groq":
        return ChatGroq(model=config["model"], temperature=0.8)

def show():
    # ── SESSION STATE ──────────────────────────────────────────────────────────
    if "messages" not in st.session_state:
        st.session_state.messages = []
    if "persona" not in st.session_state:
        st.session_state.persona = "Funny"

    # ── SIDEBAR ────────────────────────────────────────────────────────────────
    with st.sidebar:
        st.markdown("""
        <div style="
            font-size:0.6rem;letter-spacing:0.13em;font-weight:700;
            text-transform:uppercase;color:#8b8aab;
            padding: 4px 0 8px 0;margin-top:8px;">
            ⚙️ Model Settings
        </div>""", unsafe_allow_html=True)

        selected_model_name = st.selectbox(
            "Switch Brain", list(MODELS_CONFIG.keys()),
            label_visibility="visible"
        )
        llm = load_llm(selected_model_name)

        st.markdown("<div style='height:6px'></div>", unsafe_allow_html=True)

        if st.button("🗑️  Clear Conversation", use_container_width=True):
            st.session_state.messages = []
            st.rerun()

        st.markdown(f"""
        <div style="
            margin-top:10px;
            background: rgba(124,58,237,0.12);
            border: 1px solid rgba(124,58,237,0.3);
            border-radius: 10px;
            padding: 10px 12px;
            font-size: 0.78rem;
            color: #a78bfa;
            line-height: 1.6;">
            Currently using: <strong style="color:#c084fc">{selected_model_name}</strong><br>
            <span style="color:#8b8aab;font-size:0.72rem;">
            Memory preserved across model switches.</span>
        </div>""", unsafe_allow_html=True)

    # ── PAGE CSS ───────────────────────────────────────────────────────────────
    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Syne:wght@700;800&family=DM+Sans:wght@400;500&display=swap');

    /* Persona buttons */
    div[data-testid="stHorizontalBlock"] > div > div > div > button {
        background: rgba(255,255,255,0.03) !important;
        border: 1px solid rgba(124,58,237,0.25) !important;
        border-radius: 12px !important;
        color: #c4c3e0 !important;
        font-family: 'DM Sans', sans-serif !important;
        font-size: 0.82rem !important;
        padding: 10px 6px !important;
        transition: all 0.18s ease !important;
        min-height: 58px !important;
    }
    div[data-testid="stHorizontalBlock"] > div > div > div > button:hover {
        background: rgba(124,58,237,0.2) !important;
        border-color: #7c3aed !important;
        color: #fff !important;
        transform: translateY(-1px);
        box-shadow: 0 4px 16px rgba(124,58,237,0.3) !important;
    }

    /* Chat messages */
    [data-testid="stChatMessage"] {
        background: rgba(255,255,255,0.03) !important;
        border: 1px solid rgba(124,58,237,0.12) !important;
        border-radius: 14px !important;
        padding: 12px 16px !important;
        margin-bottom: 8px !important;
    }

    /* User message */
    [data-testid="stChatMessage"]:has([data-testid="chatAvatarIcon-user"]) {
        background: rgba(124,58,237,0.1) !important;
        border-color: rgba(124,58,237,0.25) !important;
    }

    /* Chat input box */
    [data-testid="stChatInput"] textarea {
        background: rgba(255,255,255,0.04) !important;
        border: 1px solid rgba(124,58,237,0.3) !important;
        border-radius: 12px !important;
        color: #f1f0ff !important;
        font-family: 'DM Sans', sans-serif !important;
    }
    [data-testid="stChatInput"] textarea:focus {
        border-color: #7c3aed !important;
        box-shadow: 0 0 0 2px rgba(124,58,237,0.2) !important;
    }

    /* Selectbox */
    [data-testid="stSidebar"] .stSelectbox > div > div {
        background: rgba(255,255,255,0.04) !important;
        border: 1px solid rgba(124,58,237,0.3) !important;
        border-radius: 10px !important;
        color: #f1f0ff !important;
    }

    /* Clear button */
    [data-testid="stSidebar"] .stButton > button {
        background: rgba(239,68,68,0.1) !important;
        border: 1px solid rgba(239,68,68,0.3) !important;
        border-radius: 10px !important;
        color: #fca5a5 !important;
        font-size: 0.82rem !important;
        transition: all 0.18s ease !important;
    }
    [data-testid="stSidebar"] .stButton > button:hover {
        background: rgba(239,68,68,0.22) !important;
        border-color: #ef4444 !important;
        color: #fff !important;
    }

    /* Divider */
    hr { border-color: rgba(124,58,237,0.2) !important; }

    /* Active persona badge */
    .persona-badge {
        display: inline-flex;
        align-items: center;
        gap: 6px;
        background: rgba(124,58,237,0.15);
        border: 1px solid rgba(124,58,237,0.35);
        border-radius: 99px;
        padding: 4px 14px;
        font-size: 0.78rem;
        color: #c084fc;
        font-family: 'DM Sans', sans-serif;
        margin-right: 8px;
    }
    .model-badge {
        display: inline-flex;
        align-items: center;
        gap: 6px;
        background: rgba(6,182,212,0.1);
        border: 1px solid rgba(6,182,212,0.3);
        border-radius: 99px;
        padding: 4px 14px;
        font-size: 0.78rem;
        color: #67e8f9;
        font-family: 'DM Sans', sans-serif;
    }
    </style>
    """, unsafe_allow_html=True)

    # ── HEADER ─────────────────────────────────────────────────────────────────
    st.markdown("""
    <div style="padding: 8px 0 4px 0;">
        <div style="
            font-family: 'Syne', sans-serif;
            font-size: 2rem;
            font-weight: 800;
            background: linear-gradient(135deg, #a855f7, #ec4899, #06b6d4);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            line-height: 1.2;
            margin-bottom: 4px;">
            🌐 Multi-Aura Hub
        </div>
        <div style="color:#8b8aab; font-size:0.82rem; letter-spacing:0.04em;">
            Switch models on the fly · Personas stay in memory
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<div style='height:6px'></div>", unsafe_allow_html=True)

    # ── PERSONA SELECTOR ───────────────────────────────────────────────────────
    st.markdown("""
    <div style="font-size:0.6rem;font-weight:700;letter-spacing:0.13em;
                text-transform:uppercase;color:#8b8aab;margin-bottom:8px;">
        Choose Personality
    </div>""", unsafe_allow_html=True)

    cols = st.columns(len(PERSONAS))
    for i, (name, info) in enumerate(PERSONAS.items()):
        with cols[i]:
            if st.button(f"{info['icon']}\n{name}", use_container_width=True, key=f"persona_{name}"):
                st.session_state.persona = name

    # ── ACTIVE STATUS BAR ──────────────────────────────────────────────────────
    active = PERSONAS[st.session_state.persona]
    st.markdown(f"""
    <div style="margin: 12px 0 4px 0; display:flex; align-items:center; gap:8px; flex-wrap:wrap;">
        <span class="persona-badge">{active['icon']} {st.session_state.persona}</span>
        <span class="model-badge">🤖 {selected_model_name}</span>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<hr style='margin:10px 0 14px 0;'>", unsafe_allow_html=True)

    # ── CHAT HISTORY ───────────────────────────────────────────────────────────
    if not st.session_state.messages:
        st.markdown(f"""
        <div style="
            text-align:center; padding: 48px 0;
            color:#8b8aab; font-size:0.9rem; font-family:'DM Sans',sans-serif;">
            {active['icon']} <span style="color:#6b6a8a;">
            {st.session_state.persona} mode ready — say something</span>
        </div>""", unsafe_allow_html=True)

    for message in st.session_state.messages:
        if isinstance(message, HumanMessage):
            with st.chat_message("user"):
                st.markdown(message.content)
        elif isinstance(message, AIMessage):
            with st.chat_message("assistant", avatar=active["icon"]):
                st.markdown(message.content)

    # ── CHAT INPUT ─────────────────────────────────────────────────────────────
    if prompt := st.chat_input(f"Ask {st.session_state.persona.lower()} {active['icon']}..."):
        st.session_state.messages.append(HumanMessage(content=prompt))
        with st.chat_message("user"):
            st.markdown(prompt)

        system_instruction = SystemMessage(content=PERSONAS[st.session_state.persona]["prompt"])
        full_prompt = [system_instruction] + st.session_state.messages

        with st.chat_message("assistant", avatar=active["icon"]):
            with st.spinner(f"{selected_model_name} thinking..."):
                try:
                    response = llm.invoke(full_prompt)
                    st.markdown(response.content)
                    st.session_state.messages.append(AIMessage(content=response.content))
                except Exception as e:
                    st.error(f"⚠️ {str(e)}")