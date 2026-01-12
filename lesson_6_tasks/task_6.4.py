class Rectangle:
    def __init__ (self, width:float, height:float):
        self.__width = width
        self.__height = height

    @property
    def width(self) -> float:
        return self.__width

    @width.setter
    def width(self, value: float) -> None:
        if value > 0:
            self.__width = value
        else:
            print("Ошибка: Значение должно быть больше 0!")

    @property
    def height(self) -> float:
        return self.__height

    @height.setter
    def height(self, value: float) -> None:
        if value > 0:
            self.__height = value
        else:
            print("Ошибка: Значение должно быть больше 0!")


    def __str__(self) -> str:
        return f"Прямоугольник {self.width} x {self.height}"

    def area(self):
        return self.width*self.height

    def __add__(self, other):
        return self.area()+other.area()


rect1 = Rectangle(5, 4)
rect2 = Rectangle(10, 2)
print(rect1)
print(rect1 + rect2)
rect1.width = -5