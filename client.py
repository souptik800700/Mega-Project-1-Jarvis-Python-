from groq import Groq

client = Groq(
    api_key="<apna api key dalo>"
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