from google import genai
import os
from dotenv import load_dotenv

load_dotenv()

temp = [0 , 0.3, 0.5, 0.7, 0.9, 1.0]

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

for t in temp:

    response = client.models.generate_content(
        model = "gemini-2.5-flash-lite",
        contents = "What is LLM?",
        config={
            "temperature":t
        }
    )
    print(f"temperature: {t}")
    print(response.text)