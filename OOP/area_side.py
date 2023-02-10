import math


class Square:

    def __init__(self, side):
        self._side = side
        self._area = self._side ** 2
        self._perimeter = self._side * 4
        self._diagonal = self._side * math.sqrt(2)

    def get_side(self):
        return self._side

    def get_perimeter(self):
        return self._perimeter

    def get_area(self):
        return self._area

    def get_diagonal(self):
        return self._diagonal

    def set_side(self, new_length):
        self._side = new_length
        self._area = self._side ** 2
        self._perimeter = self._side * 4
        self._diagonal = self._side * math.sqrt(2)

    def set_perimeter(self, new_length):
        self._perimeter = new_length
        self._side = new_length / 4
        self._area = (new_length / 4) ** 2
        self._diagonal = (new_length / 4) * math.sqrt(2)

    def set_diagonal(self, new_length):
        self._diagonal = new_length
        self._side = new_length / math.sqrt(2)
        self._area = (new_length / math.sqrt(2)) ** 2
        self._perimeter = (new_length / math.sqrt(2)) * 4

    def set_area(self, new_area):
        self._area = new_area
        self._side = math.sqrt(new_area)
        self._diagonal = math.sqrt(new_area) * math.sqrt(2)
        self._perimeter = math.sqrt(new_area) * 4


x = Square(4)
print(x.get_area())
print(x.get_diagonal())
print(x.get_perimeter())
print(x.set_area(9))
print(x.get_side())