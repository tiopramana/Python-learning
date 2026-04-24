# Class variable adalah variable yang dapat di shared among all instances of a class
# untuk digunakan diluar constructor
# agar kita dapat mengshared data among all object have been created from the class

class Student:

    year = 2024
    student_num = 0

    def __init__(self, name, age):
        self.name = name
        self.age  = age
        Student.student_num += 1

student1 = Student("Tio pramana", 18)
student2 = Student("Vidiya Dewi", 19)
student3 = Student("Selamat", 45)
student4 = Student("Pria Solo", 60)

print("="*48)

print(f"The graduating class of year {Student.year} has {Student.student_num} stundent\n")
print(student1.name, student1.age)
print(student2.name, student2.age)
print(student3.name, student3.age)
print(student4.name, student4.age)

print("="*48)

