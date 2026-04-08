import math

multipication_strings = """Lorem Ipsum is placeholder text commonly used in design and publishing to demonstrate graphic elements (fonts, layout) without using meaningful content. Derived from Cicero's 45 BC work in Latin, it has been the industry standard since the 1500s. It prevents viewers from focusing on text, allowing focus on"""

print(len(multipication_strings))

# Unpacking characters

x = "Python"

a, b, c, d, e, f, = x
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)

# Format Strings yang digunakan untuk membuat output secara rapi 

nama = "Tio"
umur= 20
hobi= "Mancing"

a = "Nama pria tersebut {} dengan umur {}, dan hobi {}".format(nama, umur, hobi)

print(a)

radius = 14
pi = math.pi
area = pi  # radius ## 2
result = 'The area of circle with {} is {}'.format(str(radius), str(area))
print(result)  # The area of circle with 10 is 314.0