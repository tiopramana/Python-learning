umur = int(input("Masukan Nomor Kelas Anda : "))

while umur < 0:
    print("Tidak Ada umur dibawah 0 Kecuali Belum Lahir")
    int(input("Masukan umur mu lagi : "))
print(f"Wow Umur Kamu {umur}".format(umur))

