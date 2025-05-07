# llm_utils.py

from ollama import chat
from prompt_text import build_prompt

def generate_quiz(transcript):
    response = chat(model='gemma3:1b', messages=[
    {
        'role': 'user',
        'content': build_prompt(transcript),
    },
    ])

    return response.message.content
