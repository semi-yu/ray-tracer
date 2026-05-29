import numpy as np


class Quadruple:
    def __init__(self, x, y, z, w):
        self._coord = np.array([x, y, z, w])

    def set_coord(self, coord):
        self._coord = coord

    @property
    def coord(self):
        return self._coord


class Vector(Quadruple):
    def __init__(self, x=0, y=0, z=0):
        super().__init__(x, y, z, 0)


class Point(Quadruple):
    def __init__(self, x=0, y=0, z=0):
        super().__init__(x, y, z, 1)
