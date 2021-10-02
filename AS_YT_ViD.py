from pytube import YouTube
print("-----Welcome-----")
print("Enter URL here")
url = input()
print("Processing.......\nDownloading......")
yt = YouTube(url)
streams = yt.streams.get_highest_resolution()
streams.download()
print("Successfully Downloaded")