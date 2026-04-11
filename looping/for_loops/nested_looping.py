# Nested loop adalah loop yang berada di dalam loop lain. 
# Nested loop digunakan untuk melakukan iterasi lebih dari satu kali.



# pilihan = int(input("Masukkan pilihan: "))
# bentuk = input("Masukkan bentuk: ")

# for i in range (1, pilihan + 1):
#     gap = " " * (pilihan - i)
#     star = bentuk * (2 * i - 1)
#     print(gap + star)

buah = ["apel", "mangga", "jeruk"]

for i in buah:
    if i:
        print("Pastikan ada buah", i)
    print("Ada \n")

row = int(input("Masukan Baris: "))
col = int(input("Masukan Kolom: "))
symbol = input("Masukan Symbol: ")

for x in range(row):
    for y in range(col):
        print(symbol, end='')
    print()