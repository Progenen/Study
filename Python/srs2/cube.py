from .geometry import Shape

class Cube(Shape):
    """Куб с вычислением объема и площади поверхности."""

    def init(self, edge_length):
        super().init("Куб")
        self.edge_length = edge_length  # Длина ребра

    def volume(self):
        return self.edge_length ** 3

    def surface_area(self):
        return 6 * (self.edge_length ** 2)