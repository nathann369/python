from curses.ascii import isdigit
import random

top = input("type a Number:  ")

if top.isdigit():
    top = int(top)

    if top <= 0:
        print(" Please try a bigger number next time ")
        quit()
else:
    print("Please type a digit..")
    quit()

r = random.randint(0,top)
guesses = 0

print("this would be the number", r, "...")

while True:
    guesses += 1
    userg = input("Take a guess: ")
    if userg.isdigit():
        userg = int(userg)

    else:
        print("Please type a digit..")
        continue

    if userg == r:
        print("you are correct!!")
        break
    
    elif userg > r:
        print("you guesses above the number")
    else: 
            print("you are below the number !!")
print("you got it in " , guesses, "guesses")
