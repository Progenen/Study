import math

class TriangleValidator:
    def __call__(self, a, b, c):
        if not (a + b > c and a + c > b and b + c > a):
            raise ValueError("Треугольник с такими сторонами не может существовать")

class Triangle:
    validator = TriangleValidator()

    def __init__(self, a, b, c):
        self.validator(a, b, c)
        self.a = a
        self.b = b
        self.c = c

    def perimeter(self):
        return self.a + self.b + self.c

    def area(self):
        s = self.perimeter() / 2  
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))

    def triangle_type(self):
        if self.a == self.b == self.c:
            return "Равносторонний"
        elif self.a == self.b or self.a == self.c or self.b == self.c:
            return "Равнобедренный"
        else:
            return "Разносторонний"

t = Triangle(32, 5, 5)
print("Тип треугольника:", t.triangle_type())
print("Периметр:", t.perimeter())
print("Площадь:", t.area())