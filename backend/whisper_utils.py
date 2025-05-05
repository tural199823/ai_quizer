def transcribe_youtube_video(url):
    # 1. Download audio with yt_dlp
    # 2. Convert to WAV or MP3 if needed
    # 3. Run whisper on the file
    # 4. Return transcript

    import yt_dlp
    import whisper
    import os

    # Step 1: Download audio with yt_dlp
    ydl_opts = {
        'format': 'bestaudio/best',
        'extractaudio': True,
        'audioformat': 'wav',
        'outtmpl': '%(title)s.%(ext)s',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'wav',
            'preferredquality': '192',
        }],
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info_dict = ydl.extract_info(url, download=True)
        original_filename = ydl.prepare_filename(info_dict)

    filename = os.path.splitext(original_filename)[0] + ".wav"

    model = whisper.load_model("base")
    result = model.transcribe(filename)

    # Step 4: Return transcript
    transcript = result['text']

    return {
        "filename":f"{filename}", 
        "transcript":f"{transcript}"
        }

print("salam")

# somedic = transcribe_youtube_video("https://www.youtube.com/watch?v=r4IQopBxzOo")
# print(somedic["transcript"])
# print(somedic["filename"])
