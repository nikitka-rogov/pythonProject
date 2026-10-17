from .geometric_figure import GeometricFigure
from .figure_color import FigureColor

class Rectangle(GeometricFigure):
    figure_name = "Прямоугольник"

    def __init__(self, width, height, color):
        self.width = width
        self.height = height
        self.color = FigureColor(color)

    def area(self):
        return self.width * self.height

    @classmethod
    def get_name(cls):
        return cls.figure_name

    def __repr__(self):
        return "{}: Ширина: {}, Высота: {}, Цвет: {}, Площадь: {:.2f}".format(
            self.get_name(), self.width, self.height, self.color.color, self.area()
        )