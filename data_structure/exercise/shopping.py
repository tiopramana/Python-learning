# Exercise creating shopping cart system

food = []
price = []
total = 0

while True:
    foods = input("Enter foods you wanna eat (q for quit): ")

    if foods.lower() == "q":
        break
    else: 
        prices = float(input(f"Enter the price of the food you order: "))
        food.append(foods)
        price.append(prices)
    for i in food:
        print(i, end=" ")
    for a in price:
        total += a
print(f"total of {food} is {total}")