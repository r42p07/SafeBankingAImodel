

from python import YouTube
url= ... .
yt_video = YouTube(url)
yt_video.stream.get_highest_resolution()
yt_video.download();

print("download fertig")