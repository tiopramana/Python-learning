# *args and **kwargs is by default of a function must be
# called with the correct number of arguments
# However, sometimes you may not know how many arguments that will be passed into your function.
# *args and **kwargs allow functions to accept a unknown number of arguments.

# problem

# def a (x, y):
#     return x + y

# print(a(1,2,3))

# Atbitary Arguments *args for unkeyword of arguments


def a(*args):
    total = 0
    for i in args:
        total += i
    return total


print(a(1, 2, 3))


def name_people(*args):
    for i in args:
        print(i, end=" ")


name_people("Tio", "Selamat", "Vivi", "\n")

# Keyword arguments **kwargs used for keyword of arguments


def keyword_argu(**kwargs):
    for key, value in kwargs.items():
        print(key, value, end=" ")
    print()


keyword_argu(title="Anjay", last="Mabar", end="propesional")

# Using *args and **kwargs in one of function


def shipping_label(*args, **kwargs):
    for x in args:
        print(x, end=" ")
        for key, value in kwargs.items():
            print(key, value, end=" ")
        print()


shipping_label(
    "Dr.TioPramana",
    age=20,
    rumah="Disana deh",
)
