import yt_dlp

url = input("Enter your youtube video link")

output_path =input("Enter video path where to save")

ydl_opts = {
    'outtmpl': output_path,
    'format': 'mp4/best'
}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])
