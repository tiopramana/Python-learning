import random


print("Selamat datang di game batu gunting kertas")
print("Silahkan pilih : (batu, gunting, kertas)")

def permainan():
    pilihan = ['gunting', 'batu', 'kertas']

    pilihan_player = input("Masukan pilihan : ")

    if pilihan_player not in pilihan:
        print("Pilihan tidak sesuai")
        print("Silahkan coba lagi")
        return permainan()
    
    pilihan_bot = random.choice(pilihan)

    if pilihan_bot == pilihan_player:
        print("Hasil seri!")
    elif (pilihan_player == "gunting" and pilihan_bot == "kertas") or \
         (pilihan_player == "batu" and pilihan_bot == "gunting") or \
         (pilihan_player == "kertas" and pilihan_bot == "batu"):
        print("Selamat anda menang!")
    else:
        print("Anda kalah lawan memilih", pilihan_bot)

permainan()
