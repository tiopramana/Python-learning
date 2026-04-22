# Banking System With Python

def moneymachine():

    def withdraw():
        wd = float(input("Masukan nominal yang akan di tarik : "))
        if wd > money:
            print("Pastikan tidak wd lebih dari saldo anda")
        else:
            print(f"Wd berhasil sebesar {wd}")
        return wd

    def deposit():
        depo = float(input("Masukan nominal uang deposit : "))
        if depo < 0:
            print("Masukan nominal dengan benar")
        else:
            print(f"Deposit berhasil sebesar {depo} tunai")

        return depo

    def checkBalance(money):
        print(f"Sisa saldo anda {money}")
        pass

    money = 0.0
    atm_on = True

    while atm_on:
        print("Selamat datang di ATM BTI")
        print("Pilih menu")
        print("1. Check Saldo")
        print("2. Deposit Uang")
        print("3. Tarik Uang")
        print("4. Keluar")

        pilihan_user = input("Masukan pilihan anda : ")

        if pilihan_user == "1":
            checkBalance(money)
        elif pilihan_user == "2":
            money += deposit()
        elif pilihan_user == "3":
            money -= withdraw()
        elif pilihan_user == "4":
            break
        else:
            atm_on = False

if __name__ == '__main__':
    moneymachine()