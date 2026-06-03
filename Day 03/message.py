messages = []

messages.append({
    "role": "system",
    "content": "You are a helpful tutor."
})

messages.append({
    "role": "user",
    "content": "What is Python?"
})

messages.append({
    "role": "assistant",
    "content": "Python is a programming language."
})

messages.append({
    "role": "user",
    "content": "Who created it?"
})

messages.append({
    "role": "assistant",
    "content": "Python was created by Guido van Rossum."
})

for message in messages:
    print(message)