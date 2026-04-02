import streamlit as st
# from dotenv import load_dotenv
from langchain_mistralai import ChatMistralAI
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage
# load_dotenv()



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
# Load Environment Variables


    st.title("🌐 Multi-Aura Hub")
    # ── CONFIGURATION ─────────────────────────────────────────────────────────────

    MODELS_CONFIG = {
        "Mistral (Small)": {"provider": "mistral", "model": "mistral-small-2603"},
        "Gemini (Flash)": {"provider": "google", "model": "gemini-2.5-flash-lite"},
        "Llama 3 (Groq)": {"provider": "groq", "model": "llama-3.3-70b-versatile"},
    }

    PERSONAS = {
        "Funny":      {"icon": "😄", "prompt": "You are a hilarious and witty assistant. Crack jokes and keep things fun."},
        "Aggressive": {"icon": "🔥", "prompt": "You are an aggressive, blunt assistant. No sugarcoating. Direct and intense."},
        "Socratic":   {"icon": "🧠", "prompt": "You are a Socratic assistant. Guide users via thoughtful questions and philosophy."},
        "Creative":   {"icon": "🎨", "prompt": "You are a wildly creative assistant. Use vivid metaphors and poetic language."},
        "Professional": {"icon": "💼", "prompt": "You are a professional, concise, and formal corporate assistant."}
    }

    # ── SESSION STATE ─────────────────────────────────────────────────────────────
    if "messages" not in st.session_state:
        st.session_state.messages = []
    if "persona" not in st.session_state:
        st.session_state.persona = "Funny"

    # ── MODEL INITIALIZATION ──────────────────────────────────────────────────────


    # ── SIDEBAR (Model Selection) ─────────────────────────────────────────────────
    with st.sidebar:
        st.title("⚙️ Model Settings")
        selected_model_name = st.selectbox("Switch Brain", list(MODELS_CONFIG.keys()))
        llm = load_llm(selected_model_name)
        
        st.divider()
        if st.button("Clear Conversation", use_container_width=True):
            st.session_state.messages = []
            st.rerun()
        
        st.info(f"Currently using: **{selected_model_name}**\n\nMemory is preserved even if you switch models!")

    # ── MAIN UI (Persona Selection) ───────────────────────────────────────────────
    st.markdown(f"""<h1 style='text-align: center; color: #a78bfa;'>🌐 Multi-Aura Hub</h1>""", unsafe_allow_html=True)

    # Persona Selection using Columns (Simulating your card style)
    st.write("### Choose Personality")
    cols = st.columns(len(PERSONAS))
    for i, (name, info) in enumerate(PERSONAS.items()):
        with cols[i]:
            if st.button(f"{info['icon']}\n{name}", use_container_width=True):
                st.session_state.persona = name

    st.markdown(f"**Active Persona:** `{st.session_state.persona}` | **Model:** `{selected_model_name}`")
    st.divider()

    # ── CSS (Retaining your beautiful Aura look) ─────────────────────────────────
    st.markdown("""
    <style>
        .stChatMessage { border-radius: 15px; margin-bottom: 10px; }
        [data-testid="stSidebar"] { background-color: #0d1117; }
    </style>
    """, unsafe_allow_html=True)

    # ── CHAT LOGIC ────────────────────────────────────────────────────────────────
    # Display existing chat history
    for message in st.session_state.messages:
        if isinstance(message, HumanMessage):
            with st.chat_message("user"):
                st.markdown(message.content)
        elif isinstance(message, AIMessage):
            with st.chat_message("assistant", avatar="⚡"):
                st.markdown(message.content)

    # User Input
    if prompt := st.chat_input("Ask anything..."):
        # Append User Message
        st.session_state.messages.append(HumanMessage(content=prompt))
        with st.chat_message("user"):
            st.markdown(prompt)

        # Prepare input with current persona + history
        system_instruction = SystemMessage(content=PERSONAS[st.session_state.persona]["prompt"])
        full_prompt = [system_instruction] + st.session_state.messages

        # Generate Response
        with st.chat_message("assistant", avatar="⚡"):
            with st.spinner(f"{selected_model_name} is thinking..."):
                try:
                    response = llm.invoke(full_prompt)
                    st.markdown(response.content)
                    # Append AI Message
                    st.session_state.messages.append(AIMessage(content=response.content))
                except Exception as e:
                    st.error(f"Error: {str(e)}")