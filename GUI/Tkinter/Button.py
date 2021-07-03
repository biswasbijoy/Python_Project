from tkinter import *

root = Tk()

root.geometry("600x640")

def click() :
    lbl = Label(root, text = "Haha! Kaysa Laga mera mojak! :D :D",
                font = ('Harlow Solid Italic', 18),
                foreground = 'green')
    lbl.pack(padx = 30, pady = 10)


button = Button(root, text = "Click",font = ("Harlow Solid Italic", 16, 'bold'),
                foreground='green', bg = 'powderblue', command = click)
button.pack(pady = 50)


root.mainloop()