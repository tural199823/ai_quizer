from groq import Groq
import os
from dotenv import load_dotenv
from pathlib import Path


env_path = Path(r"C:\Users\tural\ai_quizer\backend\.env")
load_dotenv(dotenv_path=env_path)

# Initialize Groq client
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

# Set path to audio file
audio_path = env_path.parent / "How Your Brain Works？ - The Dr. Binocs Show ｜ Best Learning Videos For Kids ｜ Peekaboo Kidz.wav"
print(f"Audio path: {audio_path}")

print(audio_path)

with open(audio_path, "rb") as file:
    response = client.audio.transcriptions.create(
        file=file,
        model="whisper-large-v3",
        prompt="Just return a plain transcript",
        response_format="json",
        language="en",
        temperature=0.0,
    )

    print(response.text)

#     