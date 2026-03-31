# from dotenv import load_dotenv
# import os
# load_dotenv()

# import streamlit as st
# from langchain_mistralai import ChatMistralAI
# from langchain_core.messages import HumanMessage, AIMessage, SystemMessage

# # ── Page config ──────────────────────────────────────────────────────────────
# st.set_page_config(
#     page_title="Mistral Chat",
#     page_icon="✦",
#     layout="centered",
# )

# # ── Custom CSS ────────────────────────────────────────────────────────────────
# st.markdown("""
# <style>
# @import url('https://fonts.googleapis.com/css2?family=Syne:wght@400;600;700;800&family=DM+Mono:ital,wght@0,300;0,400;1,300&display=swap');

# /* ── Root & background ── */
# html, body, [data-testid="stAppViewContainer"] {
#     background: #0a0a0f !important;
#     font-family: 'DM Mono', monospace;
# }
# [data-testid="stAppViewContainer"] {
#     background:
#         radial-gradient(ellipse 80% 60% at 50% -10%, rgba(120,80,255,0.18) 0%, transparent 70%),
#         radial-gradient(ellipse 50% 40% at 90% 80%, rgba(255,100,180,0.10) 0%, transparent 60%),
#         #0a0a0f !important;
# }
# [data-testid="stHeader"], header { background: transparent !important; }
# [data-testid="stToolbar"] { display: none; }

# /* ── Main container ── */
# .main .block-container {
#     max-width: 760px;
#     padding: 2.5rem 1.5rem 6rem;
#     margin: auto;
# }

# /* ── Title ── */
# .chat-title {
#     font-family: 'Syne', sans-serif;
#     font-weight: 800;
#     font-size: 2.6rem;
#     letter-spacing: -0.03em;
#     background: linear-gradient(135deg, #e8e0ff 0%, #c084fc 40%, #f472b6 100%);
#     -webkit-background-clip: text;
#     -webkit-text-fill-color: transparent;
#     background-clip: text;
#     margin-bottom: 0.1rem;
#     line-height: 1.1;
# }
# .chat-subtitle {
#     font-family: 'DM Mono', monospace;
#     font-size: 0.72rem;
#     color: #6b7280;
#     letter-spacing: 0.12em;
#     text-transform: uppercase;
#     margin-bottom: 2.2rem;
# }

# /* ── Chat messages ── */
# .msg-wrap {
#     display: flex;
#     flex-direction: column;
#     gap: 0.85rem;
#     margin-bottom: 1.5rem;
# }
# .msg {
#     display: flex;
#     gap: 0.75rem;
#     align-items: flex-start;
#     animation: fadeUp 0.3s ease both;
# }
# @keyframes fadeUp {
#     from { opacity: 0; transform: translateY(10px); }
#     to   { opacity: 1; transform: translateY(0);    }
# }
# .msg.user  { flex-direction: row-reverse; }

# .avatar {
#     width: 32px; height: 32px;
#     border-radius: 8px;
#     display: flex; align-items: center; justify-content: center;
#     font-size: 0.85rem;
#     flex-shrink: 0;
#     font-family: 'Syne', sans-serif;
#     font-weight: 700;
# }
# .avatar.bot  { background: linear-gradient(135deg,#7c3aed,#c026d3); color:#fff; }
# .avatar.user { background: linear-gradient(135deg,#1d4ed8,#0ea5e9); color:#fff; }

# .bubble {
#     max-width: 78%;
#     padding: 0.75rem 1.1rem;
#     border-radius: 14px;
#     font-size: 0.88rem;
#     line-height: 1.65;
#     white-space: pre-wrap;
# }
# .bubble.bot {
#     background: rgba(255,255,255,0.04);
#     border: 1px solid rgba(255,255,255,0.08);
#     color: #d1d5db;
#     border-top-left-radius: 4px;
# }
# .bubble.user {
#     background: linear-gradient(135deg, rgba(124,58,237,0.55), rgba(192,38,211,0.45));
#     border: 1px solid rgba(192,38,211,0.3);
#     color: #f3e8ff;
#     border-top-right-radius: 4px;
# }

# /* ── Divider ── */
# .divider {
#     height: 1px;
#     background: linear-gradient(90deg, transparent, rgba(255,255,255,0.07), transparent);
#     margin: 1.5rem 0;
# }

# /* ── Input area ── */
# [data-testid="stChatInput"] {
#     background: rgba(255,255,255,0.04) !important;
#     border: 1px solid rgba(255,255,255,0.10) !important;
#     border-radius: 14px !important;
#     color: #e5e7eb !important;
#     font-family: 'DM Mono', monospace !important;
#     font-size: 0.88rem !important;
# }
# [data-testid="stChatInput"]:focus-within {
#     border-color: rgba(168,85,247,0.5) !important;
#     box-shadow: 0 0 0 3px rgba(168,85,247,0.12) !important;
# }
# [data-testid="stChatInputSubmitButton"] svg { fill: #a855f7 !important; }

# /* ── Clear button ── */
# .stButton button {
#     background: rgba(255,255,255,0.04);
#     border: 1px solid rgba(255,255,255,0.10);
#     color: #6b7280;
#     font-family: 'DM Mono', monospace;
#     font-size: 0.75rem;
#     letter-spacing: 0.06em;
#     border-radius: 8px;
#     padding: 0.35rem 0.9rem;
#     transition: all 0.2s;
# }
# .stButton button:hover {
#     border-color: rgba(168,85,247,0.4);
#     color: #c084fc;
#     background: rgba(168,85,247,0.08);
# }

# /* hide streamlit branding */
# #MainMenu, footer { visibility: hidden; }
# </style>
# """, unsafe_allow_html=True)


# # ── Model init ────────────────────────────────────────────────────────────────
# @st.cache_resource
# def get_model():
#     return ChatMistralAI(model="mistral-small-2603", temperature=0.9, max_tokens=100)

# model = get_model()


# # ── Session state ─────────────────────────────────────────────────────────────
# if "messages" not in st.session_state:
#     st.session_state.messages = [
#         SystemMessage(content="You are a helpful and funny assistant.")
#     ]


# # ── Header ────────────────────────────────────────────────────────────────────
# st.markdown('<div class="chat-title">✦ Mistral Chat</div>', unsafe_allow_html=True)
# st.markdown('<div class="chat-subtitle">mistral-small-2603 · funny & helpful</div>', unsafe_allow_html=True)

# col1, col2 = st.columns([6, 1])
# with col2:
#     if st.button("Clear", key="clear"):
#         st.session_state.messages = [
#             SystemMessage(content="You are a helpful and funny assistant.")
#         ]
#         st.rerun()

# st.markdown('<div class="divider"></div>', unsafe_allow_html=True)


# # ── Render history ────────────────────────────────────────────────────────────
# def render_messages():
#     chat_msgs = [m for m in st.session_state.messages if not isinstance(m, SystemMessage)]
#     if not chat_msgs:
#         st.markdown(
#             '<p style="color:#374151;font-size:0.82rem;text-align:center;'
#             'font-family:\'DM Mono\',monospace;padding:2rem 0;">'
#             '— start a conversation —</p>',
#             unsafe_allow_html=True
#         )
#         return

#     html = '<div class="msg-wrap">'
#     for m in chat_msgs:
#         if isinstance(m, HumanMessage):
#             html += (
#                 f'<div class="msg user">'
#                 f'<div class="avatar user">U</div>'
#                 f'<div class="bubble user">{m.content}</div>'
#                 f'</div>'
#             )
#         elif isinstance(m, AIMessage):
#             html += (
#                 f'<div class="msg bot">'
#                 f'<div class="avatar bot">✦</div>'
#                 f'<div class="bubble bot">{m.content}</div>'
#                 f'</div>'
#             )
#     html += '</div>'
#     st.markdown(html, unsafe_allow_html=True)

# render_messages()


# # ── Input ─────────────────────────────────────────────────────────────────────
# if prompt := st.chat_input("Type a message…"):
#     st.session_state.messages.append(HumanMessage(content=prompt))

#     with st.spinner(""):
#         response = model.invoke(st.session_state.messages)

#     st.session_state.messages.append(AIMessage(content=response.content))
#     st.rerun()




import streamlit as st
from dotenv import load_dotenv
import os

from langchain_mistralai import ChatMistralAI
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage

# Load environment variables
load_dotenv()

# Initialize model
model = ChatMistralAI(model="mistral-small-2603", temperature=0.9, max_tokens=100)

# Streamlit UI
st.set_page_config(page_title="AI Chatbot", page_icon="🤖")
st.title("🤖 AI Chatbot")

# Initialize session state
if "messages" not in st.session_state:
    st.session_state.messages = [
        SystemMessage(content="You are a helpful and funny assistant.")
    ]

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Display chat history
for role, msg in st.session_state.chat_history:
    if role == "user":
        st.chat_message("user").write(msg)
    else:
        st.chat_message("assistant").write(msg)

# User input
user_input = st.chat_input("Type your message...")

if user_input:
    # Exit condition
    if user_input == "0":
        st.stop()

    # Display user message immediately
    st.chat_message("user").write(user_input)

    # Add user message
    st.session_state.messages.append(HumanMessage(content=user_input))
    st.session_state.chat_history.append(("user", user_input))

    # Get response
    response = model.invoke(st.session_state.messages)

    # Add AI response
    st.session_state.messages.append(AIMessage(content=response.content))
    st.session_state.chat_history.append(("assistant", response.content))

    # Display response
    st.chat_message("assistant").write(response.content)
