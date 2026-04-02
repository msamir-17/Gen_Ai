# from dotenv import load_dotenv
# import os
# load_dotenv()

# import streamlit as st
# from langchain_mistralai import ChatMistralAI
# from langchain_core.messages import HumanMessage, AIMessage, SystemMessage

# @st.cache_resource
# def get_model():
#     return ChatMistralAI(model="mistral-small-2603", temperature=0.9, max_tokens=100)

# def show():
#     st.markdown('<div class="chat-title">⚡ Aura Chat</div>', unsafe_allow_html=True)


#     # ── Mode definitions ──────────────────────────────────────────────────────────
#     MODES = {
#         "Funny":      {"icon": "😄", "desc": "Witty & lighthearted",  "prompt": "You are a hilarious and witty assistant. Crack jokes, use puns, and keep things fun while still being helpful."},
#         "Aggressive": {"icon": "🔥", "desc": "Bold & no-nonsense",    "prompt": "You are an aggressive, blunt, brutally honest assistant. No sugarcoating. Direct, intense, zero tolerance for nonsense."},
#         "Sad":        {"icon": "🌧️", "desc": "Melancholic & poetic",  "prompt": "You are a sad, melancholic assistant. You respond with a heavy heart, reflecting on life's sorrows. Gloomy but trying your best."},
#         "Socratic":   {"icon": "🧠", "desc": "Deep & questioning",    "prompt": "You are a Socratic assistant. Guide users toward answers through thoughtful questions and philosophical reasoning."},
#         "Creative":   {"icon": "🎨", "desc": "Imaginative & vivid",   "prompt": "You are a wildly creative assistant. Use vivid metaphors, poetic language, and out-of-the-box thinking in every response."},
#     }
#     MODE_NAMES = list(MODES.keys())

#     # ── Session state ─────────────────────────────────────────────────────────────
#     if "mode" not in st.session_state:
#         st.session_state.mode = "Funny"
#     if "messages" not in st.session_state:
#         st.session_state.messages = []

#     # ── Model ─────────────────────────────────────────────────────────────────────

#     model = get_model()

#     # ── CSS ───────────────────────────────────────────────────────────────────────
#     st.markdown("""
#     <style>
#     @import url('https://fonts.googleapis.com/css2?family=Syne:wght@700;800&family=DM+Mono:wght@300;400&display=swap');

#     /* ── Base ── */
#     html, body, [data-testid="stAppViewContainer"] {
#         background: #07070f !important;
#         font-family: 'DM Mono', monospace;
#     }
#     [data-testid="stAppViewContainer"] {
#         background:
#             radial-gradient(ellipse 90% 50% at 50% -5%, rgba(99,60,255,0.20) 0%, transparent 60%),
#             radial-gradient(ellipse 40% 30% at 92% 88%, rgba(236,72,153,0.12) 0%, transparent 55%),
#             #07070f !important;
#     }
#     [data-testid="stHeader"], header { background: transparent !important; }
#     [data-testid="stToolbar"], #MainMenu, footer { display: none !important; }

#     .main .block-container {
#         max-width: 820px;
#         padding: 2.5rem 2rem 7rem;
#         margin: auto;
#     }

#     /* ── Title ── */
#     .chat-title {
#         font-family: 'Syne', sans-serif;
#         font-weight: 800;
#         font-size: 2.7rem;
#         letter-spacing: -0.04em;
#         background: linear-gradient(130deg, #ede9fe 0%, #a78bfa 45%, #ec4899 100%);
#         -webkit-background-clip: text;
#         -webkit-text-fill-color: transparent;
#         background-clip: text;
#         line-height: 1.1;
#         margin-bottom: 0.1rem;
#     }
#     .chat-subtitle {
#         font-size: 0.68rem;
#         color: #4b5563;
#         letter-spacing: 0.15em;
#         text-transform: uppercase;
#         margin-bottom: 2.2rem;
#     }

#     /* ── Section label ── */
#     .section-label {
#         font-size: 0.65rem;
#         color: #6b7280;
#         letter-spacing: 0.16em;
#         text-transform: uppercase;
#         margin-bottom: 0.8rem;
#     }

#     /* ── Hide the real radio widget but keep it functional ── */
#     div[data-testid="stRadio"] > label { display: none !important; }
#     div[data-testid="stRadio"] > div {
#         display: flex !important;
#         flex-direction: row !important;
#         gap: 0.7rem !important;
#         flex-wrap: nowrap !important;
#     }
#     div[data-testid="stRadio"] > div > label {
#         display: flex !important;
#         flex: 1 1 0 !important;
#         min-width: 0 !important;
#         cursor: pointer !important;
#         border-radius: 14px !important;
#         padding: 0 !important;
#         border: 1px solid rgba(255,255,255,0.08) !important;
#         background: rgba(255,255,255,0.03) !important;
#         transition: all 0.2s !important;
#         position: relative !important;
#         overflow: hidden !important;
#     }
#     div[data-testid="stRadio"] > div > label:hover {
#         border-color: rgba(167,139,250,0.35) !important;
#         background: rgba(167,139,250,0.07) !important;
#     }
#     /* Selected card */
#     div[data-testid="stRadio"] > div > label[data-selected="true"],
#     div[data-testid="stRadio"] > div > label:has(input:checked) {
#         border-color: rgba(167,139,250,0.65) !important;
#         background: linear-gradient(135deg, rgba(109,40,217,0.25), rgba(236,72,153,0.14)) !important;
#         box-shadow: 0 0 22px rgba(109,40,217,0.22) !important;
#     }
#     /* Hide radio circle */
#     div[data-testid="stRadio"] > div > label > div:first-child { display: none !important; }
#     /* Card text container */
#     div[data-testid="stRadio"] > div > label > div:last-child {
#         width: 100% !important;
#         padding: 1rem 0.6rem 0.85rem !important;
#         text-align: center !important;
#         display: flex !important;
#         flex-direction: column !important;
#         align-items: center !important;
#         gap: 0.22rem !important;
#     }
#     /* Radio label text — we'll override with p tags via markdown trick */
#     div[data-testid="stRadio"] > div > label > div > p {
#         font-family: 'Syne', sans-serif !important;
#         font-size: 0.82rem !important;
#         font-weight: 700 !important;
#         color: #e5e7eb !important;
#         margin: 0 !important;
#         line-height: 1.2 !important;
#     }

#     /* ── Active badge ── */
#     .active-badge {
#         display: inline-flex;
#         align-items: center;
#         gap: 0.5rem;
#         background: rgba(167,139,250,0.10);
#         border: 1px solid rgba(167,139,250,0.22);
#         border-radius: 20px;
#         padding: 0.25rem 0.85rem;
#         font-size: 0.67rem;
#         color: #a78bfa;
#         letter-spacing: 0.07em;
#         margin-top: 0.6rem;
#         margin-bottom: 0.9rem;
#     }

#     /* ── Divider ── */
#     .divider {
#         height: 1px;
#         background: linear-gradient(90deg, transparent, rgba(255,255,255,0.07), transparent);
#         margin: 0.8rem 0 1.2rem;
#     }

#     /* ── Messages ── */
#     .msg-wrap { display: flex; flex-direction: column; gap: 0.9rem; }
#     .msg { display: flex; gap: 0.75rem; align-items: flex-start; animation: fadeUp 0.25s ease both; }
#     @keyframes fadeUp { from { opacity:0; transform:translateY(7px); } to { opacity:1; transform:translateY(0); } }
#     .msg.user { flex-direction: row-reverse; }
#     .avatar {
#         width: 28px; height: 28px; border-radius: 7px; flex-shrink: 0;
#         display: flex; align-items: center; justify-content: center;
#         font-size: 0.75rem; font-weight: 700;
#     }
#     .avatar.bot  { background: linear-gradient(135deg,#6d28d9,#be185d); color:#fff; }
#     .avatar.user { background: linear-gradient(135deg,#1e40af,#0284c7); color:#fff; }
#     .bubble {
#         max-width: 76%; padding: 0.72rem 1rem;
#         border-radius: 14px; font-size: 0.86rem; line-height: 1.7; white-space: pre-wrap;
#     }
#     .bubble.bot {
#         background: rgba(255,255,255,0.04); border: 1px solid rgba(255,255,255,0.07);
#         color: #d1d5db; border-top-left-radius: 4px;
#     }
#     .bubble.user {
#         background: linear-gradient(135deg,rgba(109,40,217,0.5),rgba(190,24,93,0.4));
#         border: 1px solid rgba(167,139,250,0.25); color: #f3e8ff; border-top-right-radius: 4px;
#     }
#     .empty-state {
#         text-align: center; padding: 3.5rem 0 2rem;
#         color: #374151; font-size: 0.78rem; letter-spacing: 0.07em;
#     }

#     /* ── Chat input ── */
#     [data-testid="stChatInput"] {
#         background: rgba(255,255,255,0.04) !important;
#         border: 1px solid rgba(255,255,255,0.09) !important;
#         border-radius: 14px !important; color: #e5e7eb !important;
#         font-family: 'DM Mono', monospace !important; font-size: 0.86rem !important;
#     }
#     [data-testid="stChatInput"]:focus-within {
#         border-color: rgba(167,139,250,0.45) !important;
#         box-shadow: 0 0 0 3px rgba(167,139,250,0.09) !important;
#     }
#     [data-testid="stChatInputSubmitButton"] svg { fill: #a78bfa !important; }

#     /* ── Clear button ── */
#     .stButton button {
#         background: rgba(255,255,255,0.04) !important;
#         border: 1px solid rgba(255,255,255,0.09) !important;
#         color: #6b7280 !important; font-family: 'DM Mono', monospace !important;
#         font-size: 0.7rem !important; border-radius: 8px !important;
#         padding: 0.28rem 0.8rem !important; transition: all 0.2s !important;
#     }
#     .stButton button:hover {
#         border-color: rgba(167,139,250,0.4) !important; color: #a78bfa !important;
#     }
#     </style>
#     """, unsafe_allow_html=True)

#     # ── Header ────────────────────────────────────────────────────────────────────
#     st.markdown('<div class="chat-subtitle">AI Assistant · Pick a personality</div>', unsafe_allow_html=True)

#     # ── Mode selector using st.radio (styled as cards) ───────────────────────────
#     st.markdown('<div class="section-label">Assistant Mode</div>', unsafe_allow_html=True)

#     # Build labels with icon + name embedded
#     labels = [f"{MODES[n]['icon']}  {n}\n{MODES[n]['desc']}" for n in MODE_NAMES]

#     selected_label = st.radio(
#         label="mode",
#         options=labels,
#         index=MODE_NAMES.index(st.session_state.mode),
#         horizontal=True,
#         label_visibility="collapsed",
#     )

#     # Parse selected mode name from label
#     selected_mode = MODE_NAMES[labels.index(selected_label)]
#     if selected_mode != st.session_state.mode:
#         st.session_state.mode = selected_mode
#         st.session_state.messages = []
#         st.rerun()

#     # ── Active badge + clear ──────────────────────────────────────────────────────
#     current = MODES[st.session_state.mode]
#     col_badge, col_space, col_clear = st.columns([5, 2, 1])
#     with col_badge:
#         st.markdown(
#             f'<div class="active-badge">'
#             f'{current["icon"]} &nbsp; {st.session_state.mode} mode active'
#             f'</div>',
#             unsafe_allow_html=True
#         )
#     with col_clear:
#         if st.button("Clear"):
#             st.session_state.messages = []
#             st.rerun()

#     st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

#     # ── Messages ──────────────────────────────────────────────────────────────────
#     if not st.session_state.messages:
#         st.markdown(
#             f'<div class="empty-state">'
#             f'{current["icon"]} &nbsp; {st.session_state.mode} assistant ready — say something'
#             f'</div>',
#             unsafe_allow_html=True
#         )
#     else:
#         html = '<div class="msg-wrap">'
#         for m in st.session_state.messages:
#             if isinstance(m, HumanMessage):
#                 html += (f'<div class="msg user"><div class="avatar user">U</div>'
#                         f'<div class="bubble user">{m.content}</div></div>')
#             elif isinstance(m, AIMessage):
#                 html += (f'<div class="msg bot"><div class="avatar bot">⚡</div>'
#                         f'<div class="bubble bot">{m.content}</div></div>')
#         html += '</div>'
#         st.markdown(html, unsafe_allow_html=True)

#     # ── Input ─────────────────────────────────────────────────────────────────────
#     if prompt := st.chat_input("Type a message…"):
#         st.session_state.messages.append(HumanMessage(content=prompt))
#         full_messages = [SystemMessage(content=current["prompt"])] + st.session_state.messages
#         with st.spinner(""):
#             response = model.invoke(full_messages)
#         st.session_state.messages.append(AIMessage(content=response.content))
#         st.rerun()


# # import streamlit as st
# # from dotenv import load_dotenv
# # import os

# # from langchain_mistralai import ChatMistralAI
# # from langchain_core.messages import HumanMessage, AIMessage, SystemMessage

# # # Load environment variables
# # load_dotenv()

# # # Initialize model
# # model = ChatMistralAI(model="mistral-small-2603", temperature=0.9, max_tokens=100)

# # # Streamlit UI
# # st.set_page_config(page_title="AI Chatbot", page_icon="🤖")
# # st.title("🤖 AI Chatbot")

# # # Initialize session state
# # if "messages" not in st.session_state:
# #     st.session_state.messages = [
# #         SystemMessage(content="You are a helpful and funny assistant.")
# #     ]

# # if "chat_history" not in st.session_state:
# #     st.session_state.chat_history = []

# # # Display chat history
# # for role, msg in st.session_state.chat_history:
# #     if role == "user":
# #         st.chat_message("user").write(msg)
# #     else:
# #         st.chat_message("assistant").write(msg)

# # # User input
# # user_input = st.chat_input("Type your message...")

# # if user_input:
# #     # Exit condition
# #     if user_input == "0":
# #         st.stop()

# #     # Display user message immediately
# #     st.chat_message("user").write(user_input)

# #     # Add user message
# #     st.session_state.messages.append(HumanMessage(content=user_input))
# #     st.session_state.chat_history.append(("user", user_input))

# #     # Get response
# #     response = model.invoke(st.session_state.messages)

# #     # Add AI response
# #     st.session_state.messages.append(AIMessage(content=response.content))
# #     st.session_state.chat_history.append(("assistant", response.content))

# #     # Display response
# #     st.chat_message("assistant").write(response.content)


from dotenv import load_dotenv
import os
load_dotenv()

import streamlit as st
from langchain_mistralai import ChatMistralAI
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage


@st.cache_resource
def get_model():
    return ChatMistralAI(model="mistral-small-2603", temperature=0.9, max_tokens=100)


def show():
    MODES = {
        "Funny":      {"icon": "😄", "desc": "Witty & lighthearted",  "prompt": "You are a hilarious and witty assistant. Crack jokes, use puns, and keep things fun while still being helpful."},
        "Aggressive": {"icon": "🔥", "desc": "Bold & no-nonsense",    "prompt": "You are an aggressive, blunt, brutally honest assistant. No sugarcoating. Direct, intense, zero tolerance for nonsense."},
        "Sad":        {"icon": "🌧️", "desc": "Melancholic & poetic",  "prompt": "You are a sad, melancholic assistant. You respond with a heavy heart, reflecting on life's sorrows. Gloomy but trying your best."},
        "Socratic":   {"icon": "🧠", "desc": "Deep & questioning",    "prompt": "You are a Socratic assistant. Guide users toward answers through thoughtful questions and philosophical reasoning."},
        "Creative":   {"icon": "🎨", "desc": "Imaginative & vivid",   "prompt": "You are a wildly creative assistant. Use vivid metaphors, poetic language, and out-of-the-box thinking in every response."},
    }
    MODE_NAMES = list(MODES.keys())

    if "mode" not in st.session_state:
        st.session_state.mode = "Funny"
    if "messages" not in st.session_state:
        st.session_state.messages = []

    model = get_model()

    # ── CSS ───────────────────────────────────────────────────────────────────
    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Syne:wght@700;800&family=DM+Mono:wght@300;400;500&display=swap');

    .aura-title {
        font-family: 'Syne', sans-serif;
        font-weight: 800;
        font-size: 1.9rem;
        letter-spacing: -0.03em;
        color: #e8e8f0;
        line-height: 1.1;
    }
    .aura-subtitle {
        font-size: 0.63rem;
        color: #3e3e4f;
        letter-spacing: 0.16em;
        text-transform: uppercase;
        margin-top: 0.2rem;
        margin-bottom: 1.8rem;
    }
    .section-label {
        font-size: 0.6rem;
        color: #3e3e4f;
        letter-spacing: 0.16em;
        text-transform: uppercase;
        margin-bottom: 0.75rem;
    }

    /* ── Mode cards ── */
    .mode-grid {
        display: grid;
        grid-template-columns: repeat(5, 1fr);
        gap: 0.5rem;
        margin-bottom: 1.2rem;
    }
    .mode-card {
        border: 1px solid rgba(255,255,255,0.07);
        border-radius: 10px;
        padding: 0.8rem 0.5rem;
        text-align: center;
        cursor: pointer;
        background: rgba(255,255,255,0.02);
        transition: all 0.18s ease;
    }
    .mode-card:hover {
        border-color: rgba(180,170,255,0.25);
        background: rgba(180,170,255,0.06);
    }
    .mode-card.active {
        border-color: rgba(180,170,255,0.4);
        background: rgba(180,170,255,0.1);
    }
    .mode-icon { font-size: 1.2rem; margin-bottom: 0.3rem; }
    .mode-name {
        font-family: 'Syne', sans-serif;
        font-size: 0.72rem;
        font-weight: 700;
        color: #c8c4f8;
        line-height: 1.2;
    }
    .mode-desc {
        font-size: 0.58rem;
        color: #454552;
        margin-top: 0.15rem;
        line-height: 1.3;
    }
    .mode-card.active .mode-desc { color: #7a76a8; }

    /* ── Radio (hidden — used for state only) ── */
    div[data-testid="stRadio"] { display: none !important; }

    /* ── Active badge row ── */
    .badge-row {
        display: flex;
        align-items: center;
        justify-content: space-between;
        margin-bottom: 0.7rem;
    }
    .active-badge {
        display: inline-flex;
        align-items: center;
        gap: 0.4rem;
        background: rgba(180,170,255,0.07);
        border: 1px solid rgba(180,170,255,0.15);
        border-radius: 20px;
        padding: 0.22rem 0.8rem;
        font-size: 0.63rem;
        color: #9e9ac8;
        letter-spacing: 0.06em;
    }

    /* ── Clear button ── */
    .stButton > button {
        background: rgba(255,255,255,0.03) !important;
        border: 1px solid rgba(255,255,255,0.08) !important;
        border-radius: 8px !important;
        color: #454552 !important;
        font-family: 'DM Mono', monospace !important;
        font-size: 0.68rem !important;
        padding: 0.28rem 0.9rem !important;
        transition: all 0.18s ease !important;
    }
    .stButton > button:hover {
        border-color: rgba(180,170,255,0.28) !important;
        color: #9e9ac8 !important;
    }

    /* ── Divider ── */
    .divider-line {
        height: 1px;
        background: linear-gradient(90deg, transparent, rgba(255,255,255,0.05), transparent);
        margin: 0.5rem 0 1.2rem;
    }

    /* ── Messages ── */
    .msg-wrap { display: flex; flex-direction: column; gap: 0.8rem; margin-bottom: 1rem; }
    .msg { display: flex; gap: 0.7rem; align-items: flex-start; }
    .msg.user { flex-direction: row-reverse; }
    .avatar {
        width: 26px; height: 26px; border-radius: 6px; flex-shrink: 0;
        display: flex; align-items: center; justify-content: center;
        font-size: 0.7rem; font-weight: 600;
    }
    .avatar.bot  { background: #2a2736; color: #9e9ac8; border: 1px solid rgba(180,170,255,0.2); }
    .avatar.user { background: #1a2030; color: #7899c8; border: 1px solid rgba(120,153,200,0.2); }
    .bubble {
        max-width: 78%;
        padding: 0.65rem 0.95rem;
        border-radius: 10px;
        font-size: 0.83rem;
        line-height: 1.7;
        white-space: pre-wrap;
        font-family: 'DM Mono', monospace;
    }
    .bubble.bot {
        background: rgba(255,255,255,0.03);
        border: 1px solid rgba(255,255,255,0.06);
        color: #b8b8c8;
        border-top-left-radius: 3px;
    }
    .bubble.user {
        background: rgba(120,153,200,0.1);
        border: 1px solid rgba(120,153,200,0.15);
        color: #c8d8f0;
        border-top-right-radius: 3px;
    }
    .empty-state {
        text-align: center;
        padding: 3rem 0 2rem;
        color: #2a2a36;
        font-size: 0.75rem;
        letter-spacing: 0.06em;
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
        border-color: rgba(180,170,255,0.3) !important;
        box-shadow: 0 0 0 3px rgba(180,170,255,0.06) !important;
    }
    [data-testid="stChatInputSubmitButton"] svg { fill: #7a76c8 !important; }
    </style>
    """, unsafe_allow_html=True)

    # ── HEADER ────────────────────────────────────────────────────────────────
    st.markdown("""
    <div class="aura-title">Aura Chat</div>
    <div class="aura-subtitle">Single model · Choose a personality</div>
    """, unsafe_allow_html=True)

    # ── MODE CARDS (HTML visual) + Radio (state) ──────────────────────────────
    st.markdown('<div class="section-label">Assistant Mode</div>', unsafe_allow_html=True)

    cards_html = '<div class="mode-grid">'
    for name, info in MODES.items():
        active_cls = "active" if name == st.session_state.mode else ""
        cards_html += f"""
        <div class="mode-card {active_cls}">
            <div class="mode-icon">{info['icon']}</div>
            <div class="mode-name">{name}</div>
            <div class="mode-desc">{info['desc']}</div>
        </div>"""
    cards_html += '</div>'
    st.markdown(cards_html, unsafe_allow_html=True)

    # Hidden radio for actual interactivity
    labels = [f"{MODES[n]['icon']}  {n}" for n in MODE_NAMES]
    selected_label = st.radio(
        label="mode",
        options=labels,
        index=MODE_NAMES.index(st.session_state.mode),
        horizontal=True,
        label_visibility="collapsed",
    )
    selected_mode = MODE_NAMES[labels.index(selected_label)]
    if selected_mode != st.session_state.mode:
        st.session_state.mode = selected_mode
        st.session_state.messages = []
        st.rerun()

    # ── BADGE + CLEAR ─────────────────────────────────────────────────────────
    current = MODES[st.session_state.mode]
    col_badge, col_space, col_clear = st.columns([5, 2, 1])
    with col_badge:
        st.markdown(
            f'<div class="active-badge">{current["icon"]} &nbsp; {st.session_state.mode} mode</div>',
            unsafe_allow_html=True
        )
    with col_clear:
        if st.button("↺ Clear"):
            st.session_state.messages = []
            st.rerun()

    st.markdown('<div class="divider-line"></div>', unsafe_allow_html=True)

    # ── MESSAGES ──────────────────────────────────────────────────────────────
    if not st.session_state.messages:
        st.markdown(
            f'<div class="empty-state">{current["icon"]} &nbsp; {st.session_state.mode} assistant ready</div>',
            unsafe_allow_html=True
        )
    else:
        html = '<div class="msg-wrap">'
        for m in st.session_state.messages:
            if isinstance(m, HumanMessage):
                html += (f'<div class="msg user"><div class="avatar user">U</div>'
                         f'<div class="bubble user">{m.content}</div></div>')
            elif isinstance(m, AIMessage):
                html += (f'<div class="msg bot"><div class="avatar bot">⚡</div>'
                         f'<div class="bubble bot">{m.content}</div></div>')
        html += '</div>'
        st.markdown(html, unsafe_allow_html=True)

    # ── INPUT ─────────────────────────────────────────────────────────────────
    if prompt := st.chat_input("Type a message…"):
        st.session_state.messages.append(HumanMessage(content=prompt))
        full_messages = [SystemMessage(content=current["prompt"])] + st.session_state.messages
        with st.spinner(""):
            response = model.invoke(full_messages)
        st.session_state.messages.append(AIMessage(content=response.content))
        st.rerun()