
import random
MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

symbol_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}
symbol_value = {
    "A": 5 ,
    "B": 4,
    "C": 3,
    "D": 2
}

def check_winnings(columns, lines , bet, values):
    winnings  = 0 
    winning_lines = []
    for line in range(lines):
        symbol = columns[0],[line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol] * bet
            winning_lines.append(lines + 1)
    return winnings, winning_lines


def get_slot_mechine_spin(rows, cols, symbols):
    all_symbols = []
    for symbols, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbols)
            
    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)
        columns.append(column)
    return columns

def print_slot_mechine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) -1:
                print(column[row],  end=" | ") 
            else:
                print(column[row])

        print()


def deposit():
    while True:
        amount = input("how much would you want deposit? $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be greater than 0.")
        else:
            print("Please enter a digit.")
    return amount

def get_number_of_lines():
    while True:
        lines = input("Enter the number of lines you want to bet on ( 1- " + str( MAX_LINES) +")? ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Enter a valid number of lines ")
        else:
            print("Please enter a digit.")
    return lines
    

def get_bet():
    while True:
        amount = input("how much would you want bett? $")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"Amount must be between ${MIN_BET} - ${MAX_BET}")
        else:
            print("Please enter a digit.")
    return amount

    
    
    
def instructions():
    print("Welcome to my betting scheme")
    print("you can deposit betting coins to the scheme and input the lines of slots you would want to bet on")
    print("Finally you would be asked to input how much you would be betting per line of slots ")
    print(f"Note for now there are only {MAX_LINES} lines of slots to bet on")

def spin(balance):
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bets = bet * lines

        if total_bets > balance:
            print(f"you do not have enough coins to bet with..., your current balance is ${balance}")
        else:
            break
   
    print(f"you are betting ${bet} on each {lines} slot. Total bet is : {total_bets}$")
    
    slots = get_slot_mechine_spin(ROWS, COLS, symbol_count)
    print_slot_mechine(slots)
    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_value)
    print(f"you won ${winnings}.")
    print(f"you won on line", * winning_lines)
    return winnings - total_bets

def main():
    instructions()
    balance = deposit()
    while True:
        print(f"your current balance is ${balance}")
        answer = input("Press enter to play and (q to quit)")
        if answer == "q":
            break
        balance += spin(balance)
    print(f"you are left with ${balance}")

main()