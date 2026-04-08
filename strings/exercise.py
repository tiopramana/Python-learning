a = "Thirty", "Days", "Of", "Python"
b = ' '.join(a)
print(b)    

company = "Coding","For","All"

# name = " ".join(company)

name = " ".join(company).replace("Coding", "Python")

print(name)

print(len(name))

print(name.upper())

print(name.lower())

print(name.capitalize())

print(name.title())

print(name.swapcase())

# Cut(slice) out the first word of Coding For All string.
print(name.split()[1:3])

# Check if Coding For All string contains a word Coding using the method index, find or other methods.
print("Coding" in name)

# Replace the word coding in the string 'Coding For All' to Python.
print(name.replace("Coding", "Python"))

# Change "Python for Everyone" to "Python for All" using the replace method or other methods.
print(name.replace("Python For All", "Python For Everyone"))

# Split the string 'Coding For All' using space as the separator (split()) .
print(" ".join(company).split())

# "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" split the string at the comma.
company_tech = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"

print(company_tech.split(","))

# What is the character at index 0 in the string Coding For All.
print(name[0])

print(name[-1])

print(name[10])

acronym_1 = "Python For Everyone"
x = acronym_1.split()

y = "".join(x[0].upper() for x in x)

print(y)

acronym_2 = "Coding For All"

x = acronym_2.split()

y = "".join(x[0].upper() for x in x)

print(y)

search_index_1 = "Coding For All"

# Use index to determine the position of the first occurrence of C in Coding For All.
print(search_index_1.find("C"))

# Use index to determine the position of the first occurrence of F in Coding For All.
print(search_index_1.find("F"))

search_rfind = "Coding For All People"
print(search_rfind.rfind("l"))

sentence = "You cannot end a sentence with because because because is a conjunction"

print(sentence.find("because"))

print(sentence.rfind("because"))

print(sentence.index("because"))

print(sentence.rindex("because"))

print(sentence[31:54])

does = "Coding For All"

print(does.startswith("Coding"))


print(does.startswith("coding"))

space = " Coding For All  "

print(space.isidentifier())

var1 = "30DaysOfPython"
var2 = "thirty_days_of_python"

print(var1.isidentifier())

print(var2.isidentifier())

pylib = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']


print(" # ".join(pylib))


print("I am enjoying this challenge.\nI just wonder what is next.")

print("Name \t Age \t Country \t City")
print("Tio \t 250 \t Indonesia \t Denpasar")


radius = int(input("Masukan Radius Lingkaran : "))
pi = 3.14

penyelesain = pi * radius ** 2

hasil = "The Area of circle with radius {} is {} meters square".format(radius, penyelesain)

print(hasil)



# 8 + 6 = 14
# 8 - 6 = 2
# 8 * 6 = 48
# 8 / 6 = 1.33
# 8 % 6 = 2
# 8 // 6 = 1
# 8 ** 6 = 262144