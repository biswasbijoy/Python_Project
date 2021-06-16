import tkinter as tk
from random import randint
import time
import pygame as pg
from PIL import Image, ImageTk
import turtle
from pygame import mixer

snake_speed = 10

mixer.init()
music1 = '3_min.mp3'
music2 = '5_min.mp3'

music_no = 0
mq = [music1, music2]

mixer.music.load(mq[music_no])
mixer.music.play()

pg.init()
MUSIC_ENDED = pg.USEREVENT
pg.mixer.music.set_endevent(MUSIC_ENDED)



root = tk.Tk()
root.title('Snake Game')
root.state('zoomed')

img = Image.open('images.jpg')
img = img.resize((1280, 720), Image.ANTIALIAS)
resized_img = ImageTk.PhotoImage(img)

img1 = Image.open('images1.jpg')
img1 = img1.resize((1280, 720), Image.ANTIALIAS)
resized_img1 = ImageTk.PhotoImage(img1)


load_img = tk.Label(root, image = resized_img)
load_img.place(x = 0, y = 0)


#load_img1 = tk.Label(root, image = resized_img1)
#load_img1.place(x = 0, y = 0)


score_board = tk.Frame(root, bg = 'orange')
score_board.pack(fill = 'x')

score_txt = tk.Label(score_board, text = 'Score: ', font = ('satisfy', 18), foreground='blue', bg = 'orange')
score_dgt = tk.Label(score_board, text = '0', font = ('satisfy', 18), foreground='blue', bg = 'orange')
high_score_txt = tk.Label(score_board, text = 'High Score: ', font = ('satisfy', 18), foreground='blue', bg = 'orange')
high_score_dgt = tk.Label(score_board, text = '0', font = ('satisfy', 18), foreground='blue', bg = 'orange')


score_txt.pack(side = 'left')
score_dgt.pack(side = 'left')
high_score_dgt.pack(side = 'right')
high_score_txt.pack(side = 'right')


#Game screen
canvas = tk.Canvas(root, height = 600, width = 640)

game_screen = turtle.TurtleScreen(canvas)
game_screen.bgcolor('#3a5f0b')
canvas.pack(ipady = 30)
game_screen.tracer(0)

#Head
head = turtle.RawTurtle(game_screen)
head.speed(0)
head.shape('circle')
head.color('red')
head.penup()
head.goto(0, 0)
head.direction = 'stop'


#Food

food = turtle.RawTurtle(game_screen)
food.speed(0)
food.shape('circle')
food.color('skyblue')
food.penup()
food.goto(0, 100)



snake_body = []

#movement setup 

def up() :
    if head.direction != 'down' :
        head.direction = 'up'
def down() :
    if head.direction != 'up' :
        head.direction = 'down'
def left() :
    if head.direction != 'right' :
        head.direction = 'left'
def right() :
    if head.direction != 'left' :
        head.direction = 'right'


def move() :
    global snake_speed

    if head.direction == 'right' :
        x = head.xcor()
        head.setx(x + snake_speed)
    if head.direction == 'left' :
        x = head.xcor()
        head.setx(x - snake_speed)
    if head.direction == 'up' :
        y = head.ycor()
        head.sety(y + snake_speed)
    if head.direction == 'down' :
        y = head.ycor()
        head.sety(y - snake_speed)



def theme() :
    load_img.config(image = resized_img)
    game_screen.bgcolor('#3a5f0b')
    score_txt.config(foreground='blue')
    score_dgt.config(foreground = 'blue')
    high_score_txt.config(foreground = 'blue')
    high_score_dgt.config(foreground = 'blue')
    head.color('red')


def theme1() :
    load_img.config(image = resized_img1)
    game_screen.bgcolor('powderblue')
    score_txt.config(foreground = 'cyan')
    score_dgt.config(foreground = 'cyan')
    high_score_txt.config(foreground = 'cyan')
    high_score_dgt.config(foreground = 'cyan')
    head.color('red')


def close():
    mixer.music.stop()
    pg.event.clear()
    root.destroy()
    
root.protocol('WM_DELETE_WINDOW',close)
#Controling

game_screen.listen()
game_screen.onkeypress(up, 'Up')
game_screen.onkeypress(down, 'Down')
game_screen.onkeypress(left, 'Left')
game_screen.onkeypress(right, 'Right')


high_score = 0
score = 0
start = False

while True :
    game_screen.update()

    if head.xcor() > 310 or head.xcor() < -310 or head.ycor() > 290 or head.ycor() < -290 :
        time.sleep(1) 
        head.goto(0, 0)
        head.direction = 'stop'
        for body in snake_body :
            body.goto(1000, 1000)
    
        if score > high_score :
            high_score = score
            high_score_dgt.config(text = high_score)
        
        snake_body.clear()
        score = 0
        score_dgt.config(text = score)
        start = False
        speed = 10
        theme()

    if head.distance(food) < 30 :
        start = True
        x = randint(-310, 310)
        y = randint(-290, 290)
        food.goto(x, y)


        add_body = turtle.RawTurtle(game_screen)
        add_body.shape('square')
        add_body.color('blue')
        add_body.speed(0)
        add_body.penup()
        snake_body.append(add_body)

        score += 1
        score_dgt.config(text = score)
        if score >= 15 :
            theme1()
            for i in range(0,len(snake_body)):
                s = snake_body[i]
                s.color('#8533ff')
    for i in range(len(snake_body) - 1, 0, -1) :
        x = snake_body[i - 1].xcor()
        y = snake_body[i - 1].ycor()
        snake_body[i].goto(x, y)
    if len(snake_body) > 0 :
        x = head.xcor()
        y = head.ycor()
        snake_body[0].goto(x, y)
    
    move()

    for body in snake_body: # we check each segment
        if body.distance(head) < 10:
            time.sleep(1) # we sleep
            head.goto(0,0) # go back to the center
            head.direction = 'stop' # stop moving
            
            # Hide the segments
            for body in snake_body:
                body.goto(1000,1000)

            # update the highest score
            score -= 10
            if score > high_score:
                highScore = score
                high_score_dgt.config(text=highScore)
                    
            # Clear the segments list
            snake_body.clear()
            score = 0
            score_dgt.config(text=score)
            speed = 10
            start = False
            theme()
    for event in pg.event.get():
        if event.type == MUSIC_ENDED:
            music_no += 1
            if music_no > len(mq) - 1:
                music_no = 0
                mixer.music.load(mq[music_no])
                mixer.music.play()
            else:
                mixer.music.load(mq[music_no])
                mixer.music.play()
            
    time.sleep(0.08)

root.mainloop()