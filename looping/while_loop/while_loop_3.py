angka = int(input("Masukan Angka dari 1 - 10 : "))

while angka < 1 or angka > 10:
    print(f"{angka} Angka Tidak Valid ")
    angka = int(input("Masukan Angka dari 1 - 10 : "))

print(f"Angka Yang Kamu pilih adalah {angka}")