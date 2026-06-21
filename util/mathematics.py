import numpy as np


EPSILON = 1e-5


class Quadruple:
    def __init__(self, x, y, z, w):
        self._coord = np.array([x, y, z, w])

    def set_coord(self, coord):
        self._coord = coord
        return self

    @property
    def coord(self):
        return self._coord

    @property
    def x(self):
        return self._coord[0]

    @property
    def y(self):
        return self._coord[1]

    @property
    def z(self):
        return self._coord[2]

    @property
    def w(self):
        return self._coord[3]
    
    def __repr__(self):
        return f"coord ({self._coord})"


class Vector(Quadruple):
    def __init__(self, x=0, y=0, z=0):
        super().__init__(x, y, z, 0)

    def __sub__(self, other):
        if isinstance(other, Vector):
            return Vector().set_coord(self._coord - other.coord)

    def __mul__(self, other):
        if isinstance(other, (float, int, np.number)):
            return Vector().set_coord(self._coord * other)
        
    def dot(self, other) -> float:
        return np.dot(self._coord, other.coord)

    def normalize(self):
        mag = np.linalg.norm(self._coord)

        new_coord = self._coord.copy()

        result = Vector()
        result.set_coord(new_coord / mag)

        return result

    def magnitude(self):
        return np.linalg.norm(self._coord)


class Point(Quadruple):
    def __init__(self, x=0, y=0, z=0):
        super().__init__(x, y, z, 1)
