from flask import Flask, request, jsonify
import json

app = Flask(__name__)

data = {
    "college_name": "Atharva College",
    "courses": ["EXTC", "IT", "CS"],
    "fees_extc": "₹1,20,000 per year",
    "principal": "Dr. ABC",
    "location": "Malad, Mumbai"
}

def get_answer(question):
    q = question.lower()

    if "course" in q:
        return f"We offer: {', '.join(data['courses'])}"
    elif "fees" in q:
        return f"EXTC fees is {data['fees_extc']}"
    elif "principal" in q:
        return f"Principal is {data['principal']}"
    elif "location" in q:
        return f"Located at {data['location']}"
    else:
        return "Ask college-related questions only."

@app.route("/chat", methods=["POST"])
def chat():
    msg = request.json.get("message")
    return jsonify({"reply": get_answer(msg)})

app.run(host="0.0.0.0", port=5000)
