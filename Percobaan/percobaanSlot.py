import random

def spin_symbol():
    print("Mesin judol bergerak!")

    symbol = ["🤡", "🥶", "😁", "🤩","🥸"]

    result = []

    for i in range(3):
        spin = random.choice(symbol)
        result.append(spin)
    return result



def tampil_symbol(row):
    print("*"*13)
    print(" | ".join(row))
    print("*"*13)

def hasil_judol(row, bet):
    if row[0] == row[1] == row[2]:
        if row[0] == '🤡':
            return bet * 10
        elif row[0] == '🥶':
            return bet * 5
        elif row[0] == '😁':
            return bet * 4
        elif row[0] == '🤩':
            return bet * 2
        elif row[0] == '🥸':
            return bet * 3
        else:
            return bet
    return 0

    
def main():
    print("*"*24)
    print("Symbols: 🤡 🥶 😁 🤩 🥸")
    print("*"*24)

    balance = int(input("Masukan saldo anda : "))

    while balance > 0:
        if balance > 100:
            print(f"Jangan ragu untuk menang saldo anda ada {balance}")
        else:
            print(f"Nikmati saja karena saldo anda mungkin tidak cukup {balance}")

        bet = input("Masukan bet yang anda mau : ")

        if not bet.isdigit():
            print("Masukan bet sesuai dengan bentuk uang")
            continue

        bet = int(bet)

        if bet > balance:
            print("Pastikan saldo anda mencukup!")
            continue

        if bet <= 0:
            print("Masuakan bet lebih dari 0")
            continue

        balance -= bet

        row = spin_symbol()

        print("Spinning...")

        tampil_symbol(row)

        payout = hasil_judol(row, bet)

        if payout > 0:
            print(f"Selamat anda menang {payout}")
        else:
            print("You lose for this round, never give up!")

        balance += payout

        play_again = input("Yes or No : ").lower()

        if play_again != 'yes':
            print("Judol berhenti!")
            break

        print("*"*20)
        print(f"Game selesai hasil anda {balance}")
        print("Terimakasih sudah bermain!")
        print("*"*20)



    

if __name__ == '__main__':
    main()