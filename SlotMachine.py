import random

def spin_row():
    symbols = ['🍒', '🍉', '🍋', '🔔', '⭐']

    results = []
    for symbol in range(3):
        results.append(random.choice(symbols))
    return results

def print_row(row):
    print("*************")
    print(" | ".join(row))
    print("*************")

def get_payout(row, bet):
    if row[0] == row[1] == row[2]:
        if row[0] == '🍒':
            return bet * 3
        elif row[0] == '🍉':
            return bet * 4
        elif row[0] == '🍋':
            return bet * 2
        elif row[0] == '🔔':
            return bet * 5
        elif row[0] == '⭐':
            return bet * 10
    return 0
        
         

def main():
    balance = 100

    print("************************")
    print("Welcome to python slots ")
    print("Symbols: 🍒 🍉 🍋 🔔 ⭐")
    print("************************")

    while balance > 0:
        print("****************************")
        print(f"Current balance: ₹{balance}")
        print("****************************")   

        bet = input("Please your bet amount: ")

        if not bet.isdigit():
            print("Please enter a valid number!")
            continue

        bet = int(bet)

        if bet > balance:
            print("Insufficient balance!")
            continue

        if bet <= 0:
            print("Bet must be greater than zero!")
            continue

        balance -= bet 

        row = spin_row()
        print("Spinning.......\n")
        print_row(row)

        payout = get_payout(row, bet)

        if payout > 0:
            print(f"You won: ₹{payout}")
        else:
            print("Sorry you lost the round!")

        balance += payout

        play_again = input("Do you want to play again? (Y/N): ").upper()

        if play_again != 'Y':
            break

if __name__ =='__main__':
    main()
