import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get the API key securely from environment variables
api_key = os.getenv('GOOGLE_API_KEY')

if api_key:
    # Configure the API key
    genai.configure(api_key=api_key)
    print("API key loaded successfully.")
else:
    print("API key not found in .env file!")

# Initialize the model
model = genai.GenerativeModel(model_name='gemini-1.5-pro')

# Streamlit UI
st.title("💬 Gemini 1.5 Pro Chatbot")
st.caption("Built with Streamlit + Gemini API")

# Initialize session state for chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# User input box
user_input = st.text_input("You:", key="input_text")

if user_input:
    # Add user message to history
    st.session_state.chat_history.append(("You", user_input))
    
    # Generate Gemini response
    response = model.generate_content(user_input)
    bot_reply = response.text
    
    # Add bot reply to history
    st.session_state.chat_history.append(("Gemini", bot_reply))

# Display the conversation
for sender, message in st.session_state.chat_history:
    if sender == "You":
        st.markdown(f"{sender}:** {message}")
    else:
        st.markdown(f"**{sender}:** {message}")
