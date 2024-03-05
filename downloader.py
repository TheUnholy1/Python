import yt_dlp

url = input("Enter video url: ")

ydl_opts = {
    'outtmpl': 'D:/Jaspher/Downloads %(title)s.%(ext)s',
}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])

print('Download complete')
