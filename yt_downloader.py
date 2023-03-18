from pytube import YouTube

# ask for the YouTube video URL
url = input("Enter the YouTube video URL: ")

# create a YouTube object and get the video information
yt = YouTube(url)

# print the video title and available streams
print("Title: ", yt.title)
print("Available Streams: ")
for stream in yt.streams:
    print(stream)

# ask the user to select a stream
itag = input("Enter the itag of the stream you want to download: ")

# filter the streams by itag and get the first result
stream = yt.streams.get_by_itag(itag)

# download the stream
print("Downloading...")
stream.download('D:/Jaspher/Downloads')
print("Download complete!")
