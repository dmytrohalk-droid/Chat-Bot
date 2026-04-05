from flask import Flask, render_template, request, jsonify, session
from memory import get_ai_response
import uuid

app = Flask(__name__)
app.secret_key = "super_secret_key_change_this"

@app.route("/")
def home():
    # assign unique user ID
    if "user_id" not in session:
        session["user_id"] = str(uuid.uuid4())

    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json["message"]
    user_id = session["user_id"]

    reply = get_ai_response(user_id, user_input)

    return jsonify({"reply": reply})

if __name__ == "__main__":
    app.run(debug=True)
