# List
# List adalah tipe data di Python yang digunakan untuk menyimpan koleksi elemen dalam urutan tertentu. Elemen dalam list dapat diubah (mutable).

# Ciri-ciri:

# Mutable (bisa diubah, seperti menambah, menghapus, atau memodifikasi elemen).
# Dapat menyimpan elemen dengan tipe data yang berbeda.
# Mempertahankan urutan elemen.
# Menggunakan tanda kurung siku [].


# List atau array yang bisa digunakan sebagai tempat data

lst = list()

empty_list = list()

print(len(empty_list))

buah = ["apel", "jeruk", "mangga", "lemon"]
vegetables = ['Tomato', 'Potato', 'Cabbage','Onion', 'Carrot']
animal_products = ['milk', 'meat', 'butter', 'yoghurt']  
web_techs = ['HTML', 'CSS', 'JS', 'React','Redux', 'Node', 'MongDB']
countries = ['Finland', 'Estonia', 'Denmark', 'Sweden', 'Norway']

# Output of the list or array
print("Jenis Buah : " + ", ".join(buah))
print('Number of fruits:', len(buah))
print('Vegetables:', vegetables)
print('Number of vegetables:', len(vegetables))
print('Animal products:',animal_products)
print('Number of animal products:', len(animal_products))
print('Web technologies:', web_techs)
print('Number of web technologies:', len(web_techs))
print('Countries:', countries)
print('Number of countries:', len(countries))

print(buah[0:3])

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
# print(help(buah))


print(len(buah))

print( "apel" in buah)

print(buah.append("lolok"))

print(buah)
