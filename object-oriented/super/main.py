# super() adalah Dalam Python, fungsi super() digunakan untuk memanggil metode dari 
# kelas induk (superclass) di dalam kelas anak (subclass). Ini memungkinkan untuk memperluas 
# atau menimpa metode yang diwariskan sambil tetap menggunakan fungsionalitas kelas induk.

class Shape:
    def __init__(self, color, is_filled):
        self.color = color
        self.is_filled = is_filled

    def describeShape(self):
        print(f"The color of the shape is {self.color} and {'filled' if self.is_filled else 'not filled'}")

class Circle(Shape):
    def __init__(self, color, is_filled, radius):
        super().__init__(color, is_filled)
        self.radius = radius

    def describeShape(self):
        print(f"It is a circle with an area {3.14 * self.radius ** 2}cm^2")
        super().describeShape()

class Square(Shape):
    def __init__(self, color, is_filled, width):
        super().__init__(color, is_filled)
        self.width = width

    def describeShape(self):
        print(f"It is a square with an area {self.width * self.width }cm^2")
        super().describeShape()

class Triangle(Shape):
    def __init__(self, color, is_filled, width, height):
        super().__init__(color, is_filled)
        self.width = width
        self.height = height

    def describeShape(self):
        print(f"It is a triangle with an area {self.width * self.height / 2 }cm^2")
        super().describeShape()

circle = Circle(color="Green", is_filled=True, radius=5)
square = Square(color="Yellow", is_filled=False, width=30)
triangle = Triangle(color="Black", is_filled=True, width=20, height=10)

circle.describeShape()
print()
square.describeShape()
print()
triangle.describeShape()

# print(f"The color of the shape is {circle.color} and is it filled? {circle.is_filled} the radius is {circle.radius}")
# print(f"The color of the shape is {square.color} and is it filled? {square.is_filled} the radius is {square.width}")
# print(f"The color of the shape is {triangle.color} and is it filled? {triangle.is_filled} the width is {triangle.width} and height {triangle.height}")

