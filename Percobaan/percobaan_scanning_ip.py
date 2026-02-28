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

def get_ip_website(domain):
    try:
        ip_address = socket.gethostbyname(domain)
        print(f"Ip Address yang anda masuka : {ip_address}")
    except socket.gaierror:
        print("Gagal menemukan Domain! Silah Coba ulang")

def main():
    print("Website IP Address Scanner")
    print("==========================")
    # Meminta pengguna untuk memasukkan nama domain
    domain = input("Enter the website domain (e.g., example.com): ").strip()
    # Memanggil fungsi untuk mendapatkan IP
    get_ip_website(domain)
if __name__ == "__main__":
    main()

