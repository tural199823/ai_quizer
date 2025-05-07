from backend.whisper_utils import transcribe_youtube_video
from backend.supabase_codes import save_to_supabase, get_transcript_data  
from backend.chat_ollama import generate_quiz
from backend.chat_groq import generate_quiz_groq
from backend.prompt_text import build_prompt

if __name__ == "__main__":
    transcript = transcribe_youtube_video("https://www.youtube.com/watch?v=TUIAVnvujOo")
    save_to_supabase(transcript)
    data = get_transcript_data(transcript["filename"])
    print(generate_quiz_groq(build_prompt(data["transcript"])))
