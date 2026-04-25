# Polymorphism adalah Greek word yang memiliki banyak form atau faces
# Poly = many
# Morp = Form

# Ada dua cara dalam mendapatkan polymorphism
# 1. Inheritance atau warisan dari parent class atau class induk
# 2. Duck Typing adalah object yang harus memiliki attributes atau methods

from abc import ABC, abstractmethod 

class Shape:
    
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

class Square(Shape):
    
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side * self.side

class Triangle(Shape):
    
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return self.base * self.height * 0.5

class Pizza(Circle):
    def __init__(self, topping, radius):
        super().__init__(radius)
        self.topping = topping

    def areaPizza(self):
        print(f"Pizza with {self.topping} have an radius {self.radius}")
        return

shape = [Circle(10), Square(20), Triangle(15, 10), Pizza("Lolokroni", 15)]

for i in shape:
    print(f"{i.area()}cm^2")
