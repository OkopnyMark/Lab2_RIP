from lab_python_oop.GeomFig import GeomFig
from lab_python_oop.ColFig import ColFig
from math import pi

class Circle(GeomFig):
    def __init__(self, rad, color):
        self.rad = rad
        ccol = ColFig(color)
        self.color = ccol.col
        self.name = 'Круг'

    def area(self):
        return self.rad * self.rad * pi

    def __repr__(self):
        return '{}: \n\t Цвет: {}\n\t Радиус: {}\n\t Площадь: {}\n'.format(self.name, self.color, self.rad, self.area())

