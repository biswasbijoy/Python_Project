import tkinter as tk
from typing import Sized
from pytube import YouTube
from PIL import ImageTk, Image

root = tk.Tk()

root.title('Youtube Video Downloader')
root.geometry('600x600')
root.resizable(0, 0)
image2 = Image.open("E:\\1E__Document\VS Code\Pythone project\Video_downloader.jpg")
image2 = image2.resize((600, 600), Image.ANTIALIAS)
reimage2 = ImageTk.PhotoImage(image2)

#BG
load_img1 = tk.Label(root, image = reimage2)
load_img1.place(x = 0, y = 0)

m1 = tk.Label(root, text = 'Youtube Video Downloader', font = 'arial 18', foreground = 'blue', bg = '#f4c2c2')
m1.place(x = 155, y = 100)

url = tk.StringVar()


dis = tk.Label(root, text = 'Enter url or Paste link here:', font = ('calibri', 20), foreground = 'green', bg = '#8cff9e')
dis.place(x = 154, y = 200)
url_box = tk.Entry(root, width = 80, textvariable = url)
url_box.place(x = 60, y = 280)


def Download() :
    link = YouTube(str(url.get()))
    vdo = link.streams.first()
    vdo.download()
    Completed_buton = tk.Label(root, text = 'DOWNLOADED 💯', font = ('calibri'), bg = 'green', foreground = 'white')
    Completed_buton(x = 280, y = 300)

button = tk.Button(root, text = 'DOWNLOAD', font = ('calibri'), bg = 'green', padx = 3, command = Download)

button.place(x = 250, y = 320)


root.mainloop()