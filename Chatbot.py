import os
import google.generativeai as genai
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Set generation configuration
generation_config = {
    "temperature": 1,
    "top_p": 0.92,
    "top_k": 64,
    "max_output_tokens": 8192,
    "response_mime_type": "text/plain",
}

# Initialize model
model = genai.GenerativeModel(
    model_name="gemini-2.0-flash",
    generation_config=generation_config,
)


chat = model.start_chat()


chat.send_message(
    "You are a helpful and professional AI chatbot for the company 'DSN Jos'. "
    "You assist users by answering questions, providing information, and representing the values and mission of DSN Jos. "
    "Always be friendly, knowledgeable, and professional in your responses."
)

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
    try:
        chat_with_gemini()
    except KeyboardInterrupt:
        print("\nGoodbye!")
