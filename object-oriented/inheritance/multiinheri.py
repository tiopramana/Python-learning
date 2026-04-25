# Multiple Inheritance (pewarisan banyak parent) yang dimana satu class
# Akan mewarisi lebih dari satu class

# Multilevel inheritance (pewarin secara turun menurun) yang dimana class itu dia akan
# menurunkan kelevel level seterus nya begitu berantai

# Multiple inheritance

class Animal:

    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"This {self.name} need to eat!")

    def sleep(self):
        print(f"This {self.name} need to sleep!")

class Herbivore(Animal):
    def herb(self):
        print("This animal just eaten an vegies!")

class Carnivore(Animal):
    def carni(self):
        print("This animal just eaten an meat!")

class Tortoes(Herbivore):
    pass

class Snake(Carnivore):
    pass

class Fish(Herbivore, Carnivore):
    pass

tortoes = Tortoes("Gokil")
snake = Snake("Likog")
fish = Fish("Fih")

tortoes.herb()
snake.carni()
fish.carni()


tortoes.eat()
snake.sleep()

# Multilevel contoh agar lebih lengkap

class Kakek:
    def kakek(self):
        print("Saya kakek")

class Ayah(Kakek):
    def ayah(self):
        print("Saya Ayah!")

class Anak(Ayah):
    def anak(self):
        print("Saya anak")

anak = Anak()

anak.kakek()
anak.ayah()
anak.anak()