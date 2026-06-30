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
        return f"({self._coord})"


class Vector(Quadruple):
    def __init__(self, x=0, y=0, z=0):
        super().__init__(x, y, z, 0)

    def set_coord(self, coord):
        self._coord = np.array([coord[0], coord[1], coord[2], 0.0])
        return self

    def __sub__(self, other):
        if isinstance(other, Vector):
            return Vector().set_coord(self._coord - other.coord)

    def __mul__(self, other):
        if isinstance(other, (float, int, np.number)):
            return Vector().set_coord(self._coord * other)

    def dot(self, other) -> float:
        return np.dot(self._coord, other.coord)

    def cross(self, other):
        return Vector().set_coord(np.cross(self._coord[:3], other.coord[:3]))

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

    def __sub__(self, other) -> Vector:
        result = self.coord - other.coord
        return Vector().set_coord(result)

    def set_coord(self, coord):
        self._coord = np.array([coord[0], coord[1], coord[2], 1.0])
        return self
