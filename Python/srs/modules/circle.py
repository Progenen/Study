from .shape import Shape

class Circle(Shape):
    """Класс для круга."""
    
    def __init__(self, radius):
        super().__init__("Круг")  # Вызов конструктора родительского класса
        self.radius = radius  # Радиус круга
    
    def area(self):
        """Вычисляет площадь круга."""
        return math.pi * self.radius ** 2
    
    def perimeter(self):
        """Вычисляет периметр (длину окружности)."""
        return 2 * math.pi * self.radius
    
    def __str__(self):
        """Переопределение метода для более детального описания."""
        return f"{super().__str__()}, Радиус: {self.radius}"