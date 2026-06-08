import math

import numpy as np

from intersect import intersect
from shadow import hit

from util.transformation import Transformation
from util.mathematics import Point, Vector

from entities.sphere import Sphere
from entities.ray import Ray

from image.canvas import Canvas, Color


width = 100


def main():
    canvas = Canvas(width, width)
    color = Color(255, 0, 0)

    ray_origin = Point(0, 0, -5.0)

    sphere_origin = Point(0, 0, 0)
    sphere = Sphere(sphere_origin, 1.0)

    transform = Transformation().shear(1, 0, 0, 0, 0, 0).scale(0.5, 1, 1)

    sphere.set_transform(transform)

    wallsize = 6.0
    wallz = 10

    pixelsize = wallsize / width
    half = wallsize / 2

    for y in range(width):
        worldy = -half + pixelsize * y

        for x in range(width):
            worldx = -half + pixelsize * x
            world_pos = Vector(worldx, worldy, wallz)

            ray_direct = Vector(0, 0, 0)
            diff = world_pos.coord - ray_origin.coord

            ray_direct.set_coord(diff / np.linalg.norm(diff))
            ray = Ray(ray_origin, ray_direct)

            xpoints = intersect(sphere, ray)

            if hit(xpoints):
                canvas.write_pixel(y, x, color)

    canvas.to_ppm()


if __name__ == "__main__":
    main()
