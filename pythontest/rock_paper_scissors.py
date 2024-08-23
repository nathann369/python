import random

user = 0
computer = 0

option = ["rock", "paper", "scissors"]

print('Welcome to Rock Paper Scissors')

while True:
    user_I = input("Type Rock/Paper/Scissors or Q to quit the game: ").lower()
    if user_I == "q":
        break
        


    if user_I not in option:
        continue

    random_n = random.randint(0,2)

    computer_pick = option[random_n]
    print("The Computer Picked", computer_pick + ".")
    if user == "rock" and computer ==  "scissors":
        print("Bravoo Youve won!!")
        user =+ 1
        

    elif user == "paper" and computer ==  "rock":
        print("Bravoo Youve won!!")
        user =+ 1
        

    elif user == "scissors" and computer ==  "paper":
        print("Bravoo Youve won!!")
        user =+ 1

    else:
        print('you lost ')
        computer += 1
        

print("You won", user, "times")
print("computer won", computer, "times")
print("GoodBye")