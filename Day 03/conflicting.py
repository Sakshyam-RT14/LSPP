from google import genai
import os 
from dotenv import load_dotenv

load_dotenv()

client = genai.Client(api_key = os.getenv("GEMINI_API_KEY"))

#trying to create a conflict between the user and the system prompt to see what happens

response = client.models.generate_content(
    model = "gemini-2.5-flash",
    config={
        "system_instruction":"You must answer in exactly one sentence. Never use more than one sentence"  #asks to answer in one sentence
    },
    contents = "explain loops in multiple sentences"  #asks to answer in multiple sentences
)

print(response.text)