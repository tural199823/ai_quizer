from backend.whisper_utils import transcribe_youtube_video
from backend.supabase_codes import save_to_supabase, get_transcript_data  
# from backend.chat_ollama import generate_quiz
from backend.chat_groq import generate_quiz_groq


if __name__ == "__main__":
    # transcript = transcribe_youtube_video("https://www.youtube.com/watch?v=SZorAJ4I-sA")
    # save_to_supabase(transcript)
    filename = "The Art of Doing Anything Exceptionally1 Well ( even if you are not pro ).wav"
    data = get_transcript_data(filename)

    print(data)
    # print(data)
