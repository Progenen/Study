from .cube import Cube
from .cylinder import Cylinder
from .tetrahedron import Tetrahedron

def demonstrate():
    """Функция демонстрации работы программы."""
    figures = {
        "Куб": Cube(5),
        "Цилиндр": Cylinder(3, 7),
        "Тетраэдр": Tetrahedron(4)
    }

    for name, figure in figures.items():
        print(f"\n{name}:")
        print(figure)
        print(f"Объем: {figure.volume():.2f}")
        print(f"Площадь поверхности: {figure.surface_area():.2f}")

# Замыкание для вывода приветствия
def closure_example():
    def greeting(message):
        def inner(name):
            return f"{message}, {name}!"
        return inner

    greet = greeting("Добро пожаловать")
    print(greet("пользователь"))

# Итератор
class FigureIterator:
    def init(self, figures):
        self.figures = figures
        self.index = 0

    def iter(self):
        return self

    def next(self):
        if self.index < len(self.figures):
            result = self.figures[self.index]
            self.index += 1
            return result
        raise StopIteration

# Функтор
class Functor:
    def call(self, message):
        print(f"Сообщение: {message}")

if name == "main":
    demonstrate()
    closure_example()

    print("\nИтератор:")
    figures = ["Куб", "Цилиндр", "Тетраэдр"]
    for figure in FigureIterator(figures):
        print(figure)

    print("\nФунктор:")
    functor = Functor()
    functor("Пример вызова функтора")