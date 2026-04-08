# Metode Metode dalam menggunakan string pada python 

# =================================================================
# Methods Case

# str.lower() berguna untuk mengubah huruf menjadi kecil semua
print(("HALLO").lower()) 

# str.upper() berguna untuk mengubah huruf menjadi besar semua
print(("hello").upper())

# str.capitalize() berguna untuk mengubah huruf depan menjadi capital
print(("heLLo").capitalize())

# str.title() berguna untuk mengubah setiap huruf depan menjadi capital
print(("hello world").title())

# str.swapcase() berguna untuk menukar huruf yang besar menjadi kecil diubah ke huruf kecil
print(("heLLo").swapcase())

# =================================================================
# Alignment method

# str.center(width) mengatur posisi dalam string mengatur lebarnya
print(("Hello World").center(10))

# str.ljust(width): mengatur posisi bagian width kiri
print(("Hello World").ljust(10))

# str.rjust(width): Right-aligns the string in a field of given width
print(("Hello World").rjust(10))

# =================================================================
# Split dan Join

# str.split(sep): mengatur agar str bisa memiliki jarak dengan simbol tertentu
print(("a,b,c").split(",")) 

# str.rsplit(sep): Melakukan jarak pada bagian kanan
print(("a,b,c").rsplit(",", 1)) 

# str.splitlines(): Splits str menjadi garis lurus
print(("garis1\ngaris2").splitlines())

# str.join(iterable): Joins elements yang dimasuka kedalam satu strings
print((",").join(['a', 'b', 'c']))

# =================================================================

# Mengecek Karakter pada str apa kah benar ato salah / True or False

# str.isalpha(): memberikan hasil true jika mengecek huruf pada str alfabet
print(("Hellow").isalpha())

# str.isdigit(): Mengecek str apakah mengandung angka atau digit
print(("123").isdigit())

# str.isalnum(): Mengecek apakah str mengandung text dan digit
print(("Hello123").isalnum())

# str.isspace: mengecek apakah str itu ruang kosong
print((' ').isspace())

# str.count untuk menghitung jumlah huruf
print("thirty days of python".count("o"))

# ==================================================================
# str.strip(): Menghapus space yang ada
print((" HEllo ").strip())

# str.lstrip(): Menghapus space pada bagian kiri
print((" Hello").lstrip())

# str.rstrip(): Menghapus space pada bagian kanan
print(("Hello ").rstrip())










