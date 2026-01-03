from flask import Flask, render_template, request, send_file, jsonify
from downloader import download_video
import os

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/download", methods=["POST"])
def download():
    data = request.json
    url = data.get("url")

    if not url:
        return jsonify({"error": "No URL provided"}), 400

    try:
        file_path = download_video(url)

        return send_file(
            file_path,
            as_attachment=True,
            download_name=os.path.basename(file_path)
        )

    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True)
