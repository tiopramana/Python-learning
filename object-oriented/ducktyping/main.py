# Duck typing adalah jalan lain untuk mendapatkan polymorphism selain inheritance
# atau pewarisan dan object harus minimum memiliki attributes atau method 

# Slogan
# "If it a duck and quacks like a duck, it must be a duck"

class Animal:
    alive = True

class Dog(Animal):
    def speak(self):
        print("Anjay")

class Cat(Animal):
    def speak(self):
        print("WIAW")

class Car:

    alive = False

    def speak(self):
        print("HONK!")

animal = [Dog(), Cat(), Car()]

for ani in animal:
    ani.speak()
    print(ani.alive)