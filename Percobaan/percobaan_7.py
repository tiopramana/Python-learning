a = [1, 2]  # Changed tuple to list
a[0] += 1

print(a)

a = 2
b = 3
c = 4

if a > b:
    if a > c:
        print(a)
    else:
        print("ABC")
elif a < b:
    if a > c:
        print("AC")
    print("BCA")
else:
    print("CAB")


for x in range(10):
  if x % 2 == 0:
    continue
  print(x)

for i in range(5): print("Hello")

x = 5
y = 10
print(x > 6 or y < 15)

x = 10
y = 5
z = 15

if x > y and x > z:
    print("X terbesar")
elif y > x and y > z:
    print("Y terbesar")
else:
    print("Z terbesar")

angka = [1, 2, 3, 4, 5]
hasil = 0
for x in angka:
    if x % 2 != 0:
        hasil += x
print(hasil)
