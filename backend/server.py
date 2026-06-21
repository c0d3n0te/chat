from fastapi import FastAPI
from pydantic import BaseModel
import openai
import os

# Load your API key (Render/Railway will store it as an environment variable)
openai.api_key = os.getenv("OPENAI_API_KEY")

app = FastAPI()

class Message(BaseModel):
    text: str

@app.post("/chat")
async def chat(message: Message):
    user_input = message.text

    # Send the message to the AI model
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",   # or "gpt-4" if you have access
        messages=[
            {"role": "system", "content": "You are Ellie, a friendly assistant who explains EDS clearly and kindly."},
            {"role": "user", "content": user_input}
        ]
    )

    reply = response["choices"][0]["message"]["content"]
    return {"response": reply}
