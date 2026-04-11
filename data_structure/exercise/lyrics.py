import sys
import time 

print("Lagu")

def liriklagu():
    baris = [
        ("HIDUP ANIS BASWEDANN", 0.58, 0.2),
        ("HIDUP ANIS BASWEDANN", 0.58, 0.2),
        ("HIDUP ANIS BASWEDANN", 0.58, 0.2),
    ]

    print("ANIESSS")
    time.sleep(1)

    for char, delay_char, delay_line in baris:
        for lirik in char:
            print(lirik, end="", flush=True)
            time.sleep(delay_char)
        print()
        time.sleep(delay_line)
liriklagu()