from .rectangle import Rectangle

class Square(Rectangle):
    figure_name = "Квадрат"

    def __init__(self, side, color):
        # Квадрат — это прямоугольник с одинаковыми сторонами
        super().__init__(side, side, color)

    def __repr__(self):
        return "{}: Сторона: {}, Цвет: {}, Площадь: {:.2f}".format(
            self.get_name(), self.width, self.color.color, self.area()
        )