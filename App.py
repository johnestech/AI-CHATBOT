import os
import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Set up Streamlit page
st.set_page_config(page_title="Gemini Chatbot - DSN Jos", layout="centered")
st.title("💬 Gemini Chatbot - DSN Jos")

# Initialize chat session
if "chat" not in st.session_state:
    model = genai.GenerativeModel("gemini-pro")
    st.session_state.chat = model.start_chat(history=[
        {
            "role": "system",
            "parts": [
                "You are a friendly, helpful AI assistant for the company 'DSN Jos'. "
                "You assist users by answering questions about DSN Jos, its services, and general information. "
                "You always reply clearly, professionally, and in a conversational tone."
            ]
        }
    ])
    st.session_state.history = []  # To store (user, ai) messages for display

# User input
user_input = st.chat_input("Type your message...")

if user_input:
    # Store and display user input
    st.session_state.history.append(("You", user_input))

    try:
        response = st.session_state.chat.send_message(user_input)
        ai_reply = response.text
    except Exception as e:
        ai_reply = f"Error: {e}"

    # Store and display AI response
    st.session_state.history.append(("Gemini", ai_reply))

# Display chat history
for speaker, msg in st.session_state.history:
    st.markdown(f"**{speaker}:** {msg}")
