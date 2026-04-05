import tkinter as tk
import pyttsx3
from memory import get_ai_response

engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def send_message():
    user_input = entry.get()
    if not user_input:
        return

    chat_box.insert(tk.END, "You: " + user_input + "\n")

    reply = get_ai_response(user_input)

    chat_box.insert(tk.END, "Bot: " + reply + "\n\n")

    speak(reply)

    entry.delete(0, tk.END)

# UI Setup
window = tk.Tk()
window.title("AI Chatbot")
window.geometry("500x500")

chat_box = tk.Text(window, wrap=tk.WORD)
chat_box.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

entry = tk.Entry(window)
entry.pack(padx=10, pady=5, fill=tk.X)

send_button = tk.Button(window, text="Send", command=send_message)
send_button.pack(pady=5)

window.mainloop()