import numpy as np


class Quadruple:
    def __init__(self, x, y, z, w):
        self._coord = np.array([x, y, z, w])

    def set_coord(self, coord):
        self._coord = coord
        return self

    @property
    def coord(self):
        return self._coord


class Vector(Quadruple):
    def __init__(self, x=0, y=0, z=0):
        super().__init__(x, y, z, 0)

    def normalize(self):
        mag = np.linalg.norm(self._coord)

        new_coord = self._coord.copy()

        result = Vector()
        result.set_coord(new_coord / mag)

        return result


class Point(Quadruple):
    def __init__(self, x=0, y=0, z=0):
        super().__init__(x, y, z, 1)
