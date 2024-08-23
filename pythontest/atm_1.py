#this project is incomplete 

USER_1 = "cat"
PIN_1 = 123
USER_ID_1 = 220987654
USER_2 = "dog"
PIN_2 = 321
USER_ID_2 = 220456789
USER_3 = "goat"
PIN_3 = 000
USER_ID_3 = 220123456

MAX_BAL = 50000


MIN_BAL = 10

NEW_BALANCE = 0

A = 1000
B = 500
C = 200
D = 100
E = 0



def welcome_message():
    print('welcome to our ATM Demo service')
    print('lets assume your card has already been inputed ')

#Transfer function
def transfer():
    while True:
        transfer = input("How Much Do You Want To Transfer: $")
        if transfer.isdigit():
            transfer = int(transfer)
            user = input("Enter User Acc No:")
            if user != USER_ID_1:
                print(f'You are about to transfer ${transfer} to {user} :)')
                break
            elif user != USER_ID_2:
                 print(f'You are about to transfer ${transfer} to {user} :)')
                 break
            elif user != USER_ID_3:
                 print(f'You are about to transfer ${transfer} to {user} :)')
                 break
            else:
                 print('incorrect user :(')
                 
        else:
                print('Invalid input :(')
                print('Please enter a digit')
# deposite Function
def deposite():
    while True:
        deposite = input("How Much Do You Want To Deposite: $")
        if deposite.isdigit():
            deposite = int(deposite)
            print(f"You Are About To Deposite ${deposite} In Your Account")
            balance = deposite + NEW_BALANCE
            print("Your balance is: $",balance)
            break
                 
        else:
                print('Invalid input :(')
                print('Please enter a digit')

#login function
def get_user():
    while True:
        user_input = input("Please enter your pin: ")
        if user_input.isdigit():
            user_input = int(user_input)
            if user_input == PIN_1:
                print(f'welcome {USER_1} :)')
                break
            elif user_input == PIN_2:
                 print(f'welcome {USER_2} :)')
                 break
            elif user_input == PIN_3:
                 print(f'welcome {USER_3} :)')
                 break
            else:
                 print('incorrect user :(')
                 
        else:
                print('Invalid input :(')
                print('Please enter a digit')
    return user_input
# Withdrawal Function
def withdrawal():
    while True:
        
        print('How much do you want to withdraw?')
        print("A. $1000")
        print("B. $500")
        print("C. $200")
        print("D. $100")
        print("E. Input Your amount")
        amount = input("Enter Amount: ").upper()
        
        if amount == "A":
            amount = A
            print(f"You are About to witdraw ${amount}" )
            balance = amount - MAX_BAL
            #print(f"your balance is ${balance}")
            break
        elif amount == "B":
            amount = B
            print(f"You are About to witdraw ${amount}")
            balance = amount - MAX_BAL
            #print(f"your balance is ${balance}")
            break
        elif amount == "C":
            amount = C
            print(f"You are About to witdraw ${amount}")
            balance = amount - MAX_BAL
            #print(f"your balance is ${balance}")
            break
        elif amount == "D":
            amount = D
            print(f"You are About to witdraw ${amount}")
            balance = amount - MAX_BAL
            #print(f"your balance is ${balance}")
            
            break
        elif amount == "E":
            while True:
                N_amount = input("Enter your amount: $")
                if N_amount.isdigit():
                    N_amount = int(N_amount)
                    if N_amount <= MIN_BAL:
                        print("you need to have a minimum of $10 in your account ")
                    else:
                        N_amount = E
                        print(f"you are about to witdraw ${E}")
                    break
                else:
                    print("INVALID INPUT!!!")
                    print("enter a numeric amount")
                    
            return N_amount
        N_amount = amount
        #balance = amount - NEW_BALANCE
        NEW_BALANCE = MAX_BAL - amount
        print(f"your balance is ${NEW_BALANCE}")
    return amount


#Check balance method
def check_balance():
    print(f"your balance is :${MAX_BAL}")
    #if withdrawal() == NEW_BALANCE:
       # print()
    #if NEW_BALANCE != MAX_BAL:
     #   NEW_BALANCE = E  - MAX_BAL
      #  print(f"your balance is ${NEW_BALANCE}")


#how to change pin ("i havent impplemented the complete and correct function")

def change_pin():
    while True:
        pin = input("Enter Last Known Pin: ")
        if pin.isdigit():
            pin = int(pin)
            if pin == PIN_1:
                print("Enter New Pin: ")
                break
            elif pin == PIN_2:
                print("Enter New Pin: ")
                break
            elif pin == PIN_3:
                print("Enter New Pin: ")
                break
            else:
                print("Invalid Pin")
        else:
            print("Invalid Input!!! please enter a Digit")


#option function
def options():
    while True:
        print("Dear Highly Estimed User how would you like to proceed ")
        print("1.Withdrawals")
        print("2. Transfer")
        print("3. Check Balance")
        print("4. Deposite")
        print("5. Change Pin")
        response = input('')
        if response.isdigit():
            response = int(response)
            if response == 1:
                response = withdrawal()
                break
            elif response == 2:
                response = transfer()
                break
            elif response == 3:
                response = check_balance()
                break
            elif response == 4:
                response = deposite()
                break
            elif response == 5:
                response = change_pin()
                break
            else:
                print("Invalid Input")

        else:
            print("Invalid Input!!! please enter a Digit")
    return response
    

#main function
def atm_1():
    while True:
        welcome_message()
        get_user()
        options()

        print("Press Enter to perform another Transaction OR N to Exit")
        exit = input('').upper()
        if exit == "N":
            quit()
        

atm_1()