# Percobaan 2 penjualan barang pada toko

item = input("Apa Barang Yang Kamu Beli Di Toko ini : ")

if item == "Kondom":
    harga = 50.000
    print(f"Harga Per Item : {harga}")
    yang_dibeli = (int(input("Berapa yang ingin ada beli : ")))
    total = harga * yang_dibeli
    print(f"Total : {total}")

elif item == "Jajan":
    harga = 30.000
    print(f"Harga Per Item : {harga}")
    yang_dibeli = (int(input("Berapa yang ingin ada beli : ")))
    total = harga * yang_dibeli
    print(f"Total : {total}")

else:
    print("Barang Tidak Terstock")
