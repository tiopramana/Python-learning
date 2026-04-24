# Pewarisan memungkinkan kita untuk mendefinisikan sebuah kelas yang mewarisi 
# semua metode dan properti dari kelas lain.
# Kelas induk adalah kelas yang diwarisi, juga disebut kelas dasar.
# Kelas anak adalah kelas yang mewarisi dari kelas lain, juga disebut kelas turunan.

class Person:

    def __init__(self, name, height):
        self.name = name
        self.school = True

    def hadir(self):
        print(f"Siswa bernama {self.name} sudah disekolah!")
    
    def telat(self):
        print(f"Siswa bername {self.name} terlambat")

class Student(Person):
    
    def alasanTidakTelat(self):
        print("Bangun Pagi!")

    def alasanTelat(self):
        print("Tidak bangun pagi!")

data1 = Student("Tio pramana", 180)
data2 = Student("Vidiya Dewi", 160)

print()
data1.hadir()
data1.alasanTidakTelat()
print()
data2.telat()
data2.alasanTelat()