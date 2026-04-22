import random

number = random.random()

if number > 99:
    print("Nilai Ratusan")
elif number > 80:
    print("Nilai dibawah 80", number)
elif number < 70:
     print("Nilai dibawah 70", number)
elif number < 60:
    print("Nilai dibawah 60", number)
else:
    print("bukan angka")
