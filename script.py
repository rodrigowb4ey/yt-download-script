from pytube import YouTube
import os

save_path = os.getcwd()

url = input("URL do vídeo: ")

yt = YouTube(url).streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download(save_path)
print("Download completo!")