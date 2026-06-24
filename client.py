from groq import Groq

client = Groq(
    api_key="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"
)

chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": "What is coding?"
        }
    ],
    model="llama-3.1-8b-instant"
)

print(chat_completion.choices[0].message.content)