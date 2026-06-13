from dotenv import load_dotenv
import os 
from google import genai

load_dotenv()

class chatbot:
    def __init__(self):
        self.history = []
        self.memory = []
        self.client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

    def memory_classifier(prompt):
        memory_classification = client.models.generate_content(
            model = "gemini-2.5-flash-lite",
            config = {
                "response_mime_type":"applications/json"
            },
            contents =f"""
            You are a memory classifier which decides whether to keep the info in the knowledge base or not based on your knowledge 

            use json and json Only to store the necessary information

            example:
            
                {{
    "personal": [
        "Name is Sakshyam",
        "19 years old"
    ],

    "education": [
        "Studies Computer Engineering",
        "Learning Numerical Methods"
    ],

    "technology": [
        "Uses Arch Linux",
        "Favorite language is Python"
    ],

    "projects": [
        "Building a knowledge base chatbot"
    ]
}}
 """
        
        )
        memory_data = memory_classification.text.strip()
        with open("knowledgebase.txt","a") as file:
            file.write(str(memory_data))