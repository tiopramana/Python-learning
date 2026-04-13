# Function dalam python menggunakan def nama ()

def data(username, age, height, bodyweight):
    print(f"Nama saya: {username}")
    print(f"Umur saya: {age}")
    print(f"Tinggi saya: {height}")
    print(f"Bodyweight: {bodyweight}")

data("tio", 18, 180, 89 )

# Math function calculation

def tambah(angka1, angka2):
    data = angka1 + angka2
    return data

def kurang(angka1, angka2):
    data = angka1 + angka2
    return data

def perkalian(angka1, angka2):
    data = angka1 * angka2
    return data

def devide(angka1, angka2):
    data = angka1 // angka2
    return data

print(tambah(1, 5))
print(kurang(6, 10))
print(perkalian(2, 10))
print(devide(10, 2))

def name (first, second):
    first = first.capitalize()
    second = second.capitalize()
    return first + " " + second

full_name = name("tio", "pramana")

print(full_name)