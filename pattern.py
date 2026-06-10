import numpy as np

from util.mathematics import Point
from image.canvas import Color


class StripePattern:
    def __init__(self, a: Color, b: Color):
        self._a = a
        self._b = b

    def stripe_at(self, point: Point) -> Color:
        pointx = point.x
        print(pointx, int(pointx), np.floor(pointx))
        return self._a if np.floor(pointx) % 2 == 0 else self._b

    @property
    def a(self): return self._a

    @property
    def b(self): return self._b