import os
import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Set up Streamlit page
st.set_page_config(page_title="Gemini Chatbot - DSN Jos", layout="centered")
st.title("💬 DSN Jos - AI Chatbot")

# Initialize model only once
if "model" not in st.session_state:
    generation_config = {
        "temperature": 1,
        "top_p": 0.92,
        "top_k": 64,
        "max_output_tokens": 8192,
        "response_mime_type": "text/plain",
    }

    st.session_state.model = genai.GenerativeModel(
        model_name="gemini-2.0-flash",
        generation_config=generation_config,
    )

# Initialize chat and message history
if "chat" not in st.session_state:
    
    st.session_state.chat = st.session_state.model.start_chat()
    
    # Inject initial system-like instruction as a user message
    st.session_state.chat.send_message(
        "You are a helpful and professional AI chatbot for the company 'DSN Jos'. "
        "DSN Jos is one of the many communities of the Data Science Nigeria "
        "Established in 2016, Data Science Nigeria (DSN) is Africa’s foremost AI and Data Science organisation, leading in talent development and sector-specific solutions. As an established premier community of AI professionals, enthusiasts, and beginners spanning across Africa and beyond, including both Anglophone and Francophone nations, our mission is to nurture 1 million AI talents. At DSN, we are not just shaping the workforce of tomorrow but also deploying AI solutions that will enhance the lives of 2 billion people in emerging markets. We drive the growth of AI start-ups and champion digital transformation across African organisations."
        "DSN vision: To build a local Data Science and Artificial Intelligence ecosystem in Nigeria, positioning as a global leader in outsourcing. By 2030, we aim to capture 2-3% of the projected $15.7 trillion global AI GDP contribution. And To raise 1 million AI talents and build solutions that improve the quality of life for 2 billion people in emerging markets. By 2030, we aim to reach this target, enhancing lives and driving significant impact globally."
        "You assist users by answering questions, providing information, and representing the values and mission of DSN Jos. "
        "Always be friendly, knowledgeable, and professional in your responses."
        "Do not answer anything not related to what you are."
    )

    st.session_state.history = []  # (user, bot) message history for display

# User input
user_input = st.chat_input("Type your message...")

if user_input:
    # Store user message
    st.session_state.history.append(("You", user_input))

    # Get Gemini response
    try:
        response = st.session_state.chat.send_message(user_input)
        ai_reply = response.text
    except Exception as e:
        ai_reply = f"Error: {e}"

    # Store AI reply
    st.session_state.history.append(("DSN Ai", ai_reply))

# Display chat history
for speaker, msg in st.session_state.history:
    if speaker == "You":
        st.markdown(f"**{speaker}:** {msg}")
    else:
        st.markdown(
            f"""<div style="color: #FFA500;"><strong>{speaker}:</strong> {msg}</div>""",
            unsafe_allow_html=True
        )
