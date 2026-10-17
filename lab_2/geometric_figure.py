from abc import ABC, abstractmethod

class GeometricFigure(ABC):
    @abstractmethod
    def area(self):
        """Абстрактный метод для вычисления площади фигуры"""
        pass