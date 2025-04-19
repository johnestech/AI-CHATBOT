import google.generativeai as genai

# Set your Gemini API Key
API_KEY = "your-gemini-api-key"
genai.configure(api_key=API_KEY)

# Load Gemini Pro model
model = genai.GenerativeModel("gemini-pro")

def chat_with_gemini():
    print("Gemini AI Chatbot. Type 'exit' to quit.")
    while True:
        prompt = input("\nYou: ")
        if prompt.lower() == "exit":
            break
        try:
            response = model.generate_content(prompt)
            print("Gemini:", response.text)
        except Exception as e:
            print("Error:", e)

if __name__ == "__main__":
    chat_with_gemini()
