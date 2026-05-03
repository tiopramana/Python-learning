# @property Tujuannya adalah mengubah sebuah method agar bisa diakses seolah-olah
#  ia adalah atribut (variabel biasa).


class Rectrangel:
    def __init__(self, width, height):
        self._width = width
        self._height = height

    @property  # Ini property dari width
    def width(self):
        return f"The Width of rectrangle is {self._width:.1f}cm"

    @property  # Ini property dari height
    def height(self):
        return f"The height of rectrangle is {self._height:.1f}cm"

    @width.setter  # Ini penggunaan nya yang dimana menjalankan sistem diluar variable internal
    def new_width(self, new_width):
        if new_width > 0:
            self._width = new_width
        else:
            print("Width must greater than 0")

    @height.setter  # Ini penggunaan nya yang dimana menjalankan sistem diluar variable internal
    def new_height(self, new_height):
        if new_height > 0:
            self._height = new_height
        else:
            print("Height must greater than 0")

    @width.deleter  # Ini penggunaan nya yang dimana menjalankan sistem diluar variable internal
    def new_del_width(self):
        del self._width
        print("The new width has been deleted")

    @height.deleter  # Ini penggunaan nya yang dimana menjalankan sistem diluar variable internal
    def new_del_height(self):
        del self._height
        print("New height was been deleted")


rectrangle = Rectrangel(3, 4)

rectrangle.new_width = 10
rectrangle.new_height = 10

del rectrangle.new_del_width
del rectrangle.new_del_height
