import time 

my_time = int(input("Masukkan waktu dalam detik : "))

for x in range (my_time, 0, -1):
    detik = x % 60
    menit = x // 60
    jam = x // 3600
    print(f"{jam:02d}:{menit:02d}:{detik:02d}")
    time.sleep(1)

print("Waktu telah habis")