# Mencoba pembuatan calculator


def Calculator():
    print("#" * 33)
    print("Selamat datang di Calculator Tio!")
    print("#" * 33)

    is_running = True

    while is_running:
        metode = ["+", "-", "*", "/"]

        input_metode = input(
            "Masukan Metode Yang Ingin Digunakana > (+, -, *, /) dan (q) untuk keluar : "
        ).lower()

        if input_metode == "q":
            print("Terimakasih")
            break

        if input_metode not in metode:
            print("Metode Salah")
            break

        angka1 = int(input("Masukan angka pertama > "))
        angka2 = int(input("Masukan angka kedua > "))

        if input_metode == "+":
            hasil = angka1 + angka2
            print(hasil)
        elif input_metode == "-":
            hasil = angka1 - angka2
            print(hasil)
        elif input_metode == "*":
            hasil = angka1 * angka2
            print(hasil)
        elif input_metode == "/":
            hasil = angka1 / angka2
            print(hasil)
        else:
            print("Error")
            break


Calculator()
