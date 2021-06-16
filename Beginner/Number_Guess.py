import random
import sys
#Number Guessing Game.....
num = int(input("Enter a number to select range. It start from 1. : "))
number = random.randint(0, num) #take number randomly
print("Guess the number. if you want to stop game then enter 0.")
while True :    
    guess = int(input("Enter a number: "))
    if guess == 0:
        sys.exit()
    else:
        if guess == number :
            print("Wow! you got it!")
            sys.exit()
        elif guess > number :
            print("This number is greater than hiden number. Try again!")
        else :
            print("This number is lower than hiden number. Try again!")