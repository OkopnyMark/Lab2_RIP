from lab_python_oop.GeomFig import GeomFig
from lab_python_oop.ColFig import ColFig

class Rec(GeomFig):
    def __init__(self, width, height, color):
        self.width = width
        self.height = height
        rcol = ColFig(color)
        self.color = rcol.col
        self.name = 'Прямоугольник'

    def area(self):
        return self.width * self.height

    def __repr__(self):
        return '{}: \n\t Цвет: {}\n\t Ширина: {}\n\t Высота: {}\n\t Площадь: {}\n'.format(self.name, self.color, self.width, self.height, self.area())
