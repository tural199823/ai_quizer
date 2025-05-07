from groq import Groq
import os
from dotenv import load_dotenv
from pathlib import Path
from prompt_text import build_prompt

def generate_quiz_groq(transcript: str) -> str:
    env_path = Path(r"C:\Users\tural\ai_quizer\backend\.env").parent / ".env"

    load_dotenv(dotenv_path=env_path)

    client = Groq(
        api_key=os.getenv("GROQ_API_KEY"),
        )

    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": build_prompt(transcript),
            }
        ],
        model="llama-3.3-70b-versatile",
        )
    return chat_completion.choices[0].message.content