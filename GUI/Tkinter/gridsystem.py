from tkinter import *

root = Tk()
root.geometry("600x640")


lbl1 = Label(root, text = "Hi! I am Bijoy.")
lbl2 = Label(root, text = "Hello! I am Biswas.")
lbl3 = Label(root, text = "Ohh! Nice to meet you!")



lbl1.grid(row = 0, column = 0)
lbl2.grid(row = 1, column = 1)
lbl3.grid(row = 2, column = 2)
root.mainloop()