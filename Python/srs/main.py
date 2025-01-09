from modules.circle import Circle
from modules.rectangle import Rectangle
from modules.shape import Shape
from modules.triangle import Triangle

def decorator(func):
    def wrapper(*args, **kwargs):
        print(f"Вызов функции {func.__name__} с аргументами: {args}, {kwargs}")
        return func(*args, **kwargs)
    return wrapper

class FunctionAsObject:
    def __call__(self, shape):
        print(f"Функтор вызывает метод для: {shape}")
        print(f"Площадь: {shape.area()}, Периметр: {shape.perimeter()}")

def main():
    shapes = {
        1: lambda: Circle(float(input("Введите радиус круга: "))),
        2: lambda: Rectangle(
            float(input("Введите ширину прямоугольника: ")), 
            float(input("Введите высоту прямоугольника: "))
        ),
        3: lambda: Triangle(
            float(input("Введите сторону A треугольника: ")),
            float(input("Введите сторону B треугольника: ")),
            float(input("Введите сторону C треугольника: "))
        )
    }
    
    print("Выберите фигуру:")
    print("1. Круг")
    print("2. Прямоугольник")
    print("3. Треугольник")
    
    choice = int(input("Введите номер фигуры: "))
    
    if choice in shapes:
        shape = shapes[choice]()  # Создание выбранной фигуры
        print(shape)
        print(f"Площадь: {shape.area()}")
        print(f"Периметр: {shape.perimeter()}")
    else:
        print("Некорректный выбор!")

if __name__ == "__main__":
    main()