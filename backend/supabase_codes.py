# supabase_utils.py
from supabase import create_client, Client
from dotenv import load_dotenv
from pathlib import Path
import os

def get_supabase_client() -> Client:
    env_path = Path(r"C:\Users\tural\ai_quizer\backend\.env").parent / ".env"
    load_dotenv(dotenv_path=env_path)

    url = os.getenv("SUPABASE_URL")
    key = os.getenv("SUPABASE_KEY")

    if not url or not key:
        raise ValueError("Supabase URL or Key is missing in the .env file")

    return create_client(url, key)

def save_to_supabase(data: dict) -> None:
    supabase = get_supabase_client()

    to_upsert = {
        "filename": data["filename"],
        "transcript": data["transcript"]
    }

    response = supabase.table("Transcripts").upsert(to_upsert).execute()
    print("Saved to Supabase:", response)

def get_transcript_data(video_filename: str):
    supabase = get_supabase_client()

    response = supabase.table("Transcripts").select("filename, transcript").eq("filename", video_filename).execute()

    if response.data:
        data = response.data[0]
        return {
            "filename": data["filename"],
            "transcript": data["transcript"]
        }
    else:
        raise ValueError(f"No transcript found for filename: {video_filename}")



# env_path = Path(r"C:\Users\tural\ai_quizer\backend\.env").parent / ".env"
# load_dotenv(dotenv_path=env_path)

# url = os.getenv("SUPABASE_URL")
# key = os.getenv("SUPABASE_KEY")

# print(url, key)