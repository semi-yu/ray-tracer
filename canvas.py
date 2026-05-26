import numpy as np
from datetime import datetime

class Color:
    def __init__(self, r, g, b):
        self.r = r
        self.g = g
        self.b = b

    def arrayize(self):
        return np.array([self.r, self.g, self.b])


class Canvas:
    def __init__(self,
                 width: int,
                 height: int):
        self._filename = f"image-{datetime.now().strftime(f"%y-%m-%d %H%M%S")}.ppm"

        self._width = width
        self._height = height

        self._content = np.array([
            [[0, 0, 0]] * self._width
        ] * self._height)

    def write_pixel(self, row, col, color) -> None:
        self._content[col][row] = color.arrayize()

    def to_ppm(self):
        with open(self._filename, 'w') as f:
            f.write(f"P3\n{self._width} {self._height}\n255\n")

            for row in range(self._height):
                for col in range(self._width):
                    r, g, b = self._content[row][col]
                    f.write(f"{r} {g} {b}\n")
