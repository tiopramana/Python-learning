# Iterable is an object/collection can be return its element one at a time
# Allowing edit or change in loop 

# Tuples
number = (1,2,3,4,5)

for x in number:
    print(x, end=" ")
print()

# Array / list
fruits = ["Apel", "Strawberry", "Mangga", "Nanas"]

for x in fruits:
    print(x, end=" ")
print()

# Set
char = {"Tio Pramana"}

for x in char:
    print(x, end=" ")
print()

# Dictionary

my_dict = {"A" : 1, "B" : 2, "C": 3}

for x, y in my_dict.items():
    print(x, y)
print()