# Python slot machine
import random

def spin_gambar():
    symbols = ['🤡', '🥶', '😁', '🤩', '🥸']

    result = []

    for i in range(3):

        spin = random.choice(symbols)

        result.append(spin)
    return result

def print_gambar(row):
    print("***************")
    print(" | ".join(row))
    print("***************")
    pass

def get_payout(row, bet):
    if row[0] == row[1] == row[2]:
        if row[0] == "🥶":
            return bet * 5
        elif row[0] == "😁":
            return bet * 10
        elif row[0] == "🤩":
            return bet * 20
        elif row[0] == "🥸":
            return bet * 30
        elif row[0] == "🤡":
            return bet / 3
        else:
            return bet
    return 0

def main():
    print("*********************")
    print("Welcome to judol python")
    print("Symbols: 🤡 🥶 😁 🤩 🥸")
    print("*********************")
    
    balance = int(input("Masukan saldo anda : "))

    while balance > 0:
        print(f"Saldo anda saat ini {balance}")

        bet = input("Masukan bet anda : ")

        if not bet.isdigit():
            print("Masukan bet dalam bentuk uang")
            continue

        bet = int(bet)

        if bet > balance:
            print("Pastikan bet anda mencukupi!")
            continue

        if bet <= 0:
            print("Masuakan bet lebih dari 0")
            continue

        balance -= bet

        print()

        row = spin_gambar()

        print("Spinning... \n")

        print_gambar(row)

        payout = get_payout(row, bet)

        if payout > 0:
            print(f"You won ${payout}")
        else:
            print("You lose for this round, never give up!")

        balance += payout

        main_lagi = input("Yes Or No : ").lower()

        if main_lagi != "yes":
            print("Game Stop!")
            break
    print("******************************************")
    print(f"Game was finished now your balance is {balance}")
    print("Thank you for playing!")
    print("******************************************")

if __name__ == '__main__':
    main()