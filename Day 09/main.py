from google import genai
from dotenv import load_dotenv
import os

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

test_case= [
    ("I love this product man!","positive"),
    ("The packing was not so good but okay","neutral"),
    ("Amazing product", "positive"),
    ("Terrible support", "negative")
]

correct = 0

for text, expected in test_case:

    prompt = f"""
    Classify the sentiment based on the following labels for the given text 

    labels:
    -positive
    -negative
    -neutral

    answer ONLY one word that is the label nothing more than that should be present

    text:{text}
    """
    
    response = client.models.generate_content(
        model = "gemini-2.0-flash-lite",
        contents = prompt
    )

    prediction = response.text.strip().lower()

    if prediction == expected:
        correct +=1

accuracy = correct / len(test_case)

print(f"Accuracy {accuracy*100}")