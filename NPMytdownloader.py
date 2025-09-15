import yt_dlp
import streamlit as st

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
            # yt-dlp options (NO local saving, only fetch link)
            ydl_opts = {
                "format": format_map[quality],
                "writesubtitles": download_subs,
                "subtitleslangs": [subs_lang] if download_subs else None,
                "noplaylist": False,
                "quiet": True
            }

            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                info = ydl.extract_info(videolink, download=False)
                final_name = video_name if video_name else info.get("title", "video")

                # direct video/audio link
                if "url" in info:
                    direct_url = info["url"]
                elif "entries" in info:  # playlist case -> first entry
                    direct_url = info["entries"][0]["url"]
                else:
                    raise Exception("Could not extract video URL")

            st.success(f"✅ '{final_name}' ready to download!")
            st.markdown(
                f"[⬇️ Click here to download **{final_name}**]({direct_url})",
                unsafe_allow_html=True
            )

            if download_subs:
                st.info("🎬 Subtitles will auto-load in the video if available.")

        except Exception as e:
            st.error(f"❌ Failed to get link: {e}")
