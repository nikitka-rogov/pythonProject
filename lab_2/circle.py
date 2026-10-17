import math
from .geometric_figure import GeometricFigure
from .figure_color import FigureColor

class Circle(GeometricFigure):
    figure_name = "Круг"

    def __init__(self, radius, color):
        self.radius = radius
        self.color = FigureColor(color)

    def area(self):
        return math.pi * (self.radius ** 2)

    @classmethod
    def get_name(cls):
        return cls.figure_name

    def __repr__(self):
        return "{}: Радиус: {}, Цвет: {}, Площадь: {:.2f}".format(
            self.get_name(), self.radius, self.color.color, self.area()
        )