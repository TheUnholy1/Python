from pytube import YouTube

link = "https://youtu.be/cKCOr45Xz1I" #Paste the link in here

yt = YouTube(link)

print("Title: ", yt.title)

print("View: ", yt.views)

yd = yt.streams.get_highest_resolution()

yd.download('D:/Jaspher/Downloads')