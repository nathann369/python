import random


n = random.randint(1,10)
print('i am thinking of a number from 1 to 10')

running = True

while running:
    guess_str = input("Take a guess ")
    guess = int(guess_str)
    if guess == n:
        print("that was right")
        running = False
    elif guess < n:
        print("Try a bigger number")
    else:
        print("Try a smaller ")



def sum():
    num1 = input("Enter the first number: ").isdigit()
    num2 = input("Enter the second number: ")
    result = num1 + num2
    print("and the sum of both numbers is ", result)


def first_sum():
    sum()

first_sum()

