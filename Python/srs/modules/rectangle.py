from .shape import Shape

class Rectangle(Shape):
    """Класс для прямоугольника."""
    
    def __init__(self, width, height):
        super().__init__("Прямоугольник")  # Вызов конструктора родительского класса
        self.width = width  # Ширина
        self.height = height  # Высота
    
    def area(self):
        """Вычисляет площадь прямоугольника."""
        return self.width * self.height
    
    def perimeter(self):
        """Вычисляет периметр прямоугольника."""
        return 2 * (self.width + self.height)
    
    def __str__(self):
        return f"{super().__str__()}, Ширина: {self.width}, Высота: {self.height}"