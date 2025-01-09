import math
import tkinter as tk


# Базовый класс
class BaseFunction:
    """Базовый класс для математических функций"""

    def __init__(self, variable):
        """Инициализация переменной"""
        self.variable = variable

    def get_value(self):
        """Вычисляет значение функции для текущей переменной"""
        raise NotImplementedError("Этот метод должен быть переопределен в наследниках")

    def create_derivative(self):
        """Создает экземпляр класса, представляющий производную текущей функции"""
        raise NotImplementedError("Этот метод должен быть переопределен в наследниках")

    def __str__(self):
        """Возвращает строковое представление класса"""
        return f"Функция с переменной {self.variable}"


# Наследник: синус
class SinFunction(BaseFunction):
    """Класс для функции синуса"""

    def get_value(self):
        """Возвращает значение синуса для текущей переменной"""
        return math.sin(self.variable)

    def create_derivative(self):
        """Создает производную функции синуса (косинус)"""
        return CosFunction(self.variable)

    def __str__(self):
        """Возвращает строковое представление класса"""
        return f"sin({self.variable})"


# Наследник: косинус
class CosFunction(BaseFunction):
    """Класс для функции косинуса"""

    def get_value(self):
        """Возвращает значение косинуса для текущей переменной"""
        return math.cos(self.variable)

    def create_derivative(self):
        """Создает производную функции косинуса (-синус)"""
        return NegativeSinFunction(self.variable)

    def __str__(self):
        """Возвращает строковое представление класса"""
        return f"cos({self.variable})"


# Наследник: тангенс
class TanFunction(BaseFunction):
    """Класс для функции тангенса"""

    def get_value(self):
        """Возвращает значение тангенса для текущей переменной"""
        return math.tan(self.variable)

    def create_derivative(self):
        """Создает производную функции тангенса (1 + tan^2)"""
        return TanDerivative(self.variable)

    def __str__(self):
        """Возвращает строковое представление класса"""
        return f"tan({self.variable})"


# Производная от косинуса: -синус
class NegativeSinFunction(SinFunction):
    """Класс для функции -синуса (производная косинуса)"""

    def get_value(self):
        """Возвращает значение -синуса для текущей переменной"""
        return -super().get_value()


# Производная от тангенса: 1 + tan^2
class TanDerivative(BaseFunction):
    """Класс для производной функции тангенса"""

    def get_value(self):
        """Возвращает значение производной (1 + tan^2)"""
        return 1 + math.tan(self.variable) ** 2

    def __str__(self):
        """Возвращает строковое представление класса"""
        return f"1 + tan^2({self.variable})"


# Декоратор для логирования
def log_call(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(f"Вызов {func.__name__} с аргументами {args}, результат: {result}")
        return result

    return wrapper


# Замыкание для умножения
def multiplier(factor):
    def multiply(value):
        return value * factor

    return multiply


# Функтор для вычисления
class Evaluator:
    def __call__(self, func):
        return func.get_value()


# Итератор по значениям функций
class FunctionIterator:
    def __init__(self, functions):
        self.functions = functions
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.functions):
            raise StopIteration
        func = self.functions[self.index]
        self.index += 1
        return func.get_value()


# Демонстрация работы
@log_call
def demo():
    sin_func = SinFunction(math.pi / 4)
    cos_func = sin_func.create_derivative()
    tan_func = TanFunction(math.pi / 4)

    # Используем функтор
    evaluator = Evaluator()
    print(f"Значение sin(pi/4): {evaluator(sin_func)}")
    print(f"Значение cos(pi/4): {evaluator(cos_func)}")
    print(f"Значение tan(pi/4): {evaluator(tan_func)}")

    # Используем замыкание
    double = multiplier(2)
    print(f"Удвоенное значение sin(pi/4): {double(sin_func.get_value())}")

    # Используем итератор
    iterator = FunctionIterator([sin_func, cos_func, tan_func])
    print("Значения функций через итератор:", list(iterator))


# Интерфейс на Tkinter
def create_interface():
    root = tk.Tk()
    root.title("Математические функции")

    def calculate():
        try:
            value = float(entry.get())
            func = SinFunction(value)
            result.set(f"sin({value}) = {func.get_value()}")
        except ValueError:
            result.set("Ошибка: введите число!")

    label = tk.Label(root, text="Введите значение:")
    label.pack()

    entry = tk.Entry(root)
    entry.pack()

    result = tk.StringVar()
    button = tk.Button(root, text="Рассчитать", command=calculate)
    button.pack()

    result_label = tk.Label(root, textvariable=result)
    result_label.pack()

    root.mainloop()


# Выполнение
if name == "__main__":
    demo()
    create_interface()