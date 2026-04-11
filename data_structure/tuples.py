# Tuple adalah tipe data yang digunakan untuk menyimpan beberapa item dalam satu variabel.

t = ("apel", "jeruk", "mangga", "lemon", "apel", "lemon", "apel")

print(t.count("apel"))

print(t.index("apel"))

print("apel" in t)

# print(dir(t))

# print(help(t))

for i in t:
    print(i)
