# import streamlit as st
# # from dotenv import load_dotenv
# from langchain_mistralai import ChatMistralAI
# from langchain_google_genai import ChatGoogleGenerativeAI
# from langchain_groq import ChatGroq
# from langchain_core.messages import HumanMessage, AIMessage, SystemMessage
# # load_dotenv()




# st.title("🌐 Multi-Aura Hub")
# # ── CONFIGURATION ─────────────────────────────────────────────────────────────

# MODELS_CONFIG = {
#     "Mistral (Small)": {"provider": "mistral", "model": "mistral-small-2603"},
#     "Gemini (Flash)": {"provider": "google", "model": "gemini-2.5-flash-lite"},
#     "Llama 3 (Groq)": {"provider": "groq", "model": "llama-3.3-70b-versatile"},
# }

# PERSONAS = {
#     "Funny":      {"icon": "😄", "prompt": "You are a hilarious and witty assistant. Crack jokes and keep things fun."},
#     "Aggressive": {"icon": "🔥", "prompt": "You are an aggressive, blunt assistant. No sugarcoating. Direct and intense."},
#     "Socratic":   {"icon": "🧠", "prompt": "You are a Socratic assistant. Guide users via thoughtful questions and philosophy."},
#     "Creative":   {"icon": "🎨", "prompt": "You are a wildly creative assistant. Use vivid metaphors and poetic language."},
#     "Professional": {"icon": "💼", "prompt": "You are a professional, concise, and formal corporate assistant."}
# }


# @st.cache_resource
# def load_llm(model_option):
#     config = MODELS_CONFIG[model_option]
#     if config["provider"] == "mistral":
#         return ChatMistralAI(model=config["model"], temperature=0.8)
#     elif config["provider"] == "google":
#         return ChatGoogleGenerativeAI(model=config["model"], temperature=0.8)
#     elif config["provider"] == "groq":
#         return ChatGroq(model=config["model"], temperature=0.8)

# def show():
# # Load Environment Variables


   

#     # ── SESSION STATE ─────────────────────────────────────────────────────────────
#     if "messages" not in st.session_state:
#         st.session_state.messages = []
#     if "persona" not in st.session_state:
#         st.session_state.persona = "Funny"

#     # ── MODEL INITIALIZATION ──────────────────────────────────────────────────────


#     # ── SIDEBAR (Model Selection) ─────────────────────────────────────────────────
#     with st.sidebar:
#         st.title("⚙️ Model Settings")
#         selected_model_name = st.selectbox("Switch Brain", list(MODELS_CONFIG.keys()))
#         llm = load_llm(selected_model_name)
        
#         st.divider()
#         if st.button("Clear Conversation", use_container_width=True):
#             st.session_state.messages = []
#             st.rerun()
        
#         st.info(f"Currently using: **{selected_model_name}**\n\nMemory is preserved even if you switch models!")

#     # ── MAIN UI (Persona Selection) ───────────────────────────────────────────────
#     st.markdown(f"""<h1 style='text-align: center; color: #a78bfa;'>🌐 Multi-Aura Hub</h1>""", unsafe_allow_html=True)

#     # Persona Selection using Columns (Simulating your card style)
#     st.write("### Choose Personality")
#     cols = st.columns(len(PERSONAS))
#     for i, (name, info) in enumerate(PERSONAS.items()):
#         with cols[i]:
#             if st.button(f"{info['icon']}\n{name}", use_container_width=True):
#                 st.session_state.persona = name

#     st.markdown(f"**Active Persona:** `{st.session_state.persona}` | **Model:** `{selected_model_name}`")
#     st.divider()

#     # ── CSS (Retaining your beautiful Aura look) ─────────────────────────────────
#     st.markdown("""
#     <style>
#         .stChatMessage { border-radius: 15px; margin-bottom: 10px; }
#         [data-testid="stSidebar"] { background-color: #0d1117; }
#     </style>
#     """, unsafe_allow_html=True)

#     # ── CHAT LOGIC ────────────────────────────────────────────────────────────────
#     # Display existing chat history
#     for message in st.session_state.messages:
#         if isinstance(message, HumanMessage):
#             with st.chat_message("user"):
#                 st.markdown(message.content)
#         elif isinstance(message, AIMessage):
#             with st.chat_message("assistant", avatar="⚡"):
#                 st.markdown(message.content)

#     # User Input
#     if prompt := st.chat_input("Ask anything..."):
#         # Append User Message
#         st.session_state.messages.append(HumanMessage(content=prompt))
#         with st.chat_message("user"):
#             st.markdown(prompt)

#         # Prepare input with current persona + history
#         system_instruction = SystemMessage(content=PERSONAS[st.session_state.persona]["prompt"])
#         full_prompt = [system_instruction] + st.session_state.messages

#         # Generate Response
#         with st.chat_message("assistant", avatar="⚡"):
#             with st.spinner(f"{selected_model_name} is thinking..."):
#                 try:
#                     response = llm.invoke(full_prompt)
#                     st.markdown(response.content)
#                     # Append AI Message
#                     st.session_state.messages.append(AIMessage(content=response.content))
#                 except Exception as e:
#                     st.error(f"Error: {str(e)}")


import streamlit as st
from langchain_mistralai import ChatMistralAI
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage

MODELS_CONFIG = {
    "Mistral · Small":  {"provider": "mistral", "model": "mistral-small-2603"},
    "Gemini · Flash":   {"provider": "google",  "model": "gemini-2.5-flash-lite"},
    "Llama 3 · Groq":   {"provider": "groq",    "model": "llama-3.3-70b-versatile"},
}

PERSONAS = {
    "Funny":        {"icon": "😄", "prompt": "You are a hilarious and witty assistant. Crack jokes and keep things fun."},
    "Aggressive":   {"icon": "🔥", "prompt": "You are an aggressive, blunt assistant. No sugarcoating. Direct and intense."},
    "Socratic":     {"icon": "🧠", "prompt": "You are a Socratic assistant. Guide users via thoughtful questions and philosophy."},
    "Creative":     {"icon": "🎨", "prompt": "You are a wildly creative assistant. Use vivid metaphors and poetic language."},
    "Professional": {"icon": "💼", "prompt": "You are a professional, concise, and formal corporate assistant."},
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
    # ── SESSION STATE ─────────────────────────────────────────────────────────
    if "mm_messages" not in st.session_state:
        st.session_state.mm_messages = []
    if "mm_persona" not in st.session_state:
        st.session_state.mm_persona = "Funny"

    # ── CSS ───────────────────────────────────────────────────────────────────
    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Space+Grotesk:wght@500;600;700&display=swap');

    /* Page background */
    [data-testid="stAppViewContainer"] { background-color: #f5f4f0 !important; }

    /* ── Header ── */
    .mm-page-title {
        font-family: 'Space Grotesk', sans-serif;
        font-weight: 700;
        font-size: 2rem;
        color: #1a1a2e;
        letter-spacing: -0.03em;
        line-height: 1.1;
        margin-bottom: 0.25rem;
    }
    .mm-page-sub {
        font-size: 0.72rem;
        color: #9090a8;
        letter-spacing: 0.1em;
        text-transform: uppercase;
        margin-bottom: 2rem;
    }
    .mm-section-label {
        font-size: 0.65rem;
        color: #a0a0b8;
        letter-spacing: 0.14em;
        text-transform: uppercase;
        margin-bottom: 0.75rem;
        font-family: 'Inter', sans-serif;
        font-weight: 500;
    }

    /* ── Model selector in sidebar ── */
    [data-testid="stSidebar"] .stSelectbox label {
        font-family: 'Inter', sans-serif !important;
        font-size: 0.62rem !important;
        color: #3a3a5a !important;
        letter-spacing: 0.12em !important;
        text-transform: uppercase !important;
        font-weight: 500 !important;
    }
    [data-testid="stSidebar"] .stSelectbox > div > div {
        background: #22223c !important;
        border: 1px solid #30305a !important;
        border-radius: 8px !important;
        color: #a5b4fc !important;
        font-family: 'Inter', sans-serif !important;
        font-size: 0.82rem !important;
    }
    [data-testid="stSidebar"] .stSelectbox > div > div:hover {
        border-color: #6366f1 !important;
    }

    /* ── Sidebar clear button ── */
    [data-testid="stSidebar"] .stButton > button {
        background: #22223c !important;
        border: 1px solid #30305a !important;
        border-radius: 8px !important;
        color: #6060a0 !important;
        font-family: 'Inter', sans-serif !important;
        font-size: 0.72rem !important;
        padding: 0.45rem 1rem !important;
        width: 100% !important;
        transition: all 0.15s !important;
    }
    [data-testid="stSidebar"] .stButton > button:hover {
        border-color: #6366f1 !important;
        color: #a5b4fc !important;
    }

    /* Sidebar info */
    [data-testid="stSidebar"] .stAlert {
        background: #1e1e38 !important;
        border: 1px solid #2a2a48 !important;
        border-radius: 8px !important;
        color: #5050a0 !important;
        font-size: 0.7rem !important;
    }

    /* ── Persona cards — REAL st.button styled as cards ── */
    .persona-col .stButton > button {
        width: 100% !important;
        background: #ffffff !important;
        border: 1.5px solid #e8e8f0 !important;
        border-radius: 14px !important;
        padding: 1.2rem 0.6rem !important;
        transition: all 0.18s ease !important;
        color: #6060a0 !important;
        font-family: 'Inter', sans-serif !important;
        font-size: 0.75rem !important;
        font-weight: 500 !important;
        line-height: 1.6 !important;
        min-height: 110px !important;
        cursor: pointer !important;
        box-shadow: 0 1px 3px rgba(0,0,0,0.06) !important;
    }
    .persona-col .stButton > button:hover {
        border-color: #6366f1 !important;
        background: #fafafe !important;
        color: #4040c0 !important;
        box-shadow: 0 4px 16px rgba(99,102,241,0.12) !important;
        transform: translateY(-2px) !important;
    }

    /* Active persona card */
    .persona-col-active .stButton > button {
        background: #eef2ff !important;
        border: 1.5px solid #6366f1 !important;
        color: #3730a3 !important;
        box-shadow: 0 4px 16px rgba(99,102,241,0.18) !important;
    }

    /* ── Status pills ── */
    .status-row {
        display: flex;
        align-items: center;
        gap: 0.6rem;
        margin: 1rem 0 0.5rem;
        flex-wrap: wrap;
    }
    .pill {
        display: inline-flex;
        align-items: center;
        gap: 0.35rem;
        background: #eef2ff;
        border: 1px solid #c7d2fe;
        border-radius: 20px;
        padding: 0.25rem 0.85rem;
        font-size: 0.65rem;
        color: #4f46e5;
        font-family: 'Inter', sans-serif;
        font-weight: 500;
        letter-spacing: 0.03em;
    }

    /* ── Divider ── */
    .page-divider {
        height: 1px;
        background: #e8e8f0;
        margin: 0.75rem 0 1.5rem;
    }

    /* ── Chat messages ── */
    [data-testid="stChatMessage"] {
        background: transparent !important;
        border: none !important;
    }

    /* User message */
    [data-testid="stChatMessage"]:has([data-testid="chatAvatarIcon-user"]) {
        background: #eef2ff !important;
        border-radius: 12px !important;
        border: 1px solid #e0e7ff !important;
        padding: 0.75rem 1rem !important;
        margin-bottom: 0.5rem !important;
    }

    /* Assistant message */
    [data-testid="stChatMessage"]:has([data-testid="chatAvatarIcon-assistant"]) {
        background: #ffffff !important;
        border-radius: 12px !important;
        border: 1px solid #f0f0f8 !important;
        padding: 0.75rem 1rem !important;
        margin-bottom: 0.5rem !important;
        box-shadow: 0 1px 4px rgba(0,0,0,0.05) !important;
    }

    /* ── Chat input ── */
    [data-testid="stChatInput"] textarea {
        background: #ffffff !important;
        border: 1.5px solid #e0e0f0 !important;
        border-radius: 12px !important;
        color: #1a1a2e !important;
        font-family: 'Inter', sans-serif !important;
        font-size: 0.88rem !important;
        box-shadow: 0 2px 8px rgba(0,0,0,0.06) !important;
    }
    [data-testid="stChatInput"] textarea:focus {
        border-color: #6366f1 !important;
        box-shadow: 0 0 0 3px rgba(99,102,241,0.1) !important;
    }
    [data-testid="stChatInput"] textarea::placeholder { color: #c0c0d8 !important; }
    [data-testid="stChatInputSubmitButton"] svg { fill: #6366f1 !important; }

    /* ── Empty state ── */
    .empty-hint {
        text-align: center;
        padding: 4rem 0 2rem;
        color: #d0d0e0;
        font-size: 0.8rem;
        letter-spacing: 0.06em;
        font-family: 'Inter', sans-serif;
    }

    .stSpinner > div { border-top-color: #6366f1 !important; }
    </style>
    """, unsafe_allow_html=True)

    # ── SIDEBAR CONTROLS ──────────────────────────────────────────────────────
    with st.sidebar:
        st.markdown('<div class="mm-section-label" style="color:#3a3a5a;margin-top:1rem">Model</div>', unsafe_allow_html=True)
        selected_model_name = st.selectbox(
            "model",
            list(MODELS_CONFIG.keys()),
            label_visibility="collapsed"
        )
        llm = load_llm(selected_model_name)
        st.markdown('<div style="height:0.75rem"></div>', unsafe_allow_html=True)
        if st.button("↺  Clear Conversation", key="mm_clear"):
            st.session_state.mm_messages = []
            st.rerun()
        st.markdown('<div style="height:0.5rem"></div>', unsafe_allow_html=True)
        st.info(f"**{selected_model_name}**\n\nMemory persists across model switches.")

    # ── PAGE HEADER ───────────────────────────────────────────────────────────
    st.markdown('<div class="mm-page-title">Multi-Model Chat</div>', unsafe_allow_html=True)
    st.markdown('<div class="mm-page-sub">Switch models mid-conversation · Memory preserved</div>', unsafe_allow_html=True)

    # ── PERSONA CARDS ─────────────────────────────────────────────────────────
    st.markdown('<div class="mm-section-label">Personality</div>', unsafe_allow_html=True)

    cols = st.columns(len(PERSONAS))
    for i, (name, info) in enumerate(PERSONAS.items()):
        with cols[i]:
            is_active = st.session_state.mm_persona == name
            wrap_class = "persona-col-active" if is_active else "persona-col"
            st.markdown(f'<div class="{wrap_class}">', unsafe_allow_html=True)
            if st.button(f"{info['icon']}\n{name}", key=f"mm_persona_{name}", use_container_width=True):
                st.session_state.mm_persona = name
                st.rerun()
            st.markdown('</div>', unsafe_allow_html=True)

    # ── STATUS ────────────────────────────────────────────────────────────────
    current = PERSONAS[st.session_state.mm_persona]
    st.markdown(f"""
    <div class="status-row">
        <span class="pill">{current['icon']} {st.session_state.mm_persona}</span>
        <span class="pill">⬡ {selected_model_name}</span>
    </div>
    <div class="page-divider"></div>
    """, unsafe_allow_html=True)

    # ── CHAT ──────────────────────────────────────────────────────────────────
    if not st.session_state.mm_messages:
        st.markdown(
            f'<div class="empty-hint">{current["icon"]} Ready — send a message to begin</div>',
            unsafe_allow_html=True
        )
    else:
        for message in st.session_state.mm_messages:
            if isinstance(message, HumanMessage):
                with st.chat_message("user"):
                    st.markdown(message.content)
            elif isinstance(message, AIMessage):
                with st.chat_message("assistant", avatar="⚡"):
                    st.markdown(message.content)

    if prompt := st.chat_input("Send a message…"):
        st.session_state.mm_messages.append(HumanMessage(content=prompt))
        with st.chat_message("user"):
            st.markdown(prompt)
        system_msg = SystemMessage(content=PERSONAS[st.session_state.mm_persona]["prompt"])
        full_prompt = [system_msg] + st.session_state.mm_messages
        with st.chat_message("assistant", avatar="⚡"):
            with st.spinner(""):
                try:
                    response = llm.invoke(full_prompt)
                    st.markdown(response.content)
                    st.session_state.mm_messages.append(AIMessage(content=response.content))
                except Exception as e:
                    st.error(f"Error: {str(e)}")