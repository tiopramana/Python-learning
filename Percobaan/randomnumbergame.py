import random
import time
import os

angka1 = 1
angka2 = 5
jawaban = random.randint(angka1, angka2)
tebakan = 0
waktu = 5
mulai = True

print("Selamat datang di game tebak angka")
print(f"Silahka masukan angka dari {angka1} hingga {angka2} dari waktu 5 detik")

while mulai:
    while waktu:
        mins, secs = divmod(waktu, 60)
        print(f'{secs:02d}', end="\r")
        time.sleep(1)
        waktu -= 1
    print("Mulaii!!")
    
    tebak = input("Masukan tebakan angka : ")

    if tebak.isdigit():
        tebak = int(tebak)
        tebakan += 1

        if tebak < angka1 or tebak > angka2:
            print("This number is out of range!")
            print(f"Please select a number between {angka1} and {angka2}")

    if tebak == jawaban:
        tebakan += 1
        print("Selamat anda berhasil memilih", jawaban)
    else:
        print("Maaf anda salah jawaban nya adalah", jawaban)
        break

