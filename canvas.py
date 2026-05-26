import numpy as np
from datetime import datetime


class Canvas:
    def __init__(self,
                 width: int,
                 height: int):
        self._width = width
        self._height = height

    def save(self,
              data: np.array,
              filename: str=f"image-{datetime.now().strftime(f"%y-%m-%d %H%M%S")}.ppm"
        ) -> None:
        with open(filename, 'w') as f:
            f.write(f"P3\n{self._width} {self._height}\n255\n")

            for row in range(self._height):
                for col in range(self._width):
                    r, g, b = data[row][col]
                    f.write(f"{r} {g} {b}\n")
