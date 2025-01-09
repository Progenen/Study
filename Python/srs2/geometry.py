class Shape:
    """Базовый класс для геометрических фигур."""

    def init(self, name):
        self.name = name  # Название фигуры

    def volume(self):
        """Виртуальный метод для вычисления объема."""
        raise NotImplementedError("Метод должен быть переопределен в подклассе")

    def surface_area(self):
        """Виртуальный метод для вычисления площади поверхности."""
        raise NotImplementedError("Метод должен быть переопределен в подклассе")

    def str(self):
        return f"Геометрическая фигура: {self.name}"