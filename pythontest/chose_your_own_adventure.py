name = input("Enter Your Name: ")
print("welcome", name, "to this game ")

answer = input("You are at the end of a junction, and you can only go left ro right. which direction will you go towards ").lower() 

if answer == "left":
    answer2 = input("you just arrived at a river, would you either walk around it or swim across? Type WALK to walk around or SWIM to swim across ").lower()
    if answer2 == "walk":
        print()
    elif answer2 == "swim":
        print()
    else:
        print("invalid answer!!")

elif answer == "right":
    print()
else:
    print("Not a valid option!!")