print("!!!!!!!!Welcome To This Quiz Game!!!!!!!!")

playing = input("Get to know me!! ")

if playing.lower() != "yes":
    quit()

print("Okay Lets Begin")

score = 0

question1 = input("Cyber Security or Software Development: ")
if question1.lower() == "Cyber Security":
    print("Correct!")
    score += 1
else:
    print('Incorrect!')

question1 = input("Extrovert or Introvert: ")
if question1.lower() == "Introvert":
    print("Correct!")
    score += 1
else:
    print('Incorrect!')

question1 = input("light or dark: ")
if question1.lower()  == "dark":
    print("Correct!")
    score += 1
else:
    print('Incorrect!')

question = input("Ass or Boobs: ")
if question.lower() == "ass":
    print("Correct")
    score += 1
else:
    print("Incorrect")

question = input("Happy or Happy: ")
if question.lower() == "Happy":
    print("Correct")
    score += 1
else:
    print("Incorrect")

print("You Got " + str(score) + " questions correct")
print("You Got " + str((score/5) * 100) + "%.")