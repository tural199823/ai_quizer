from fastapi import FastAPI, Request, Query
from whisper_utils import transcribe_youtube_video, get_name_of_file
from supabase_codes import save_to_supabase, get_transcript_data  
from chat_groq import generate_quiz_groq


app = FastAPI()

@app.get("/generate-quiz/")
def generate_quiz_endpoint(url: str = Query(..., description="Youtube video URL")):
    """
    Endpoint to generate a quiz from a YouTube video URL by retrieving or transcribing its transcript.
    """
    try:
        filename = get_name_of_file(url)
        data = get_transcript_data(filename)
        if data:
            quiz = generate_quiz_groq(data["transcript"])
            return {"quiz": quiz}
        else:
            pass
    except ValueError as e:
        # If the transcript is not found, transcribe the video and save it to Supabase  
        transcript = transcribe_youtube_video(url)
        save_to_supabase(transcript)
        data = get_transcript_data(transcript["filename"])
        quiz = generate_quiz_groq(data["transcript"])
        return {"quiz": quiz}