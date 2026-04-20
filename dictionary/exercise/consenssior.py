# Membuat system ticket 

menu = {
    "popcorn": 6.00,
    "pizza" : 10.00,
    "fries" : 5.00,
    "chips" : 2.00,
    "soda" : 3.00,
    "lemonande" : 4.00,
}

cart = []
total = 0

for key, value in menu.items():
    print(f"{key:10} for ${value:.2f}")
    print()

while True:
    food = input("Masukan menu dari 1-6 : ").lower()
    if food == "q":
        break
    elif menu.get(food) is not None:
        cart.append(food)

for price in cart:
    total += menu.get(price)
    print(price, end=" ")

print()
print(total)