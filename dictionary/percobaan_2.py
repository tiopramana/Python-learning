data = [
    {"nama" : "Budi", "Gaji" : 2000},
    {"nama" : "Joko", "Gaji" : 1500},
    {"nama" : "Andi", "Gaji" : 1000}
]

salary_list = []

gaji_tertinggi = 0
nama_tertinggi = ""
total_gaji = 0

for data in data:
    salary_list.append(data["Gaji"])
    if data["Gaji"] > gaji_tertinggi:
        gaji_tertinggi = data["Gaji"]
        nama_tertinggi = data["nama"]
    total_gaji += data["Gaji"]
print(f"Nama Gaji Tertinggi : " + str(nama_tertinggi) + " Gaji : " + str(gaji_tertinggi))
print(f"Total Gaji : " + str(total_gaji))
