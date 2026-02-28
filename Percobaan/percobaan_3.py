import random
from colorama import Fore, Style

def permainan():
    print(Fore.GREEN + "=" * 61)
    print("🪨✂️📜 Selamat Datang di Permainan Batu-Gunting-Kertas 📜 ✂️  🪨")
    print("=" * 61 + Style.RESET_ALL)

    pilihan_pemain = ["Batu", "Gunting", "Kertas"]

    # User input
    pilihan_player = input(Fore.YELLOW + "Pilih: Batu, Gunting, Kertas: " + Style.RESET_ALL).capitalize()
    if pilihan_player not in pilihan_pemain:
        print(Fore.RED + "Pilihan tidak valid! Hanya Batu, Gunting, atau Kertas yang diperbolehkan." + Style.RESET_ALL)
        print("Silakan coba lagi.\n")
        return permainan()

    # Bot's choice
    pilihan_bot = random.choice(pilihan_pemain)

    # Display choices
    print(Fore.GREEN + f"\nKamu memilih: {pilihan_player}" + Style.RESET_ALL)
    print(Fore.MAGENTA + f"Musuh memilih: {pilihan_bot}" + Style.RESET_ALL)

    # Determine the result
    if pilihan_player == pilihan_bot:
        print(Fore.BLUE + "Seri! Tidak ada pemenang kali ini." + Style.RESET_ALL)
    elif (pilihan_player == "Batu" and pilihan_bot == "Gunting") or \
         (pilihan_player == "Gunting" and pilihan_bot == "Kertas") or \
         (pilihan_player == "Kertas" and pilihan_bot == "Batu"):
        print(Fore.GREEN + "Selamat! Kamu Menang! 🎉" + Style.RESET_ALL)
    else:
        print(Fore.RED + "Sayang sekali, Kamu Kalah! 😢" + Style.RESET_ALL)

    # Replay prompt
    main_ulang = input(Fore.YELLOW + "\nApakah kamu ingin bermain lagi? (Yes/No): " + Style.RESET_ALL).capitalize()
    if main_ulang == "Yes":
        print(Fore.CYAN + "\nBersiaplah untuk ronde berikutnya!\n" + Style.RESET_ALL)
        permainan()
    else:
        print(Fore.CYAN + "\nTerima kasih telah bermain! Sampai jumpa lagi! 👋" + Style.RESET_ALL)

# Run the game
permainan()
