# exception adalah step logika yang terbagi menjadi 3 yaitu (ZeroDivisionError(tanpa error), Value(Error atau catch dalam js),
# dan Value Error atau finally sebagai release!) dengan konsep 1. try, 2. except, dan finally


try:
    data = int(input("Masukan angka : "))
    for i in range(1, 1000):
        i += 1

        if i % 2:
            print("Odd")
        else:
            print("Rege")

        print(i, end=" ")

except ValueError:
    print(ValueError)
    print("Showing what the Value of the error!")

except TypeError:
    print(TypeError)
    print("Showing what the Type of the error!")

except Exception:
    print(Exception)
    print("Showing somethign errors!")

finally:
    print("Kiw")
    print("For releasing after do the try and except")
