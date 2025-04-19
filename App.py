import streamlit as st
import google.generativeai as genai

# Setup Gemini API
genai.configure(api_key="your-gemini-api-key")
model = genai.GenerativeModel("gemini-pro")

st.set_page_config(page_title="Gemini Chatbot", layout="centered")
st.title("Gemini Chatbot")

# Initialize chat history
if "chat" not in st.session_state:
    st.session_state.chat = []

# Input
user_input = st.text_input("You:", key="input")

if user_input:
    # Display user message
    st.session_state.chat.append(("You", user_input))

    # Get Gemini response
    try:
        response = model.generate_content(user_input)
        ai_reply = response.text
    except Exception as e:
        ai_reply = f"Error: {e}"

    # Display AI reply
    st.session_state.chat.append(("Gemini", ai_reply))

# Display chat history
for speaker, msg in st.session_state.chat:
    st.markdown(f"**{speaker}:** {msg}")
