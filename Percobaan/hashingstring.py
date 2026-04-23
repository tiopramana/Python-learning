import random
import string 

chars = " " + string.punctuation + string.digits + string.ascii_letters

chars = list(chars)

key = chars.copy()

random.shuffle(key)

print()
print(f"Chars of string : {chars}")
print()
print(f"Key of string : {key}")

cipher_text = input("Things you want to hashed : ")
plain_string = " "

for letter in cipher_text:
    index = key.index(letter)
    plain_string += chars[index]

print(f"Hashed text {cipher_text}")
print(f"Plain text {plain_string}")