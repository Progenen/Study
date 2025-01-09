from .geometry import Shape

class Tetrahedron(Shape):
    """Тетраэдр с перегрузкой метода вычисления площади."""

    def init(self, edge_length):
        super().init("Тетраэдр")
        self.edge_length = edge_length

    def volume(self):
        from math import sqrt
        return (self.edge_length ** 3) / (6 * sqrt(2))

    def surface_area(self):
        from math import sqrt
        return sqrt(3) * (self.edge_length ** 2)

    def str(self):
        """Перегрузка метода для представления объекта."""
        return f"Тетраэдр с длиной ребра {self.edge_length}"