import yt_dlp
import streamlit as st

st.title("NPM Video Downloader")

videolink = st.text_input("Enter YouTube Video or Playlist Link:")
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
            # yt-dlp options (only fetch info, not save)
            ydl_opts = {
                "format": format_map[quality],
                "writesubtitles": download_subs,
                "subtitleslangs": [subs_lang] if download_subs else None,
                "noplaylist": False,  # allow playlist expansion
                "quiet": True,
                "extract_flat": False
            }

            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                info = ydl.extract_info(videolink, download=False)

            # Check if it's a playlist
            if "entries" in info:
                st.success(f"✅ Playlist found: {info.get('title','Playlist')}")

                for i, entry in enumerate(info["entries"], start=1):
                    v_title = entry.get("title", f"Video {i}")
                    v_url = entry.get("url")
                    if not v_url and "url" in entry:
                        v_url = entry["url"]

                    if v_url:
                        st.markdown(
                            f"{i}. [⬇️ Download **{v_title}**]({v_url})",
                            unsafe_allow_html=True
                        )
            else:
                final_name = video_name if video_name else info.get("title", "video")
                direct_url = info.get("url")

                if not direct_url:
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
