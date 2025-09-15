import yt_dlp
import streamlit as st
from io import BytesIO

st.title("NPM Video Downloader")

videolink = st.text_input("Enter YouTube Video Link:")
video_name = st.text_input("Custom Video Name (optional):")
quality = st.selectbox("Select Quality:", ["1080p", "720p", "480p", "Audio Only"])
format_map = {
    "1080p": "bestvideo[height<=1080]+bestaudio/best",
    "720p": "bestvideo[height<=720]+bestaudio/best",
    "480p": "bestvideo[height<=480]+bestaudio/best",
    "Audio Only": "bestaudio/best"
}
download_subs = st.checkbox("Download Subtitles?")
subs_lang = st.text_input("Subtitles Language (e.g., en):", "en") if download_subs else None

if st.button("Download"):
    if videolink:
        try:
            # yt-dlp options for memory download
            ydl_opts = {
                'format': format_map[quality],
                'writesubtitles': download_subs,
                'subtitleslangs': [subs_lang] if download_subs else None,
                'noplaylist': False,
                'outtmpl': '-',  # output to stdout
                'quiet': True
            }

            # Download to BytesIO buffer
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                buffer = BytesIO()
                info = ydl.extract_info(videolink, download=False)
                final_name = video_name if video_name else info.get('title', 'video')
                # Download to temp file
                ydl_opts['outtmpl'] = final_name + '.%(ext)s'
                ydl = yt_dlp.YoutubeDL(ydl_opts)
                ydl.download([videolink])

            st.success(f"✅ '{final_name}' ready to download!")
            st.download_button(
                label="⬇️ Download to Device",
                data=open(final_name+'.mp4', 'rb').read(),
                file_name=final_name+'.mp4',
                mime='video/mp4'
            )

        except Exception as e:
            st.error(f"❌ Failed to download: {e}")
