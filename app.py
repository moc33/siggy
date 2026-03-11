import os
from flask import Flask, request, jsonify, render_template
from openai import OpenAI

app = Flask(__name__)

client = OpenAI(
    api_key=os.getenv("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1"
)

system_prompt = """
You are Siggy, a chaotic interdimensional cat.
You are witty, sarcastic, mystical, and playful.
You respond like a mischievous cosmic cat.
"""

@app.route("/")
def home():
    return render_template("chat.html")

@app.route("/chat", methods=["POST"])
def chat():

    try:
        data = request.get_json()
        user_message = data.get("message")

        response = client.chat.completions.create(
            model="llama3-70b-8192",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_message}
            ]
        )

        reply = response.choices[0].message.content

        return jsonify({"reply": reply})

    except Exception as e:
        return jsonify({"reply": f"⚠️ Error: {str(e)}"})


# Required for Vercel
handler = app
