import numpy as np

from util.mathematics import Point
from image.canvas import Color

from util.transformation import Transformation


class Pattern:
    def __init__(self, transform):
        self._transform = transform

    def set_transform(self, transform: Transformation):
        self._transform = transform
        return self

    def pattern_at(self, point: Point) -> Color:
        return Color(point.x, point.y, point.z)

        raise Exception("implement the method to use!")

    def pattern_at_object(self, obj, point: Point) -> Color:
        obj_point = np.linalg.inv(obj.transform.matrix) @ point.coord
        pat_point = np.linalg.inv(self._transform.matrix) @ obj_point

        result = Point().set_coord(pat_point)

        return self.pattern_at(result)

    @property
    def transform(self):
        return self._transform


class StripePattern(Pattern):
    def __init__(self, a: Color, b: Color, transform=Transformation()):
        super().__init__(transform)
        self._a = a
        self._b = b

    def pattern_at(self, point: Point) -> Color:
        pointx = point.x
        return self._a if np.floor(pointx) % 2 == 0 else self._b

    @property
    def a(self):
        return self._a

    @property
    def b(self):
        return self._b


class GradientPattern(Pattern):
    def __init__(self, a: Color, b: Color, transform):
        super().__init__(transform)
        self._a = a
        self._b = b

    def pattern_at(self, point: Point) -> Color:
        distance = self._b - self._a
        fraction = 1.0 - 2.0 * abs(point.x - np.floor(point.x) - 0.5)
        return self._a + distance * fraction


class RingPattern(Pattern):
    def __init__(self, a: Color, b: Color, transform):
        super().__init__(transform)
        self._a = a
        self._b = b

    def pattern_at(self, point: Point) -> Color:
        norm = np.hypot(point.x, point.z)
        return self._a if int(np.floor(norm)) % 2 == 0 else self._b


class CheckerPattern(Pattern):
    def __init__(self, a: Color, b: Color, transform):
        super().__init__(transform)
        self._a = a
        self._b = b

    def pattern_at(self, point: Point) -> Color:
        total = np.floor(point.x) + np.floor(point.y) + np.floor(point.z)
        return self._a if total % 2 == 0 else self._b
