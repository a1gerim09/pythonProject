import math


class Figure:
    unit = 'cm'

    def __init__(self):
        pass

    def calculate_area(self):
        pass

    def info(self):
        pass


class Circle(Figure):
    def __init__(self, radius):
        self.__radius = radius

    def calculate_area(self):
        return round(math.pi * self.__radius**2, 2)

    def info(self):
        return f'Circle radius: {self.__radius} {Figure.unit}, area: {self.calculate_area()} {Figure.unit}.'


class RightTriangle(Figure):
    def __init__(self, side_a, side_b):
        self.__side_a = side_a
        self.__side_b = side_b

    def calculate_area(self):
        return round(0.5 * self.__side_a * self.__side_b, 2)

    def info(self):
        return f'RightTriangle side a: {self.__side_a} {Figure.unit}, side b: {self.__side_b} {Figure.unit}, ' \
               f'area: {self.calculate_area()} {Figure.unit}.'


figures = [RightTriangle(5, 8), RightTriangle(3, 4), RightTriangle(7, 24), Circle(5), Circle(10)]


for figure in figures:
    print(figure.info())

