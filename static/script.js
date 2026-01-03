async function download() {
  const url = document.getElementById("url").value;
  const btn = document.getElementById("downloadBtn");
  const status = document.getElementById("status");

  if (!url) {
    showStatus("Please paste a YouTube link", "error");
    return;
  }

  btn.classList.add("loading");
  showStatus("Fetching video & preparing download…", "");

  try {
    const response = await fetch("/download", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ url })
    });

    if (!response.ok) {
      const data = await response.json();
      throw new Error(data.error);
    }

    const blob = await response.blob();
    const a = document.createElement("a");
    a.href = URL.createObjectURL(blob);
    a.download = "video.mp4";
    document.body.appendChild(a);
    a.click();
    a.remove();

    showStatus("Download started. Choose where to save.", "success");

  } catch (err) {
    showStatus(err.message, "error");
  } finally {
    btn.classList.remove("loading");
  }
}

function showStatus(message, type) {
  const status = document.getElementById("status");
  status.className = `status ${type}`;
  status.innerText = message;
  status.classList.remove("hidden");
}

function resetUI() {
  document.getElementById("status").classList.add("hidden");
}
