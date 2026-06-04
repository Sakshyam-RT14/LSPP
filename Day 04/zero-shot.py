from google import genai
import os
from dotenv import load_dotenv

load_dotenv()

client = genai.Client(api_key = os.getenv("GEMINI_API_KEY"))

prompt = f"""

clasify the customer feedback as positive/negative/zero

give only one word answer: positive  , negative or zero

feedback: "The product was nice i love it"


"""

response = client.models.generate_content(
    model = "gemini-2.5-flash",
    contents = prompt
)

print(response.text)