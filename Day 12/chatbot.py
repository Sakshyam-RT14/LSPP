from dotenv import load_dotenv
import os 
from google import genai
import json
import sqlite3


load_dotenv()
MAX_HISTORY = 4

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
  "content": "<memory_to_store>"
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
       memory_data = json.loads(memory_classification.text.strip())

       if memory_data["store"]:
        save_memory(
            memory_data["category"],
            memory_data["content"]
        )
        

    def save_memory(category,context):
        conn = sqlite.connect("kancha_memory.db")
        cursor = conn.cursor()

        cursor.execute("""
        INSERT OR IGNORE INTO memories(category,content) VALUES(?,?)
        
        """,(category,context))

        conn.commit()
        conn.close()
    
    
    
    
    
    def history_manager(self):
        if len(self.history)>MAX_HISTORY:
            self.history = self.history[2:]
        with open("history.txt","w") as file:
            json.dump(self.history,file, indent = 4)


    def add_history(self,prompt,response):
        self.history.append(
            {
                "role":"user",
                "parts":[{"text":prompt}]
            }
        )

        self.history.append({
            "role":"model",
            "parts":[{"text":response}]
        })
        self.history_manager()

    def clear_history(self):
        self.history.clear()
        print("The history is cleared")

    def generate_response(self,prompt):
        self.memory_classifier(prompt)
        with open("knowledgebase.txt", "r", encoding="utf-8") as f:
            knowledge = f.read()

        with open("history.txt", "r", encoding="utf-8") as f:
            full_history = f.read()

        

        response = self.client.models.generate_content(
            model = "gemini-3.1-flash-lite",
            contents = f""" user question {prompt} 
             Knowledge base: {knowledge} and 
             History: {full_history} 
            """
        )
        data =  response.text.strip()
        print(data)
        self.add_history(prompt,data)


bot = chatbot()

print("What do you want to perform")
print("/generate")
print("/clear")
print("/exit")

while True:
    user_input = input("\nYou: ")
    if user_input == "/exit":
        print("Goodbye.")
        break
    elif user_input == "/clear":
        bot.clear_history()
    elif user_input == "/generate":
        user_text = input("\nHi! Kanchha here, How can i help you:\n")
        try:
            bot.generate_response(user_text)
        except Exception as e:
            print(f"Generation Error: {e}"
)
    else:
        print("Unknown command.")