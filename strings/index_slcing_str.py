#Slicing and Indexing For strings
# Menggacces element dengan menggunakan simbol [] dengan operasi [mulai : akhir : langkah]

huruf = "a b c d e f"

# Index Strings

print(huruf[0])
print(huruf[2])
print(huruf[-3])

print(huruf.upper())

a = "Python"

# Huruf pertama

# Mulai dari 0 tapi sampai 3 saja
first_three = a[0:3]
print(first_three)

# Mulai dari 3 tapi sampai 6 (tergantung dari len stringnya)
last_three = a[3:6]
print(last_three)

# Mengskip huruf atau loncatan huruf 

a = "Python"

# Dimulari dari 0 dan len nya 6 dan lompatan 3 
jeda = a[0:6:3]

print(jeda)

# \n atau anggepan nya kaya br sebagai line break agar dia dibawah 
print('I hope every one enjoying the python challenge.\nDo you ?')  # line break
# \t itu untuk spasi didalam line atau kalimat
print('Days\tTopics\tExercises')

# Menggunakan List

angka = [10, 20, 30, 40, 50]
print(angka[1:4])  # Output: [20, 30, 40]
print(angka[:3])   # Output: [10, 20, 30]
print(angka[::2])  # Output: [10, 30, 50] (langkah 2)

# Properti And Metode in Strings

# Immutable Strings
# String bersifat immutable, artinya string tidak dapat diubah setelah didefinisikan. 
# Setiap operasi yang tampaknya memodifikasi string sebenarnya akan membuat string baru.

a = "Halo"

print(a[0])

#Indexed dan iterable
# String dapat diaksess Berdasarkan index

b  = "Halo"

print(b[0])
print(b[-1])

for huruf in b:
    print(huruf) 

# Length
# Digunakan untuk mengetahu panjang string\

c = "a b c d e f g h i j k l m n o p q r s t u"

print(len(c))

