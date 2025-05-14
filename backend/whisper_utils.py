
def get_name_of_file(url):
    """Given a YouTube URL, determines the filename that would be generated if the audio were downloaded as a WAV file using yt_dlp.
    Args:
        url (str): The URL of the YouTube video.
    Returns:
        str: The expected filename (with .wav extension) for the downloaded audio file.
    Note:
        This function does not download the file; it only simulates the filename generation process.
    """
    
    import yt_dlp
    import os
    ydl_opts = {
        'format': 'bestaudio/best',
        'extractaudio': True,
        'audioformat': 'wav',
        'outtmpl': '%(title)s.%(ext)s',
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info_dict = ydl.extract_info(url, download=False)
        original_filename = ydl.prepare_filename(info_dict)
    filename = os.path.splitext(original_filename)[0] + ".wav"
    return filename


def transcribe_youtube_video(url):
    """
    Downloads the audio from a YouTube video, transcribes it using OpenAI's Whisper model, and returns the transcript.
    Args:
        url (str): The URL of the YouTube video to transcribe.
    Returns:
        dict: A dictionary containing:
            - "filename" (str): The path to the downloaded audio file in WAV format.
            - "transcript" (str): The transcribed text of the video's audio.
    Raises:
        Exception: If downloading, conversion, or transcription fails at any step.
    """

    import yt_dlp
    import whisper
    import os

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

    model = whisper.load_model("tiny")
    result = model.transcribe(filename)

    transcript = result['text']
    os.remove(filename)
    
    return {
        "filename":f"{filename}", 
        "transcript":f"{transcript}"
        }
