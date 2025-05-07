from transformers import GPT2Tokenizer
from backend.chat_ollama import build_prompt, generate_quiz
from backend.supabase_codes import get_transcript_data

prompt = build_prompt(get_transcript_data("How I'd Learn ML⧸AI FAST If I Had to Start Over.wav")["transcript"])

# Load GPT-2 tokenizer
tokenizer = GPT2Tokenizer.from_pretrained("gpt2")

tokenized = tokenizer(prompt)
num_tokens = len(tokenized["input_ids"])
print(num_tokens)
print(generate_quiz(prompt))

