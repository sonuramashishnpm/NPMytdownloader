!pip install yt-dlp

import yt_dlp

# YT video link (example)
url = "https://youtu.be/-33oXx0TwHI?si=dGHZSaKEaDdZdSE0"

# Output path Google Drive me (agar mounted ho)
output_path = "/content/drive/MyDrive/agentic_ai_tutorial.mp4"

ydl_opts = {
    'outtmpl': output_path,
    'format': 'mp4/best'
}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])
