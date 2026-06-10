import numpy as np

from util.mathematics import Point
from image.canvas import Color

from util.transformation import Transformation


class Pattern:
    # Just an placeholder class
    def __init__(self, transform: Transformation):
        self._transform = transform
    
    def set_transform(self, transform: Transformation):
        self._transform = transform
        return self

    @property
    def transform(self): return self._transform


class StripePattern(Pattern):
    def __init__(self, a: Color, b: Color, transform = Transformation()):
        super().__init__(transform)
        self._a = a
        self._b = b

    def stripe_at(self, point: Point) -> Color:
        pointx = point.x
        return self._a if np.floor(pointx) % 2 == 0 else self._b

    def stripe_at_object(self, object, point: Point) -> Color:
        obj_point = np.linalg.inv(object.transform.matrix) @ point.coord
        pat_point = np.linalg.inv(self._transform.matrix) @ obj_point

        result  = Point().set_coord(pat_point)

        return self.stripe_at(result)

    @property
    def a(self):
        return self._a

    @property
    def b(self):
        return self._b
