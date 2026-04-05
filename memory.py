import json
import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def get_memory_file(user_id):
    return f"memory_{user_id}.json"

def load_memory(user_id):
    file = get_memory_file(user_id)

    if os.path.exists(file):
        with open(file, "r") as f:
            return json.load(f)

    return [
        {"role": "system", "content": "You are a helpful, friendly AI assistant."}
    ]

def save_memory(user_id, messages):
    with open(get_memory_file(user_id), "w") as f:
        json.dump(messages, f, indent=2)

def get_ai_response(user_id, user_input):
    messages = load_memory(user_id)

    messages.append({"role": "user", "content": user_input})

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=messages,
        temperature=0.7
    )

    reply = response.choices[0].message.content

    messages.append({"role": "assistant", "content": reply})
    save_memory(user_id, messages)

    return reply
