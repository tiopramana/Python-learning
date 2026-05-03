# Decorator di Python adalah pola desain (fungsi khusus) yang digunakan untuk mengubah, menambah, atau memperluas
# perilaku fungsi/metode lain secara dinamis tanpa mengubah kode sumber aslinya.


def add_topping(topping):
    def wrapper(**kwargs):
        print("*Adding a topping*")
        topping(**kwargs)

    return wrapper


def add_chocolate(topping):
    def wrapper(**kwargs):
        print("🍫")
        topping(**kwargs)

    return wrapper


@add_topping
@add_chocolate
def get_icecram(**kwargs):

    for key, value in kwargs.items():
        print(f"{key} and {value}")


get_icecram(name="tio", flavor="Vanilla")
