#Python Project. Beginner Level. Level 1
# Dice Rolling game.....
import random
import tkinter as bijoy

root = bijoy.Tk() # main window
root.geometry("750x475") # Resize
root.title('Roll Dice') #title

ll = bijoy.Label(root, text = '', font = ("times new roman",260)) #level to display dice

#Activate button
def roll() :
    number = ['\u2680', '\u2681', '\u2682', '\u2683', '\u2684', '\u2685']
    ll.configure(text = f'{random.choice(number)}')
    ll.pack()

b1 = bijoy.Button(root, text = "ROLL DICE",font = ('times new roman', 15), foreground = 'white', background = 'navyblue' ,command = roll) #button
b1.place(x = 317, y = 340)           
root.mainloop() #keep window running