import random as r

class  Square:

    def __init__(self):
        self.side_length = r.randint(1,10)
        print('Длинна стороны квадрата:', self.side_length)

    def perimeter(self):
        print('Периметр квадрата:', self.side_length * 4)
    def area(self):
        print('Площадь квадрата:', self.side_length * self.side_length)
    def diagonal(self):
        print('Диагональ квдрата:', self.side_length * 2 ** 0.5)

mySquare = Square()

mySquare.perimeter()
mySquare.area()
mySquare.diagonal()