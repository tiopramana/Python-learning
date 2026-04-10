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

# Unpacking List Packet 

# Contoh 1
fruit = ['mangga', 'jeruk', 'apel', 'nanas']
first_fruit, second_fruit, *rest = fruit

print(first_fruit)
print(second_fruit)
print(rest)

# Contoh 2

list = [1,2,3,4,5,6,7,8,9,10]
first, second, *rest, end = list

print(first)
print(second)
print(rest)
print(end)

# Contoh 3

countries = ['Germany', 'France','Belgium','Sweden','Denmark','Finland','Norway','Iceland','Estonia']
gr, fr, be, sw, *sisa, ic, es, = countries

print(gr)
print(fr)
print(be)
print(sw)
print(sisa)
print(ic)
print(es)

# Slicing item from list 
president = ['Jokowi', 'Prabowow', 'Anies', 'Ganjar']
print(president[0:4]) # Memprint array atau list dari index 0 -> 4 yaitu semuanya

print(president[0:]) # Memprint arry dari data 0 seterus nya hingga akhir

print(president[1:2]) # Memprint array yang melewati index 1 dan 3 4

print(president[::2]) # Step locatan data 2 kali dari 1 -> 2 -> 3 -> 4

# Menggunakan negatif 

fruits = ['banana', 'orange', 'mango', 'lemon']
print(fruits[-4:]) # Memprint array atau list dari index 0 -> 4 yaitu semuanya

print(fruits[-3:-1]) # Tidak memprint index pertama dan terakhir

print(fruits[-3:]) # Print yang dimulai dari index melewati -4 atau yang pertama

print(fruits[::-1]) # Membalik list nya dari -4 -3 -2 -1 menjadi -1 -2 -3 -4 begitu

