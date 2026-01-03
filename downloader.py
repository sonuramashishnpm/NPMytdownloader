import yt_dlp
import os
import tempfile

def download_video(url):
    temp_dir = tempfile.mkdtemp()
    output_path = os.path.join(temp_dir, "video.%(ext)s")

    ydl_opts = {
        'outtmpl': output_path,
        'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best',
        'noplaylist': True,
        'age_limit': 99,
        'quiet': True,
        'merge_output_format': 'mp4',
        'extractor_args': {
            'youtube': {'player_client': 'default'}
        }
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=True)
        filename = ydl.prepare_filename(info)

    return filename
