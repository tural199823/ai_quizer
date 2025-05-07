from fastapi import FastAPI, Request, Query
from whisper_utils import transcribe_youtube_video
from supabase_codes import save_to_supabase, get_transcript_data  
from chat_ollama import generate_quiz
from chat_groq import generate_quiz_groq
from prompt_text import build_prompt


app = FastAPI()

@app.get("/generate-quiz/")
def generate_quiz_endpoint(url: str = Query(..., description="Youtube video URL")):
    transcript = transcribe_youtube_video(url)
    save_to_supabase(transcript)
    data = get_transcript_data(transcript["filename"])
    quiz = generate_quiz_groq(build_prompt(data["transcript"]))
    return {"quiz": quiz}