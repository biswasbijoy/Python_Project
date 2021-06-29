#Digital Clock

from tkinter import *
from tkinter.font import BOLD
from tkinter.ttk import *
from time import strftime

root = Tk()
root.title("Digital Clock")

label = Label(root, font = ('Harlow Solid Italic', 50, 'bold'),
              foreground = 'purple',
              background = 'white')

def time() :
    txt = strftime('%H: %M: %S %p')
    label.config(text = txt)
    label.after(1000, time)

label.pack(anchor='center')
time()

root.mainloop()