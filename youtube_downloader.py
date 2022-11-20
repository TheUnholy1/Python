from pytube import YouTube

link = "https://youtu.be/UZX5kH72Yx4" #Paste the link in here

yt = YouTube(link)

print("Title: ", yt.title)

print("View: ", yt.views)

yd = yt.streams.get_highest_resolution()

yd.download('D:/Jaspher/Downloads')
