# Membership operator is used for test wheter a value or variable
# is found in squence of (string, list, tuple, set, or dictionary)

# in
# not in
word = "APPLE"

print(word)
tebakan = input("Masukan huruf: ")

if tebakan not in word:
    print("Tidak ada huruf", tebakan)
else:
    print("Tebakan benar", tebakan in word)

# List, set, tuple membership operators

student = {"Tio", "Vivi", "Jamson", "Bas"}

student_name = input("Enter student name: ")

if student_name not in student:
    print("No student named", student)
else:
    print("Student is", student_name in student)

# Dictionary membership operator

dict_student = {"Tio": 100,
                "Vivi": 91,
                "Bas": 92,}

dict_student_name = input("Masukan nama: ")

if dict_student_name in dict_student:
    print(f"Student with {dict_student_name} the score is {dict_student[dict_student_name]}")
else:{
    print(f"Not found a student with name {dict_student_name} and the score {dict_student[dict_student_name]}")
}       