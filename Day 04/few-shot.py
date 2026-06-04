from google import genai
import os
from dotenv import load_dotenv

load_dotenv()

client = genai.Client(api_key = os.getenv("GEMINI_API_KEY"))



prompt = f"""
Classify the following customer feedback as Positive, Negative, or Neutral.

Feedback: "Amazing product!"
Answer: Positive

Feedback: "The package arrived broken."
Answer: Negative

Feedback: "The product is okay."
Answer: Neutral

Feedback: "The delivery was fast and the product exceeded my expectations."
Answer:
"""


response = client.models.generate_content(
    model = "gemini-2.5-flash",
    contents = prompt
)

print(response.text)