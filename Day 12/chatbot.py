from dotenv import load_dotenv
import os 
from google import genai

load_dotenv()

class chatbot:
    def __init__(self):
        self.history = []
        self.memory = []
        self.client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

    def memory_classifier(self,prompt):
        memory_classification = self.client.models.generate_content(
            model = "gemini-3.1-flash-lite",
            config = {
                "response_mime_type":"application/json"
            },
            contents =f"""
            You are a memory classifier for an AI assistant.

Your task is to determine whether the user's message contains information that should be stored in a long-term knowledge base.

Store information only if it is likely to be useful in future conversations.

Examples of information to store:
- Name
- Age
- Occupation
- Education
- Skills
- Preferences
- Favorite things
- Ongoing projects
- Goals
- Software or tools regularly used
- Long-term interests

Do NOT store:
- Greetings
- Small talk
- One-time requests
- Questions
- Temporary statements
- Generic conversation

Return ONLY valid JSON.

If the message contains useful information:

{{
  "store": true,
  "category": "<category>",
  "memory": "<memory_to_store>"
}}

Valid categories:
- personal
- education
- technology
- projects
- preferences
- skills
- goals
- other

If the message should not be stored:

{{
  "store": false
}}

User Message:
{prompt}
 """
        
        )
        memory_data = memory_classification.text.strip()
        with open("knowledgebase.txt","a") as file:
            file.write(str(memory_data))

bot = chatbot()

prompt = ["hi my name is sakshyam"]

bot.memory_classifier(prompt)