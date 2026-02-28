a = [[1, 2, 3], [2, 3, 4], [3, 4, 5]]
result = []

for i in a:
    z = 0
    for j in i:
        z += j
    result.append(z)

print(result)

