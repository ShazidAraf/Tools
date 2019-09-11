import pytube
import os

if os.path.isfile('videos'):
	os.mkdir('videos') 

link = "https://www.youtube.com/watch?v=itruPegL7wo"
yt = pytube.YouTube(link)
stream = yt.streams.first()
stream.download('videos/')
