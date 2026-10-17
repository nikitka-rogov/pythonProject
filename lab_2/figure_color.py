class FigureColor:
    def __init__(self, color):
        self._color = color

    @property
    def color(self):
        """Свойство для получения цвета"""
        return self._color

    @color.setter
    def color(self, value):
        """Свойство для изменения цвета"""
        self._color = value