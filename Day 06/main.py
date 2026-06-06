from dotenv import load_dotenv
import os
from google import genai
from pydantic import BaseModel, ValidationError
import json

load_dotenv()

client = genai.Client(api_key = os.getenv("GEMINI_API_KEY"))

class Candidateinfo(BaseModel):
    name: str
    email: str
    phone: str
    skills: list[str]




resume = """
Steve Smith

Email: goatsmith@gmail.com
Phone: +977-9812345678

Skills:
Python
C++
SQL
Git
"""


prompt = f"""
<role>
You are an expert resume parsing system.
</role>

<instructions>
Extract candidate information from the resume.
Return ONLY valid JSON.
</instructions>

<context>
Extract:
- name
- email
- phone
- skills

Skills must be returned as a JSON array.
</context>

<input>
{resume}
</input>

<output_format>
{{
    "name": "string",
    "email": "string",
    "phone": "string",
    "skills": ["skill1", "skill2"]
}}
</output_format>
"""
try:
    response = client.models.generate_content(
        model = "gemini-2.5-flash",
        contents = prompt,
        config={
            "response_mime_type":"application/json"
        }

    )
    text = response.text.strip()

    data = json.loads(text)

    validated_data = Candidateinfo(**data)

    print("Validated data:\n")

    print(validated_data)

    print("Name:",validated_data.name)
    print("Email:",validated_data.email)
    print("Phone:",validated_data.phone)
    print("Skills:",validated_data.skills)

except ValidationError as e:
    print("ValidationError",e)

except Exception as e:
    print("Unexpected Error",e)

except json.JSONDecodeError as e:
    print("Json decode error",e)




