import math

class Shape:

    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color

    def describe(self):
        return f"Figura o środku w punkcie {(self.x, self.y)} i colorze {self.color}"

    def distance(self, other):
        return math.sqrt((self.x + other.x) ** 2 + (self.y + other.y) ** 2)

    def __str__(self):
        return f"Figura koloru {self.color} o środku w punkcie {(self.x, self.y)}"


x = Shape(5, 5, "zielony")
k = Shape(2, 3, "żółty")
print(x.describe())
print(x)
print(x.distance(k))