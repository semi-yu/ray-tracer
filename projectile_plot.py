import numpy as np

from image.canvas import Canvas, Color
from ch02.projectile import Projectile, Environment, tick


def main():
    position = np.array([0, 1, 0])
    initv = np.array([1, 1.8, 0])
    velocity = initv / np.linalg.norm(initv) * 11.25

    projectile = Projectile(velocity, position)

    environment = Environment(np.array([0, -0.1, 0]), np.array([-0.01, 0, 0]))

    cnv = Canvas(900, 500)
    color = Color(255, 150, 150)

    pos = projectile.position
    cnv.write_pixel(int(pos[0]), int(pos[1]), color)

    while True:
        projectile = tick(environment, projectile)
        pos = projectile.position

        if 0 <= pos[0] < 900 and 0 <= pos[1] < 500:
            cnv.write_pixel(int(pos[0]), 500 - int(pos[1]), color)
        else:
            break

    cnv.to_ppm()


if __name__ == "__main__":
    main()
