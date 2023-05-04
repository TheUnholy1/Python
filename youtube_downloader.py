from pytube import YouTube

LINK = "https://youtu.be/2Q5pLZotsqg" #Paste the link in here

yt = YouTube(LINK)

print("Title: ", yt.title)

print("View: ", yt.views)

yd = yt.streams.get_highest_resolution()

yd.download('D:/Jaspher/Downloads')
print("Download complete!")
