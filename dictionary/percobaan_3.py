# Data input
input_data = {
    "Indomaret": {
        "Ayam": 30000,
        "Sayur": 15000,
        "Buah": 20000,
        "Ikan": 22000
    },
    "Alfamart": {
        "Ayam": 25000,
        "Sayur": 12000,
        "Buah": 30000,
        "Ikan": 25000
    }
}

input_data_2 = {
    "Ayam": 2,
    "Sayur": 1,
    "Ikan": 1
}


cheapest_prices = {}
for item in input_data_2.keys():

    indomaret_price = input_data["Indomaret"].get(item, float('inf'))  # Gunakan inf jika item tidak ada
    alfamart_price = input_data["Alfamart"].get(item, float('inf'))
    

    cheapest_prices[item] = min(indomaret_price, alfamart_price)


total_cost = 0
for item, quantity in input_data_2.items():
    total_cost += cheapest_prices[item] * quantity

# Output
print("Harga termurah untuk setiap item:")
for item, price in cheapest_prices.items():
    print(f"{item}: {price * 2}")
print(f"\nTotal biaya: {total_cost}")
