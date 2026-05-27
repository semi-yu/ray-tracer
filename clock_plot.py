import math

import numpy as np

from canvas import Canvas, Color
from transformation import Transformation

width = 600
height = 600


def main():
    canvas = Canvas(width, height)
    color = Color(126, 255, 0)

    for i in range(12):
        transform = (
            Transformation()
            .rotate(math.pi / 6 * i, axis="z")
            .translate(width // 2, height // 2, 0)
        )

        position = transform.matrix @ np.array([200, 0, 0, 1])

        x, y, _, __ = map(int, position)
        canvas.write_pixel(x, y, color)

    canvas.to_ppm()


if __name__ == "__main__":
    main()
