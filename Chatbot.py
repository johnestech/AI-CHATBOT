import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Load Gemini Pro model with a predefined system message
model = genai.GenerativeModel("gemini-pro")

# Create a chat session with context
chat = model.start_chat(history=[
    {
        "role": "system",
        "parts": [
            "You are a helpful and professional AI chatbot for the company 'DSN Jos'. "
            "You assist users by answering questions, providing information, and representing the values and mission of DSN Jos. "
            "Always be friendly, knowledgeable, and professional in your responses."
        ]
    }
])

def chat_with_gemini():
    print("Gemini AI Chatbot for DSN Jos. Type 'exit' to quit.")
    while True:
        prompt = input("\nYou: ")
        if prompt.lower() == "exit":
            break
        try:
            response = chat.send_message(prompt)
            print("Gemini:", response.text)
        except Exception as e:
            print("Error:", e)

if __name__ == "__main__":
    chat_with_gemini()
