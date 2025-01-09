from .geometry import Shape

class Cylinder(Shape):
    """Цилиндр с вычислением объема и площади поверхности."""

    def init(self, radius, height):
        super().init("Цилиндр")
        self.radius = radius
        self.height = height

    def volume(self):
        from math import pi
        return pi * self.radius ** 2 * self.height

    def surface_area(self):
        from math import pi
        return 2 * pi * self.radius * (self.radius + self.height)