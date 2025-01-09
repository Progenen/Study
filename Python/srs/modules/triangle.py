from .shape import Shape

class Triangle(Shape):
    """Класс для треугольника."""
    
    def __init__(self, side_a, side_b, side_c):
        super().__init__("Треугольник")  # Вызов конструктора родительского класса
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c
    
    def area(self):
        """Вычисляет площадь треугольника (по формуле Герона)."""
        s = self.perimeter() / 2
        return math.sqrt(s * (s - self.side_a) * (s - self.side_b) * (s - self.side_c))
    
    def perimeter(self):
        """Вычисляет периметр треугольника."""
        return self.side_a + self.side_b + self.side_c