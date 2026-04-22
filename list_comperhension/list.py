# List comprehension adalah pilihan pembuatan list yang menggunakan
# Loop tradisional dan menggunakan data yang sudah ada

double = []

for i in range (1, 11):
    double.append(i ** 2)

print(double)

double = [x ** 2 for x in range (1,11)]
print(double)


fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

fresh_fruit = []

for i in fruits:
    fresh_fruit.append(i)

print(fresh_fruit)

fruit_char = [x[0].upper() for x in fruits]

print(fruit_char)

numbers = [1, 2, -3, 4, -5, 6, -7]

for i in numbers:
    if i > 0:
        print(f"Number is positive {i}")
    elif i < 0:
        print(f"Number is negative {i}")
    elif i % 2 == 0:
        print(f"Number is even {i}")
    else:{
        print(f"Number error! {i}")
    }
        
positive_number = [i for i in numbers if i >= 0]
negative_number = [i for i in numbers if i < 0]
even_number = [i for i in numbers if i % 2 == 0]
odd_number = [i for i in numbers if i % 2 == 1]
print(positive_number)
print(negative_number)
print(even_number)
print(odd_number)

data = [1,2,3,4,5,6,7,8]
angka = []

for i in data:
    angka.append(i)
print(angka)