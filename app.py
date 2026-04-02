import streamlit as st

# Setup the Sidebar Navigation
st.sidebar.title("🚀 My AI Portfolio")
page = st.sidebar.radio("Go to:", ["Multi-Model Chatbot", "Aura Chat (Single)", "Movie Data Extractor"])

if page == "Multi-Model Chatbot":
    import chatModels.Multimodel_Chatbot as multi
    # Note: You might need to wrap your files in a 'main()' function to call them here
elif page == "Aura Chat (Single)":
    import chatModels.UI_ChatBot as aura
elif page == "Movie Data Extractor":
    import TrexInfo.UICore1 as extractor