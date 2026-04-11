input = [800,600,400,200]

compared_input = [500, 200,400]

hasil = []

for i in range(len(input)):
    if input[i] in compared_input:
        hasil.append(1)
    else:
        hasil.append(0)
print(hasil)