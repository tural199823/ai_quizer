# llm_utils.py

from ollama import chat

def build_prompt(transcript):
    return f"""
You are a helpful assistant that creates educational quizzes based on transcripts. Your goal is to read the following transcript and generate **3 quiz questions** that test the user's understanding of the material.

Instructions:
- Read and understand the transcript.
- Create exactly **5 questions**.
- Vary the format: include at least one **multiple-choice question (MCQ)**, one **fill-in-the-blank**, and one **true/false**.
- Ensure questions are **clearly worded** and relevant to the most important concepts in the transcript.
- Provide the **correct answer** immediately after each question, labeled clearly as **Answer:**.
- If a multiple-choice question is used, give **4 options** (A to D) and mark the correct one.
- Keep language **concise and accurate**.
- Avoid asking trivia; focus on conceptual understanding.

Transcript:
\"\"\"
{transcript}
\"\"\"
"""

def generate_quiz(transcript):
    response = chat(model='gemma3:1b', messages=[
    {
        'role': 'user',
        'content': build_prompt(transcript),
    },
    ])

    return response.message.content
