# Dictionary

worker = {
    "name": "tio",
    "job": "janitor",
    "division": 5,
}

keys = worker.keys()
value = worker.values()

print(keys, "And Values", value)

# print(help(worker))
update = worker.update({"name": "selamat"})
worker.pop("division")  # Hanya digunakan untuk keys

for key, values in worker.items():
    print(f"every key values {key} and {value}")
