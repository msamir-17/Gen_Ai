import streamlit as st

# 1. Set Page Config ONLY ONCE here in the main file
st.set_page_config(page_title="AI Portfolio Hub", page_icon="🚀", layout="wide")

st.sidebar.title("🚀 My AI Portfolio")
page = st.sidebar.radio("Go to:", ["Multi-Model Chatbot", "Aura Chat (Single)", "Movie Data Extractor"])

if page == "Multi-Model Chatbot":
    from chatModels import Multimodel_Chatbot
    Multimodel_Chatbot.show() # <--- This calls the function inside the file

elif page == "Aura Chat (Single)":
    from chatModels import UI_ChatBot
    UI_ChatBot.show() # <--- This calls the function inside the file

elif page == "Movie Data Extractor":
    from TrexInfo import UICore1
    UICore1.show() # <--- This calls the function inside the file   