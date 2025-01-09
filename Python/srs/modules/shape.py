import math

class Shape:
    
    def __init__(self, name):
        self.name = name  # Название фигуры
    
    def area(self):
        raise NotImplementedError("Метод должен быть переопределён в наследнике.")
    
    def perimeter(self):
        raise NotImplementedError("Метод должен быть переопределён в наследнике.")
    
    def __str__(self):
        return f"Фигура: {self.name}"