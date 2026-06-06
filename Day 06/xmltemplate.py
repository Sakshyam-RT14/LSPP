import os

from dotenv import load_dotenv
from google import genai

load_dotenv()


def build_prompt(
    role: str,
    instructions: str,
    context: str,
    user_input: str,
    negative_instructions: str
):
  

    return f"""
<role>
{role}
</role>

<instructions>
{instructions}
</instructions>

<context>
{context}
</context>

<negative_instructions>
{negative_instructions}
</negative_instructions>

<input>
{user_input}
</input>
""".strip()


client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


prompt = build_prompt(
    role="Professional business writer",

    instructions="""
Write a professional email requesting a meeting.
""",

    context="""
The client is interested in discussing a potential partnership.
The meeting should be approximately 30 minutes long.
""",

    negative_instructions="""
Do not use emojis.
Do not use exclamation marks.
Do not sound overly casual.
Do not mention pricing.
""",

    user_input="""
We would like to schedule a meeting sometime next week.
"""
)

print("Generated Prompt:\n")
print(prompt)

print("\n" + "=" * 50 + "\n")

try:
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    print("Gemini Response:\n")
    print(response.text)

except Exception as e:
    print("Error:")
    print(e)