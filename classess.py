import math


class Point:
    def __init__(self, _x, _y):
        self.x = _x
        self.y = _y


class Figure:

    @staticmethod
    def sqr(_x):
        return _x * _x

    @staticmethod
    def dist(_p1, _p2):
        return math.sqrt(Figure.sqr(_p1.x - _p2.x) + Figure.sqr(_p1.y - _p2.y))

    def length(self):
        pass

    def square(self):
        pass


class Circle(Figure):
    def __init__(self, _point, _r):
        if type(_point) is Point:
            self.center = _point
        self.radius = _r

    def length(self):
        return 2 * math.pi * self.radius

    def square(self):
        return math.pi * self.radius * self.radius


class Triangle(Figure):
    def __init__(self, _p1, _p2, _p3):
        if type(_p1) is Point:
            self.p1 = _p1
        if type(_p2) is Point:
            self.p2 = _p2
        if type(_p3) is Point:
            self.p3 = _p3

    def length(self):
        l1 = Figure.dist(self.p1, self.p2)
        l2 = Figure.dist(self.p1, self.p3)
        l3 = Figure.dist(self.p2, self.p3)
        return l1 + l2 + l3

    def square(self):
        l1 = Figure.dist(self.p1, self.p2)
        l2 = Figure.dist(self.p1, self.p3)
        l3 = Figure.dist(self.p2, self.p3)
        p = (l1 + l2 + l3) / 2
        return math.sqrt(p*(p-l1)*(p-l2)*(p-l3))


class Square(Figure):
    def __init__(self, _p1, _p2):
        if type(_p1) is Point:
            self.p1 = _p1
        if type(_p2) is Point:
            self.p2 = _p2

    def length(self):
        l1 = Figure.dist(self.p1, self.p2)
        return l1*4

    def square(self):
        l1 = Figure.dist(self.p1, self.p2)
        return l1 * l1