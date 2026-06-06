from dotenv import load_dotenv
import os
from google import genai
from pydantic import BaseModel, ValidationError
import json

load_dotenv()

client = genai.Client(api_key = os.getenv("GEMINI_API_KEY"))

prompt = f"""
<instruction>
Write a professional email to a client asking if we could do a meeting
</instruction>

<context>
Do not use emojis
Do not use bullet points
Do not sound casual 
Do not use exclamation marks
</context>

<input>
the client is interested in making a bussiness deal with us 
and we would like a 1 hour meeting scheduled next week

the clients company name is "AVISTA" write a random name title and contact info on your own
</input>
"""

response = client.models.generate_content(
        model = "gemini-2.5-flash",
        contents = prompt
       
    )
print("EMAIL\n")
print(response.text)
