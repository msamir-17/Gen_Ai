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
    "😄  Funny":        "You are a hilarious and witty assistant. Crack jokes and keep things fun.",
    "🔥  Aggressive":   "You are an aggressive, blunt assistant. No sugarcoating. Direct and intense.",
    "🧠  Socratic":     "You are a Socratic assistant. Guide users via thoughtful questions and philosophy.",
    "🎨  Creative":     "You are a wildly creative assistant. Use vivid metaphors and poetic language.",
    "💼  Professional": "You are a professional, concise, and formal corporate assistant.",
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
    if "mm_messages" not in st.session_state:
        st.session_state.mm_messages = []
    if "mm_persona" not in st.session_state:
        st.session_state.mm_persona = list(PERSONAS.keys())[0]

    # ── SIDEBAR additions ─────────────────────────────────────────────────────
    with st.sidebar:
        st.markdown("""
        <div style="font-size:0.6rem;color:#2e2e50;letter-spacing:0.15em;
        text-transform:uppercase;margin-bottom:0.5rem;margin-top:0.5rem;">Model</div>
        """, unsafe_allow_html=True)
        selected_model = st.selectbox("model", list(MODELS_CONFIG.keys()), label_visibility="collapsed")
        llm = load_llm(selected_model)

        st.markdown('<div style="height:0.6rem"></div>', unsafe_allow_html=True)
        if st.button("↺  Clear Chat", key="mm_clear"):
            st.session_state.mm_messages = []
            st.rerun()

        st.markdown('<div style="height:0.4rem"></div>', unsafe_allow_html=True)
        st.info(f"**{selected_model}**\n\nMemory persists even when you switch models.")

    # ── PAGE HEADER ───────────────────────────────────────────────────────────
    st.markdown('<p class="page-title">Multi-Model Chat</p>', unsafe_allow_html=True)
    st.markdown('<p class="page-sub">Switch models mid-conversation · Memory preserved</p>', unsafe_allow_html=True)

    # ── PERSONA SELECTOR ─────────────────────────────────────────────────────
    st.markdown('<p class="section-label">Personality</p>', unsafe_allow_html=True)

    persona_keys = list(PERSONAS.keys())
    current_idx = persona_keys.index(st.session_state.mm_persona) if st.session_state.mm_persona in persona_keys else 0

    selected_persona = st.radio(
        "persona",
        persona_keys,
        index=current_idx,
        horizontal=True,
        label_visibility="collapsed",
    )

    if selected_persona != st.session_state.mm_persona:
        st.session_state.mm_persona = selected_persona
        st.rerun()

    # ── STATUS ROW ────────────────────────────────────────────────────────────
    st.markdown(f"""
    <div class="pill-row">
        <span class="pill">{st.session_state.mm_persona}</span>
        <span class="pill">⬡ {selected_model}</span>
    </div>
    <div class="divider"></div>
    """, unsafe_allow_html=True)

    # ── CHAT HISTORY ─────────────────────────────────────────────────────────
    if not st.session_state.mm_messages:
        p_icon = st.session_state.mm_persona.split()[0]
        st.markdown(f'<div class="empty-hint">{p_icon} Ready — send a message to begin</div>', unsafe_allow_html=True)
    else:
        for msg in st.session_state.mm_messages:
            if isinstance(msg, HumanMessage):
                with st.chat_message("user"):
                    st.markdown(msg.content)
            elif isinstance(msg, AIMessage):
                with st.chat_message("assistant", avatar="⚡"):
                    st.markdown(msg.content)

    # ── INPUT ─────────────────────────────────────────────────────────────────
    if prompt := st.chat_input("Send a message…"):
        st.session_state.mm_messages.append(HumanMessage(content=prompt))
        with st.chat_message("user"):
            st.markdown(prompt)

        system_msg = SystemMessage(content=PERSONAS[st.session_state.mm_persona])
        full_prompt = [system_msg] + st.session_state.mm_messages

        with st.chat_message("assistant", avatar="⚡"):
            with st.spinner(""):
                try:
                    response = llm.invoke(full_prompt)
                    st.markdown(response.content)
                    st.session_state.mm_messages.append(AIMessage(content=response.content))
                except Exception as e:
                    st.error(f"Error: {str(e)}")