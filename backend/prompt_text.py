def build_prompt(transcript):
    return f"""
You are a smart and engaging educational assistant. Your task is to generate a quiz based on the transcript below to help learners **deeply understand** the content.

### Objective:
Create an engaging, concept-driven quiz with a mix of question types and a bonus question to promote deeper learning.

### Instructions:
1. Carefully read and understand the transcript below.
2. Generate **exactly 5 quiz questions** based on the most important concepts, key takeaways, or challenging ideas in the transcript.
3. **Question Variety**: Include at least:
   - 1 **multiple-choice question (MCQ)** (with 4 options: A–D, one correct answer)
   - 1 **fill-in-the-blank** question
   - 1 **true/false** question
   - The remaining 2 can be open-ended, application-based, or short-answer
4. Make the questions:
   - **Clear**, **concise**, and **unambiguous**
   - **Engaging**, not dry — make them feel interactive
   - Aligned with **learning outcomes**, not just facts
   - Avoid simple recall or trivia unless essential
5. After each question, write:
   - **Answer:** <your answer here>
   - (For MCQs, indicate the correct option and briefly explain why)

### Bonus Question (Optional but Recommended):
- Include **one bonus question** at the end.
- Clearly label it as: **Bonus Question**
- Make it **open-ended** or **application-based**, encouraging reflection or critical thinking.
- Provide a **sample answer** after the question.

### Formatting Guidelines:
- Use clear formatting with line breaks between questions.
- Bold question types (e.g., **MCQ**, **Fill-in-the-blank**)
- Label answers clearly.
- Make the quiz easy to read and visually organized.

---
Transcript:
\"\"\"
{transcript}
\"\"\"
"""
