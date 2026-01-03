async function download() {
  const url = document.getElementById("url").value;
  const status = document.getElementById("status");

  if (!url) {
    status.innerText = "Please enter a URL";
    return;
  }

  status.innerText = "Downloading... Please wait";

  try {
    const response = await fetch("/download", {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify({ url })
    });

    if (!response.ok) {
      const data = await response.json();
      throw new Error(data.error);
    }

    const blob = await response.blob();
    const a = document.createElement("a");
    a.href = window.URL.createObjectURL(blob);
    a.download = "video.mp4";
    document.body.appendChild(a);
    a.click();
    a.remove();

    status.innerText = "Download started ✔";

  } catch (err) {
    status.innerText = "Error: " + err.message;
  }
}
