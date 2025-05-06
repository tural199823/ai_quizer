from fastapi import FastAPI, Request, Query
from backend.whisper_utils import transcribe_youtube_video
from backend.supabase_codes import save_to_supabase, get_transcript_data  # Note: file is supabase.py not supabase_codes.py
from backend.llm_utils import generate_quiz

if __name__ == "__main__":
    transcript = transcribe_youtube_video("https://www.youtube.com/watch?v=TUIAVnvujOo")
    save_to_supabase(transcript)
    data = get_transcript_data(transcript["filename"])
    print(generate_quiz(data["transcript"]))




# app = FastAPI()

# @app.get("/generate-quiz/")
# def generate_quiz_endpoint(url: str = Query(..., description="Youtube video URL")):
#     transcript = transcribe_youtube_video(url)
#     # print(transcript)
#     try:
#         save_to_supabase(transcript)
#     except Exception as e:
#         print(f"Error saving to Supabase: {e}")
#     # print("did save")
#     # get_transcript_data(transcript["filename"])
#     # print("got data")
#     quiz = generate_quiz(transcript["transcript"])
#     return {"quiz": quiz}