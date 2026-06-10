import numpy as np
from datetime import datetime


class Color:
    def __init__(self, r: float = 0.0, g: float = 0.0, b: float = 0.0):
        self._r = r
        self._g = g
        self._b = b

    def __repr__(self):
        return f"Color({self.r}, {self.g}, {self.b})"
    
    def __add__(self, other):
        calculated = np.array([self.r + other.r, self.g + other.g, self.b + other.b])
        return Color().set_coord(calculated)

    def __sub__(self, other):
        calculated = np.array([self.r - other.r, self.g - other.g, self.b - other.b])
        return Color().set_coord(calculated)

    def __mul__(self, other):
        if isinstance(other, float):
            calculated = other * self.arrayize()
            return Color().set_coord(calculated)
        elif isinstance(other, Color):
            # hadamard product
            calculated = np.multiply(self.arrayize(), other.arrayize())
            return Color().set_coord(calculated)
        else:
            raise Exception("not implemented yet!")

    def arrayize(self):
        return np.array([self._r, self._g, self._b])

    def set_coord(self, coord):
        self._r, self._g, self._b = coord[0], coord[1], coord[2]
        return self
    
    @property
    def r(self): return self._r
    
    @property
    def g(self): return self._g

    @property
    def b(self): return self._b

class Canvas:
    def __init__(self, width: int, height: int):
        self._filename = f"Image-{datetime.now().strftime('%y%m%d %H%M%S')}.ppm"

        self._width = width
        self._height = height

        self._content = np.array([[[0, 0, 0]] * self._width] * self._height)

    def write_pixel(self, row, col, color) -> None:
        r, g, b = map(lambda x: int(max(0.0, min(1.0, x)) * 255), color.arrayize())
        self._content[col][row] = np.array([r, g, b])

    def to_ppm(self):
        with open(self._filename, "w") as f:
            f.write(f"P3\n{self._width} {self._height}\n255\n")

            for row in range(self._height):
                for col in range(self._width):
                    r, g, b = self._content[row][col]
                    f.write(f"{r} {g} {b}\n")
