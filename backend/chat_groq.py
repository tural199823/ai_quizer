from groq import Groq
import os
from dotenv import load_dotenv
from pathlib import Path


def build_prompt(transcript):
    """Generates a prompt for an AI assistant to create an educational quiz based on a provided transcript.
    The prompt instructs the assistant to:
    - Analyze the transcript and detect its language.
    - Generate exactly 8 questions (4 multiple choice and 4 true/false) focused on key concepts and deep understanding.
    - For each question, include its type, the question text, options (for MCQs), the correct answer, and an explanation.
    - Ensure questions are clear, concise, and engaging.
    - Return the quiz as a valid JSON array, with no extra text or formatting.
    Args:
      transcript (str): The transcript text to base the quiz on.
    Returns:
      str: A formatted prompt string for the AI assistant."""
    
    return f"""
You are a smart and engaging educational assistant. Your task is to generate a quiz based on the transcript below to help learners **deeply understand** the content.

### Objective:
Create an engaging, concept-driven quiz with a mix of question types and a bonus question to promote deeper learning.

1. Read and understand the transcript.

2. Detect the transcript's language and write the quiz in that language.

3. Create exactly 8 questions, based on key concepts, core takeaways, or challenging points.

4. Include at least:
   - 4 multiple choice question (4 options: A–D, one correct answer)
   - 4 True/False
   
5. For each question, include:

   - "type" (e.g., mcq, true-false)
   - "question"
   - "options" (for MCQ only)
   - "answer"
   - "explanation" 

6. Ensure all questions are:

   - Clear and concise
   - Engaging and interactive
   - Focused on understanding, not trivia


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
    "type": "true-false",
    "question": "... is used to ...",
    "answer": "Some answer",
    explanation: "Because ..."
  }}
]

---
Transcript:
{transcript}
"""


def generate_quiz_groq(transcript: str) -> str:
    """
    Generates a quiz based on the provided transcript using the Groq API.
    This function loads environment variables, initializes a Groq client with the API key,
    and sends a prompt (built from the transcript) to the Groq chat completion endpoint.
    It returns the generated quiz content from the API response.
    Args:
      transcript (str): The transcript text to generate quiz questions from.
    Returns:
      str: The generated quiz content as a string.
    """
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