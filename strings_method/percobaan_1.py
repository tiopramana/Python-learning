nama = input("Masukan Nama Anda : ").strip()

if len(nama) > 12:
    print("Masukan Nama Anda Tidak Bisa Lebih Dari 12 Characters")
elif not nama.find(' ') == -1:
    print("Masukan Nama Anda Tanpa Ruang Kosong")
elif not nama.isalpha():
    print("Masukan Nama Anda tanpa angka!")
else:
    print(f"Hallo {nama}")