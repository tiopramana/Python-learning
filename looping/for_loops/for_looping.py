# for loops = For loops adalah salah satu cara untuk melakukan perulangan (iterasi) dalam pemrograman.
#       Berdasarkan tipe data string, list, tuple, set, dan dictionary.

#for item in collection:
    # kode yang akan dijalankan berulang

for x in range(1, 5):
    if x == 3:
        continue
    else:
        print(x)




for i in range(1, 5 + 1):
    spaces = " " * (5 - i)
    hashes = "*" * (2 * i - 1)
    print(spaces + hashes)

