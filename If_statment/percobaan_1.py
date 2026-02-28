# Calculator Simple 

from colorama import Fore, Style

def main():
    print(Fore.CYAN + "=" * 40)
    print("🧮 Selamat Datang di Kalkulator Sederhana 🧮")
    print("=" * 40 + Style.RESET_ALL)

    print(Fore.YELLOW + "Masukan Operasi Pengerjaan:" + Style.RESET_ALL)
    print(Fore.GREEN + "Pilihan: '+', '-', '*', '/'" + Style.RESET_ALL)
    
    operasi = input(Fore.YELLOW + "Operasi: " + Style.RESET_ALL).strip()
    if operasi not in ['+', '-', '*', '/']:
        print(Fore.RED + "Operasi tidak valid. Silahkan coba lagi!" + Style.RESET_ALL)
        return

    try:
        angka_1 = float(input(Fore.YELLOW + "Masukan Angka ke-1: " + Style.RESET_ALL))
        angka_2 = float(input(Fore.YELLOW + "Masukan Angka ke-2: " + Style.RESET_ALL))
    except ValueError:
        print(Fore.RED + "Input tidak valid. Harap masukan angka yang benar!" + Style.RESET_ALL)
        return

    print(Fore.CYAN + "=" * 40 + Style.RESET_ALL)

    if operasi == '+':
        hasil = angka_1 + angka_2
        print(Fore.GREEN + f"Hasil: {angka_1} + {angka_2} = {hasil}" + Style.RESET_ALL)
    elif operasi == '-':
        hasil = angka_1 - angka_2
        print(Fore.GREEN + f"Hasil: {angka_1} - {angka_2} = {hasil}" + Style.RESET_ALL)
    elif operasi == '*':
        hasil = angka_1 * angka_2
        print(Fore.GREEN + f"Hasil: {angka_1} * {angka_2} = {hasil}" + Style.RESET_ALL)
    elif operasi == '/':
        if angka_2 == 0:
            print(Fore.RED + "Error: Pembagian dengan nol tidak diperbolehkan!" + Style.RESET_ALL)
        else:
            hasil = angka_1 / angka_2
            print(Fore.GREEN + f"Hasil: {angka_1} / {angka_2} = {hasil}" + Style.RESET_ALL)

    print(Fore.CYAN + "=" * 40)
    print("Terima kasih telah menggunakan kalkulator ini! 🙌")
    print("=" * 40 + Style.RESET_ALL)

if __name__ == "__main__":
    main()
