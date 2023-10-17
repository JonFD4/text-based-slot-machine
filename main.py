import random

MAX_LINES =3
MIN_BET = 1
MAX_BET = 100

ROWS= 3
COLS = 3

'''Making a dictionary to represent symbols'''
symbol_count ={
"A": 2,
"B": 4,
"C": 6,
"D": 8,

}
def get_slot_machine_spin(rows, cols, symbols):
    '''Generate what symbols are going to be in each column based on the frequency of symbols available.
    We need to randomly pick the number of rows inside each column;
    so if we have three rows, we need to pick three symbols that go into the each column. For each column, there has to be a random pick
    Create a list that contains all the possible values and to randomly choose three of those values. the chosen values are removed from the list.
    '''

    all_symbols =[]
    for symbol, symbol_count in symbols.items(): 
        for _ in range(symbol_count): # underscore is used to represent an anonymous variable because we don't care about the iteration/ count value
            all_symbols.append(symbol)


def deposit():
    '''It takes the user input for deposit. while loop
    continuously ask user for a valid amount until a valid amount is given. We want to check if the amound inputted is a number and if number is greater than zero'''
    while True:
        amount = input("What would you like to depsoit? £")
        if amount.isdigit(): #
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be greater than 0.")
        else:
            print("Please enter a number.")

    return amount   


def get_number_of_lines():
    while True:
        lines = input(f"Enter the number of lines to bet on 1 - {MAX_LINES} lines ?")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Enter a valid number of lines")
        else:
            print("Please enter a number")
    
    return lines
       


def get_bet():
    '''It takes the user input for bett. while loop
    continuously ask user for a valid amount until a valid amount is given. We want to check if the amound inputted is a number and if number is greater than zero'''
    while True:
        bet_amount = input("What would you like to bet? £")
        if bet_amount.isdigit(): #
            bet_amount = int(bet_amount)
            if MIN_BET <= bet_amount<=MAX_BET:
                break
            else:
                print(f"Amount must be between ${MIN_BET} and ${MAX_BET} .")
        else:
            print("Please enter a number.")

    return bet_amount 
     




def main():
    '''This is the start of the program. when the while loop breaks it takes user here and when the program is ended and user chooses restart, it brings the user here.'''
    balance = deposit() 
    lines = get_number_of_lines() 
    while True:
        bet= get_bet()
        total_bet= bet * lines

        if total_bet > balance:
            print(f"Insufficient funds. You need money!!!")
        else:
            break

    print(f"You are betting £{bet}  on {lines}. Total bet is equal to: ${total_bet}" )
    print(f"Your balance and number of lines: £{balance}, {lines} lines")
main()    