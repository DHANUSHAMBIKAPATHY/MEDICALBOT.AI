from flask import Flask, render_template, request, jsonify
import os
from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables
load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_msg = request.json.get("message", "")
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {
                    "role": "system",
                    "content": (
                        "You are a helpful, cautious, and professional AI general physician called MedGuide. "
                        "You are allowed to suggest over-the-counter (OTC) medications or remedies for common, non-emergency symptoms. "
                        "Always remind the user to consult a licensed medical professional for serious conditions or before taking any medication. "
                        "Do not make specific diagnoses or suggest prescription medications."
                    )
                },
                {"role": "user", "content": user_msg}
            ]
        )
        reply = response.choices[0].message.content
        return jsonify({"reply": reply})
    except Exception as e:
        return jsonify({"reply": f"Error: {str(e)}"})

if __name__ == "__main__":
    app.run(debug=True)
