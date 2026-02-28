masukan_angka1 = float(input("Masukkan angka pertama: "))
masukan_angka2 = float(input("Masukkan angka kedua: "))

print("*" * 50)
print("Pilih operator yang ingin digunakan:")


def operator_calculator():

    print("1. Penjumlahan")
    print("2. Pengurangan")
    print("3. Perkalian")
    print("4. Pembagian")
    print("5. Sisa Bagi")

    pilihan = input("Masukkan pilihan (1/2/3/4/5): ")

    if pilihan == '1':
        print(masukan_angka1, "+", masukan_angka2, "=", masukan_angka1 + masukan_angka2)

    elif pilihan == '2':
        print(masukan_angka1, "-", masukan_angka2, "=", masukan_angka1 - masukan_angka2)

    elif pilihan == '3':
        print(masukan_angka1, "*", masukan_angka2, "=", masukan_angka1 * masukan_angka2)

    elif pilihan == '4':
        print(masukan_angka1, "/", masukan_angka2, "=", masukan_angka1 / masukan_angka2)

    elif pilihan == '5':
        print(masukan_angka1, "%", masukan_angka2, "=", masukan_angka1 % masukan_angka2)

    else:
        print("Input yang anda masukan salah!")

operator_calculator()


