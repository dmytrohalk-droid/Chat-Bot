from flask import Flask, render_template, request, jsonify
from memory import get_ai_response

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user_input = data["message"]

    reply = get_ai_response(user_input)

    return jsonify({"reply": reply})

if __name__ == "__main__":
    app.run(debug=True)