from flask import Flask, request, jsonify
from openai import OpenAI
import os

app = Flask(__name__)

client = OpenAI(
    api_key=os.getenv("OPENROUTER_API_KEY"),
    base_url="https://openrouter.ai/api/v1"
)

system_prompt = """
You are Siggy, a chaotic interdimensional cat.
You are witty, sarcastic, mystical, and funny.
"""

@app.route("/")
def home():
    return "Siggy AI is running"

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json["message"]

    response = client.chat.completions.create(
        model="openai/gpt-4o-mini",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_input}
        ]
    )

    return jsonify({
        "reply": response.choices[0].message.content
    })
