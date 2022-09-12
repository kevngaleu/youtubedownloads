from pytube import Youtube
from sys import argv

link = argv[1]
yt = Youtube(link)

print ("Title: ", yt.title)

print ("View: ", yt.views)


#yd = y.streams.get_by_resolution("720p")
yd = y.streams.get_audio_only()

yd.download('/home/kokobanks/videos')

