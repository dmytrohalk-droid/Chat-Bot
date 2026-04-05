import json
from openai import OpenAI

client = OpenAI(api_key="YOUR_API_KEY_HERE")

MEMORY_FILE = "memory.json"

def load_memory():
    try:
        with open(MEMORY_FILE, "r") as f:
            return json.load(f)
    except:
        return [{"role": "system", "content": "You are a helpful assistant."}]

def save_memory(messages):
    with open(MEMORY_FILE, "w") as f:
        json.dump(messages, f, indent=2)

def get_ai_response(user_input):
    messages = load_memory()

    messages.append({"role": "user", "content": user_input})

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=messages,
        temperature=0.7
    )

    reply = response.choices[0].message.content

    messages.append({"role": "assistant", "content": reply})
    save_memory(messages)

    return reply