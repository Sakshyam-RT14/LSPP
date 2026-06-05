import json
import os

from dotenv import load_dotenv
from google import genai
from pydantic import BaseModel, ValidationError

# Load environment variables
load_dotenv()


# -----------------------------
# Pydantic Model
# -----------------------------
class PersonInfo(BaseModel):
    name: str
    email: str
    date: str


# -----------------------------
# Gemini Client
# -----------------------------
client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


# -----------------------------
# LLM Function
# -----------------------------
def call_llm(prompt, retries=3):
    for attempt in range(retries):
        try:
            response = client.models.generate_content(
                model="gemini-2.5-flash",
                contents=prompt,
                config={
                    "response_mime_type": "application/json"
                }
            )

            text = response.text.strip()

            print(f"\nAttempt {attempt + 1}")
            print("Raw Response:")
            print(text)

            # Convert JSON string to dictionary
            data = json.loads(text)

            # Validate with Pydantic
            validated_data = PersonInfo(**data)

            return validated_data

        except json.JSONDecodeError as e:
            print("JSON Decode Error:", e)

        except ValidationError as e:
            print("Validation Error:")
            print(e)

        except Exception as e:
            print("Unexpected Error:")
            print(e)

    raise ValueError(
        "Failed to obtain valid JSON after all retries."
    )


# -----------------------------
# Sample Text
# -----------------------------
paragraph = """
John Smith attended the meeting on June 5, 2026.
His email is john.smith@gmail.com.
"""


# -----------------------------
# Prompt
# -----------------------------
prompt = f"""
Extract the person's information.

Return ONLY valid JSON.

Required format:

{{
    "name": "string",
    "email": "string",
    "date": "YYYY-MM-DD"
}}

Text:
{paragraph}
"""


# -----------------------------
# Run
# -----------------------------
try:
    result = call_llm(prompt)

    print("\nValidated Output:")
    print(result)

    print("\nFields:")
    print("Name :", result.name)
    print("Email:", result.email)
    print("Date :", result.date)

except Exception as e:
    print("\nFinal Error:")
    print(e)