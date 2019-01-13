from lab_python_oop.Rectangle import Rec
from lab_python_oop.ColFig import ColFig

class Square(Rec):
    def __init__(self, lenght, color):
        self.height = lenght
        self.width = lenght
        scol = ColFig(color)
        self.color = scol.col
        self.name = 'Квадрат'

    def __repr__(self):
        return '{}: \n\t Цвет: {}\n\t Длина стороны: {}\n\t Площадь: {}\n'.format(self.name, self.color, self.width, self.area())
