def greet(name):
    print("hello", name)
    print("how are you today !")

greet("Nathan")

def user():
    user = input("what is your Full Name: ").upper()
    print("welcome", user)
user()

#this function is incomplete as i have not been able to accept the values the users anters and adds them
#def numbers(x1,x2):
    #num_1 = input("Enter a Number: ")
    #x2 = input('Enter another Number: ')
    #result = x1 + x2
    #return result print("the sum is = ", numbers)

def sum():
    num1 = input("Enter the first number: ")
    print(f"your first number {num1}")
    num2 = input("Enter the second number: ")
    print(f"and your second number {num2}")
    result = num1 + num2
    print("and the sum of both numbers is ", result)





def sum_of_numbers(num1,num2):
    result = num1 + num2
    return result

num1 = 9
num2 = 10
result = sum_of_numbers(num1, num2)
print("the sum of n1 and n2 is = ", result)

print("NEW BLOCK OF CODE!!!!!!!!!")

def average_of_marks(marks):
    sumOfMarks = sum(marks)
    lengthOfmarks = len(marks)
    averageMarks = sumOfMarks / lengthOfmarks
    return averageMarks

def average_grade(averageMarks):
    if averageMarks >= 80:
        grade = 'A'
    elif averageMarks >= 60:
        grade = 'B'
    elif averageMarks >= 50:
        grade = 'C'
    else:
        grade = 'F'
    return grade

marks = [55,64,75,80,65]
averageMarks = average_of_marks(marks)
print("the average marks is: ", averageMarks)