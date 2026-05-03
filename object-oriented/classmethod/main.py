# Class method adalah metode yang digunakan untuk mengakses tidak memerlukan object
# dia langsung berkerja dengan class atau cls

import math

class Siswa:
    total = 0

    @classmethod
    def TambahSiswa(cls):
        cls.total += 1

Siswa.TambahSiswa()
Siswa.TambahSiswa()

print(Siswa.total)

# Contoh dari Bro Code

class Student:

    count = 0
    total_gpa = 0

    def __init__(self, name, gpa):
        self.name = name
        self.gpa = gpa
        Student.count += 1
        Student.total_gpa += gpa

    def get_student(self):
        print(f"The name is {self.name} and the gpa is {self.gpa}")

    @classmethod
    def get_count(cls):
        return f"Total of count {cls.count}"
    
    @classmethod
    def count_gpa(cls):
        if cls.count == 0:
            return 0
        else:
            counting = cls.total_gpa / cls.count
            average = math.ceil(counting)
            print(f"{cls.count} of student is average is {average}")

student_1 = Student("Tio", 3.5)
student_2 = Student("Lele", 4)
student_3 = Student("Vivi", 4)

print(student_1.get_student())
print(student_2.count_gpa())