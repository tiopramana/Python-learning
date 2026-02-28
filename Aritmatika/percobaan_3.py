import random
import math
import time
from colorama import Fore, Style

def perhitungan_quis(kesulitan):
    if kesulitan == "mudah":
        angka_max = 10
    elif kesulitan == "sedang":
        angka_max = 30
    else:
        angka_max = 100

    pengerjaan = random.choice(['+', '-', '*', '/', 'sqrt', '^'])

    if pengerjaan in ['+', '-', '*', '/']:
        angka1 = random.randint(1, angka_max)
        angka2 = random.randint(1, angka_max)

        if pengerjaan == '/':
            angka2 = random.randint(1, angka_max)  # Avoid division by zero
            angka1 = angka1 * angka2  # Ensure division result is integer

    elif pengerjaan == "sqrt":
        angka1 = random.randint(1, angka_max)
        angka2 = None  # No second number needed

    elif pengerjaan == "^":
        angka1 = random.randint(1, angka_max // 2)
        angka2 = random.randint(2, 4)

    return angka1, pengerjaan, angka2

def penyelesaian_masalah(angka1, pengerjaan, angka2):
    if pengerjaan == '+':
        return angka1 + angka2
    elif pengerjaan == '-':
        return angka1 - angka2
    elif pengerjaan == '*':
        return angka1 * angka2
    elif pengerjaan == '/':
        return angka1 // angka2
    elif pengerjaan == 'sqrt':
        return math.isqrt(angka1)
    elif pengerjaan == '^':
        return math.pow(angka1, angka2)

def animasi_intro():
    print(Fore.YELLOW + "===================================")
    print(" Selamat Datang di Quiz Matematika! ")
    print("===================================" + Style.RESET_ALL)
    for i in range(3, 0, -1):
        print(Fore.CYAN + f"Permainan dimulai dalam {i} detik..." + Style.RESET_ALL)
        time.sleep(1)

def permainan():
    animasi_intro()

    print(Fore.GREEN + "Pilih tingkat kesulitan: (mudah, sedang, sulit)" + Style.RESET_ALL)
    tingkat_kesulitan = input("Pilihan Anda: ").lower()
    score = 0
    total_permainan = 5

    print(Fore.MAGENTA + "\nMari mulai permainan!" + Style.RESET_ALL)
    print("=" * 30)

    for i in range(total_permainan):
        angka1, pengerjaan, angka2 = perhitungan_quis(tingkat_kesulitan)
        jawaban_benar = penyelesaian_masalah(angka1, pengerjaan, angka2)

        print(Fore.BLUE + f"Pertanyaan {i + 1}/{total_permainan}" + Style.RESET_ALL)
        if pengerjaan == 'sqrt':
            print(f"Berapa akar dari {angka1}?")
        elif pengerjaan == '^':
            print(f"Berapa {angka1} pangkat {angka2}?")
        else:
            print(f"Berapa {angka1} {pengerjaan} {angka2}?")

        try:
            user_answer = float(input(Fore.YELLOW + "Jawaban Anda: " + Style.RESET_ALL))
            if math.isclose(user_answer, jawaban_benar, rel_tol=1e-9):
                print(Fore.GREEN + "Benar! 🥳" + Style.RESET_ALL)
                score += 1
            else:
                print(Fore.RED + f"Salah! Jawaban yang benar adalah {jawaban_benar}." + Style.RESET_ALL)
        except ValueError:
            print(Fore.RED + f"Input tidak valid! Jawaban yang benar adalah {jawaban_benar}." + Style.RESET_ALL)

        print("=" * 30)

    print(Fore.CYAN + f"\nPermainan selesai! Skor akhir Anda adalah {score}/{total_permainan}." + Style.RESET_ALL)
    if score == total_permainan:
        print(Fore.GREEN + "Luar biasa! Anda menjawab semua dengan benar! 🎉" + Style.RESET_ALL)
    elif score >= total_permainan // 2:
        print(Fore.YELLOW + "Bagus! Anda cukup baik! 👍" + Style.RESET_ALL)
    else:
        print(Fore.RED + "Cobalah lagi untuk meningkatkan skor Anda! 💪" + Style.RESET_ALL)

if __name__ == "__main__":
    permainan()
