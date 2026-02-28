# Penggunaan Aritmatika Pada python
3
# rumah = orang_dirumah + 1 #Tambah
# orang_dirumah += 1

# rumah = orang_dirumah - 2 #Kurang
# orang_dirumah -= 2

# rumah = orang_dirumah * 3 #Kali
# orang_dirumah *= 3

# rumah = orang_dirumah / 4 #Bagi
# orang_dirumah /= 4

# rumah = orang_dirumah ** 5 #Pangkat
# orang_dirumah **= 5

# rumah = orang_dirumah // 4.3 mengganti le bilangan absolute

# orang_disana = orang % 10



orang_dirumah = int(input("Ada Berapa Orang kah Dirumah : "))

if orang_dirumah == 3:
    orang_dirumah += 2
    print(f"orang_dirumah ada : {orang_dirumah}")
elif orang_dirumah == 1:
    orang_dirumah += 4
    print(f"orang_dirumah ada : {orang_dirumah}")
else:
    print("Ga da Orang Dirumah")
