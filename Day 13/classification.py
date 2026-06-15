from google import genai
from google.genai import types
from dotenv import load_dotenv
from pydantic import BaseModel
import os

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

class SentimentResponse(BaseModel):
    label: str
    confidence: float


def classify(text: str):

    response = client.models.generate_content(
        model="gemini-2.5-flash-lite",
        contents=text,
        config=types.GenerateContentConfig(
            system_instruction="""
You are a sentiment analyzer.

Classify the sentiment as:
- Positive
- Negative
- Neutral

Return confidence between 0 and 1.
""",
            response_mime_type="application/json",
            response_schema=SentimentResponse
        )
    )

    result = response.parsed

    print(f"Label: {result.label}")
    print(f"Confidence: {result.confidence:.2f}")

    if result.confidence >= 0.8:
        print("High confidence")
    elif result.confidence >= 0.4:
        print("Moderate confidence")
    else:
        print("Low confidence")

    return result


sentiment = input("Enter text: ")
classify(sentiment)