buah = ["Mangga", "Jeruk", "Strawberry", "Nanas"]
sayur = ["Brokoli", "Sawi", "Kol", "Wortel"]
daging = ["Ayam", "Unta", "Anjing", "Kelinci"]

pasar = [buah, sayur, daging]

supermarket = [
    ["Mangga", "Jeruk", "Strawberry", "Nanas"],
    ["Brokoli", "Sawi", "Kol", "Wortel"],
    ["Ayam", "Unta", "Anjing", "Kelinci"],
]

for i in supermarket:
    for food in i:
        print(food, end=" ", )
    print()

# Creating num pad

num_pad = ((1,2,3),
           (4,5,6),
           (7,8,9),
           ("*",0,"="))

for i in num_pad:
    for angka in i:
        print(angka, end=" ")
    print()