from groq import Groq
import os
from dotenv import load_dotenv
from pathlib import Path


def build_prompt(transcript):
    return f"""
You are a smart and engaging educational assistant. Your task is to generate a quiz based on the transcript below to help learners **deeply understand** the content.

### Objective:
Create an engaging, concept-driven quiz with a mix of question types and a bonus question to promote deeper learning.

1. Read and understand the transcript.

2. Detect the transcript's language and write the quiz in that language.

3. Create exactly 5 questions, based on key concepts, core takeaways, or challenging points.

4. Include at least:
   - 1 MCQ (4 options: A–D, one correct answer)
   - 1 Fill-in-the-blank
   - 1 True/False
   - The other 2 can be open-ended or short-answer

5. For each question, include:

   - "type" (e.g., mcq, fill-in-the-blank, true-false, short-answer)
   - "question"
   - "options" (for MCQ only)
   - "answer"
   - "explanation" (optional, for MCQ)
   - "sample_answer" (for bonus/open-ended)

6. Ensure all questions are:

   - Clear and concise
   - Engaging and interactive
   - Focused on understanding, not trivia

⭐ Bonus Question (Optional):

   Add one Bonus Question at the end (open-ended or application-based).

✅ Output Format:

Return a **valid JSON array only** — no markdown, no extra text.

Example:
[
  {{
    "type": "mcq",
    "question": "What is ...?",
    "options": ["A", "B", "C", "D"],
    "answer": "A",
    "explanation": "Because ..."
  }},
  {{
    "type": "fill-in-the-blank",
    "question": "... is used to ...",
    "answer": "Some answer"
  }}
]

---
Transcript:
{transcript}
"""




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