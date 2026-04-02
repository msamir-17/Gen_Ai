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
    # ── CSS ───────────────────────────────────────────────────────────────────
    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Syne:wght@700;800&family=DM+Mono:wght@300;400;500&display=swap');

    .mm-header {
        margin-bottom: 0.25rem;
    }
    .mm-title {
        font-family: 'Syne', sans-serif;
        font-weight: 800;
        font-size: 1.9rem;
        letter-spacing: -0.03em;
        color: #e8e8f0;
        line-height: 1.1;
    }
    .mm-subtitle {
        font-size: 0.63rem;
        color: #3e3e4f;
        letter-spacing: 0.16em;
        text-transform: uppercase;
        margin-top: 0.2rem;
        margin-bottom: 2rem;
    }

    /* ── Model selector pills ── */
    .model-section-label {
        font-size: 0.6rem;
        color: #3e3e4f;
        letter-spacing: 0.16em;
        text-transform: uppercase;
        margin-bottom: 0.7rem;
    }

    /* Sidebar model selectbox */
    [data-testid="stSidebar"] .stSelectbox label {
        font-family: 'DM Mono', monospace !important;
        font-size: 0.68rem !important;
        color: #555568 !important;
        letter-spacing: 0.1em !important;
        text-transform: uppercase !important;
    }
    [data-testid="stSidebar"] .stSelectbox > div > div {
        background: rgba(255,255,255,0.03) !important;
        border: 1px solid rgba(255,255,255,0.08) !important;
        border-radius: 8px !important;
        color: #c8c4f8 !important;
        font-family: 'DM Mono', monospace !important;
        font-size: 0.78rem !important;
    }

    /* ── Persona cards via columns ── */
    .stButton > button {
        background: rgba(255,255,255,0.03) !important;
        border: 1px solid rgba(255,255,255,0.08) !important;
        border-radius: 10px !important;
        color: #888898 !important;
        font-family: 'DM Mono', monospace !important;
        font-size: 0.72rem !important;
        padding: 0.65rem 0.4rem !important;
        transition: all 0.18s ease !important;
        width: 100% !important;
        line-height: 1.5 !important;
    }
    .stButton > button:hover {
        background: rgba(180,170,255,0.07) !important;
        border-color: rgba(180,170,255,0.22) !important;
        color: #c8c4f8 !important;
    }

    /* Sidebar clear button */
    [data-testid="stSidebar"] .stButton > button {
        font-size: 0.68rem !important;
        padding: 0.45rem 0.8rem !important;
        color: #555568 !important;
    }

    /* ── Status bar ── */
    .status-bar {
        display: flex;
        align-items: center;
        gap: 1rem;
        font-size: 0.63rem;
        color: #3e3e4f;
        letter-spacing: 0.08em;
        margin: 0.9rem 0 0.6rem;
    }
    .status-pill {
        display: inline-flex;
        align-items: center;
        gap: 0.35rem;
        background: rgba(180,170,255,0.07);
        border: 1px solid rgba(180,170,255,0.15);
        border-radius: 20px;
        padding: 0.22rem 0.7rem;
        color: #9e9ac8;
        font-size: 0.63rem;
        letter-spacing: 0.06em;
    }
    .divider-line {
        height: 1px;
        background: linear-gradient(90deg, transparent, rgba(255,255,255,0.05), transparent);
        margin: 0.6rem 0 1.2rem;
    }

    /* ── Chat messages ── */
    [data-testid="stChatMessage"] {
        background: transparent !important;
        border: none !important;
        padding: 0 !important;
    }
    [data-testid="stChatMessage"][data-testid*="user"] {
        background: rgba(255,255,255,0.02) !important;
        border-radius: 10px !important;
        border: 1px solid rgba(255,255,255,0.05) !important;
        padding: 0.75rem 1rem !important;
        margin-bottom: 0.5rem !important;
    }

    /* ── Chat input ── */
    [data-testid="stChatInput"] textarea {
        background: rgba(255,255,255,0.03) !important;
        border: 1px solid rgba(255,255,255,0.09) !important;
        border-radius: 10px !important;
        color: #c9c9d3 !important;
        font-family: 'DM Mono', monospace !important;
        font-size: 0.82rem !important;
    }
    [data-testid="stChatInput"] textarea:focus {
        border-color: rgba(180,170,255,0.35) !important;
        box-shadow: 0 0 0 3px rgba(180,170,255,0.07) !important;
    }
    [data-testid="stChatInputSubmitButton"] svg { fill: #7a76c8 !important; }

    /* Sidebar info box */
    [data-testid="stSidebar"] .stAlert {
        background: rgba(255,255,255,0.02) !important;
        border: 1px solid rgba(255,255,255,0.07) !important;
        border-radius: 8px !important;
        font-size: 0.7rem !important;
        color: #555568 !important;
    }

    .empty-hint {
        text-align: center;
        padding: 3rem 0 2rem;
        color: #2a2a36;
        font-size: 0.75rem;
        letter-spacing: 0.06em;
    }
    </style>
    """, unsafe_allow_html=True)

    # ── SESSION STATE ─────────────────────────────────────────────────────────
    if "messages" not in st.session_state:
        st.session_state.messages = []
    if "persona" not in st.session_state:
        st.session_state.persona = "Funny"

    # ── SIDEBAR ───────────────────────────────────────────────────────────────
    with st.sidebar:
        st.markdown('<div class="model-section-label">Active Brain</div>', unsafe_allow_html=True)
        selected_model_name = st.selectbox(
            "Switch Brain",
            list(MODELS_CONFIG.keys()),
            label_visibility="collapsed"
        )
        llm = load_llm(selected_model_name)

        st.markdown('<div style="height:1rem"></div>', unsafe_allow_html=True)

        if st.button("↺  Clear conversation", use_container_width=True):
            st.session_state.messages = []
            st.rerun()

        st.markdown('<div style="height:0.5rem"></div>', unsafe_allow_html=True)
        st.info(f"**{selected_model_name}**\n\nMemory persists across model switches.")

    # ── HEADER ────────────────────────────────────────────────────────────────
    st.markdown("""
    <div class="mm-header">
        <div class="mm-title">Multi-Model Chat</div>
        <div class="mm-subtitle">Switch models mid-conversation · Memory preserved</div>
    </div>
    """, unsafe_allow_html=True)

    # ── PERSONA SELECTOR ─────────────────────────────────────────────────────
    st.markdown('<div class="model-section-label">Personality</div>', unsafe_allow_html=True)

    cols = st.columns(len(PERSONAS))
    for i, (name, info) in enumerate(PERSONAS.items()):
        with cols[i]:
            label = f"{info['icon']}\n{name}"
            if st.button(label, key=f"persona_{name}"):
                st.session_state.persona = name
                st.rerun()

    # ── STATUS BAR ───────────────────────────────────────────────────────────
    current_persona = PERSONAS[st.session_state.persona]
    st.markdown(f"""
    <div class="status-bar">
        <span class="status-pill">{current_persona['icon']} {st.session_state.persona}</span>
        <span class="status-pill">⬡ {selected_model_name}</span>
    </div>
    <div class="divider-line"></div>
    """, unsafe_allow_html=True)

    # ── CHAT HISTORY ─────────────────────────────────────────────────────────
    if not st.session_state.messages:
        st.markdown(
            f'<div class="empty-hint">{current_persona["icon"]} &nbsp; Ready — send a message to begin</div>',
            unsafe_allow_html=True
        )
    else:
        for message in st.session_state.messages:
            if isinstance(message, HumanMessage):
                with st.chat_message("user"):
                    st.markdown(message.content)
            elif isinstance(message, AIMessage):
                with st.chat_message("assistant", avatar="⚡"):
                    st.markdown(message.content)

    # ── INPUT ─────────────────────────────────────────────────────────────────
    if prompt := st.chat_input("Send a message…"):
        st.session_state.messages.append(HumanMessage(content=prompt))
        with st.chat_message("user"):
            st.markdown(prompt)

        system_instruction = SystemMessage(content=PERSONAS[st.session_state.persona]["prompt"])
        full_prompt = [system_instruction] + st.session_state.messages

        with st.chat_message("assistant", avatar="⚡"):
            with st.spinner(""):
                try:
                    response = llm.invoke(full_prompt)
                    st.markdown(response.content)
                    st.session_state.messages.append(AIMessage(content=response.content))
                except Exception as e:
                    st.error(f"Error: {str(e)}")