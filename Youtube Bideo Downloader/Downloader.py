from tkinter import *
from pytube import YouTube
from PIL import Image, ImageTk

root = Tk()
root.geometry("600x640")
root.title("Video Downloader")
root.resizable(False, False)

icon = PhotoImage(file = 'icon.jpg')
root.iconphoto(False, icon)

back_ground = Image.open('images.jpg')
back_ground = back_ground.resize((600, 640), Image.ANTIALIAS)
resized = ImageTk.PhotoImage(back_ground)

place_img = Label(root, image = resized)
place_img.place(x = 0, y = 0)

front_text = Label(root, text = 'Youtube Video Downloader', font = ('arial', 20), fg = 'blue')
front_text.pack(padx = 10, pady = 20)

paste = Label(root, text = 'Type or paste your video url here', font = ('arial', 15), fg = 'blue')
paste.pack(padx = 10, pady = 140)

url = StringVar()

url_box = Entry(root, width = 50, font = 35, textvariable = url, bd = 10)
url_box.place(x = 65, y = 260)


def download() :
    link = YouTube(str(url.get()))
    video = link.streams.first()
    video.download()

    Complet_button = Label(root, text = "DOWNLOADED", font = ('arial', 18), fg = 'black', bg = 'powderblue')
    Complet_button.place(x = 210, y = 383)


Download_button = Button(root, text = 'DOWNLOAD', font = "arial 18", foreground='black', bg = 'green', command = download)
Download_button.place(x = 220, y = 330)

root.mainloop()