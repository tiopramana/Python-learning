# If jika benar Elif Jika Masih DiPerhitungkan else tidak ada

umur = int(input("Umur saya adalah : "))

def kakulasi_umur():
    if umur <= 10:
        print("Wow Kamu masih bocah")
    elif umur <= 15:
        print("Wow Kamu suda Remaah")
    elif umur >= 20:
        print("Maaf Kamu bukan dimasa Nyaman lagi")
    else:
        print("Kamu Tua Ga Usah Ikutkan")
        return 
kakulasi_umur()