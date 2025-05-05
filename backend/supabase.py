def save_to_supabase(data: dict) -> None:
    
    from dotenv import load_dotenv
    from pathlib import Path
    from supabase import create_client, Client
    import os

    env_path = Path(r"C:\Users\tural\quizmaker\backend\.env").parent / ".env"

    load_dotenv(dotenv_path=env_path)

    # Now try to access your variables
    url = os.getenv("SUPABASE_URL")
    key = os.getenv("SUPABASE_KEY")

    # Create client
    supabase: Client = create_client(url, key)

    # # Insert data into the table
    response = supabase.table("Transcripts").insert(data).execute()
    print(response)
