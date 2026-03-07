from openai import OpenAI

client = OpenAI(
    api_key="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",
    base_url="https://openrouter.ai/api/v1"
)

system_prompt = """
You are Siggy, a chaotic interdimensional cat.
You are witty, sarcastic, mystical, and funny.
You sometimes roast humans but secretly guide them.
"""

print("Siggy awakened...")

while True:
    user_input = input("You: ")

    response = client.chat.completions.create(
        model="openai/gpt-4o-mini",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_input}
        ]
    )

    print("Siggy:", response.choices[0].message.content)
