from google import genai
import os 
from dotenv import load_dotenv
import json
import time 

load_dotenv()

client= genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

task = input("Enter a task:")

prompt = [
    task,
    f"You are an expert assistant.\n{task}",
    f"Think step by step.\n{task}",
    f"Give a short answer.\n{task}",
    f"Give a detailed answer.\n{task}"

]

result=[]

for i, prompt in enumerate(prompt , start = 1):
    print("Running prompt",i)

    start = time.time()

    response = client.models.generate_content(
        model = "gemini-2.5-flash",
        contents = prompt
    )

    end = time.time()

    result.append({
        "prompt number": i,
        "prompt": prompt,
        "response":response.text,
        "response_time": round(end-start,2),
        "token-size": len(response.text.split())
    })

with open("result.json","w") as file:
    json.dump(result , file , indent =4)

print("result is saved in the given file")




