# List
# List adalah tipe data di Python yang digunakan untuk menyimpan koleksi elemen dalam urutan tertentu. Elemen dalam list dapat diubah (mutable).

# Ciri-ciri:

# Mutable (bisa diubah, seperti menambah, menghapus, atau memodifikasi elemen).
# Dapat menyimpan elemen dengan tipe data yang berbeda.
# Mempertahankan urutan elemen.
# Menggunakan tanda kurung siku [].

buah = ["apel", "jeruk", "mangga", "lemon"]

# Membuat list
my_list = [1, 2, 3, "Python", 4.5]

# Akses elemen
print(my_list[0])  # Output: 1

# Menambah elemen
my_list.append(6)
print(my_list)  # Output: [1, 2, 3, "Python", 4.5, 6]

# Mengubah elemen
my_list[1] = "Changed"
print(my_list)  # Output: [1, "Changed", 3, "Python", 4.5, 6]

#print(dir(buah))
#print(help(buah))