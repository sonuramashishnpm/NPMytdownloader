Ultimate YouTube Downloader 🟢

A simple and interactive YouTube video/audio downloader using Python, yt-dlp, and Streamlit.
Download single videos in multiple qualities, optionally with subtitles, and save them directly to your device via browser.

🔹 Features

Single Video Download – Download any YouTube video using its link.

Quality Selection – Choose from 1080p, 720p, 480p, or Audio Only formats.

Subtitles Download – Optionally download subtitles in any language (e.g., en).

Custom Video Name – Save the video with a custom filename.

Direct Device Download – Video saved directly on your device via st.download_button (no server storage).

Metadata Preview – Before download, video info is displayed (title, uploader, duration, views, thumbnail).

Error Handling & Retry – Automatic handling of common errors.

Interactive GUI – Fully browser-based interface using Streamlit.

🔹 Screenshots

(Add screenshots of Streamlit GUI here if needed)

🔹 Installation

Clone the repository

git clone https://github.com/<username>/ultimate-yt-downloader.git
cd ultimate-yt-downloader


Install dependencies

pip install -r requirements.txt


requirements.txt:

streamlit
yt-dlp

🔹 How to Run

Run locally

streamlit run ultimate_yt_downloader.py


This will open Streamlit app in your browser.

Enter video link

Paste the YouTube link in the input box.

Enter optional custom video name.

Select quality and enable subtitles if needed.

Download

Click Download → Wait until video is ready.

Click ⬇️ Download to Device → Video saved directly to your local device.

🔹 Usage Tips

Audio Only → Great for music, lectures, or podcasts.

Custom Name → Helps keep your downloads organized.

Subtitles → Use correct language code (e.g., en for English).

Browser Download → Ensures files are saved directly on your PC or phone.

🔹 Notes

This app runs entirely in browser with Streamlit.

Files are not stored on any server – everything downloads locally.

Works on PC and mobile browsers (if phone supports Streamlit via local server).

🔹 Future Improvements

Add Playlist & Batch download.

Add progress bar in GUI for download status.

Integrate Google Drive save option for cloud storage.

🔹 License

MIT License – Free to use, modify, and distribute.
