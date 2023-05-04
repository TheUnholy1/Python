import youtube_dl

# URL of the video to be downloaded
url = "https://youtu.be/pzBdRRjotM0"

# Path to the directory where the downloaded file will be saved
save_path = "D:/Jaspher/Downloads"

# Options for downloading the video
options = {
    "outtmpl": save_path + "/%(title)s.%(ext)s",
    "ignoreerrors": True,
}

# Create a YouTube downloader object
ydl = youtube_dl.YoutubeDL(options)

# Download the video
with ydl:
    ydl.download([url])

print("Download complete!")
