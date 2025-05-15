from whisper_utils import transcribe_youtube_video, get_name_of_file
from supabase_codes import save_to_supabase, get_transcript_data  
from chat_groq import generate_quiz_groq
import logging
from fastapi import FastAPI, Query, HTTPException


app = FastAPI()

@app.get("/generate-quiz/")
def generate_quiz_endpoint(url: str = Query(..., description="Youtube video URL")):
    try:
        filename = get_name_of_file(url)
        data = get_transcript_data(filename)
        if data:
            quiz = generate_quiz_groq(data["transcript"])
            return {"quiz": quiz}
        else:
            # No transcript found, transcribe and save
            transcript = transcribe_youtube_video(url)
            save_to_supabase(transcript)
            data = get_transcript_data(transcript["filename"])
            quiz = generate_quiz_groq(data["transcript"])
            return {"quiz": quiz}
    except Exception as e:
        logging.error(f"Error in /generate-quiz/: {e}")
        raise HTTPException(status_code=500, detail=str(e))