from google import genai
import os
from dotenv import load_dotenv

load_dotenv()
client = genai.Client(api_key = os.getenv("GEMINI_API_KEY"))
prompt = f"""
convert the given unstructured given text into structured json format

text: I am Chris and i am a software engineer
output:
{{
    "name": "Chris",
    "job":"software engineer"
}}

text:My name is Brijesh and i am a data scientist
output:
{{
    "name": "Brijesh",
    "job":"data scientist"
}}

text: Myself Richard and i work as a cloud engineer
output:
{{
    "name": "Richard",
    "job":"cloud engineer"
}}

text: hi, my name is Gerald i am an AI engineer
output:

"""
response = client.models.generate_content(
    model = "gemini-2.5-flash",
    contents = prompt
)
print(response.text)