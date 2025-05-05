from fastapi import FastAPI, Request
from whisper_utils import transcribe_youtube_video
from supabase import save_to_supabase

save_to_supabase(transcribe_youtube_video("https://www.youtube.com/watch?v=r4IQopBxzOo"))