import numpy as np

from intersect import intersect
from shadow import hit

from util.transformation import Transformation
from util.mathematics import Point, Vector

from light import Light, lighting
from sphere import Sphere
from entities.ray import Ray
from entities.normal import normal_at

from image.canvas import Canvas, Color


width = 100


def position(ray: Ray, t: float) -> Point:
    result = Point(0, 0, 0)
    # P(t) = origin + direction * t
    result.set_coord(ray.origin.coord + ray.direction.coord * t)
    return result


def main():
    canvas = Canvas(width, width)

    ray_origin = Point(0, 0, -5.0)

    sphere_origin = Point(0, 0, 0)
    sphere = Sphere(sphere_origin, 1.0)
    sphere.material.set_color(Color(1.0, 0.2, 1.0))

    light = Light(Point(-10, 10, -10), Color(1.0, 1.0, 1.0))

    sphere.set_transform(Transformation())

    wallsize = 6.0
    wallz = 10

    pixelsize = wallsize / width
    half = wallsize / 2

    for y in range(width):
        worldy = half - pixelsize * y

        for x in range(width):
            worldx = -half + pixelsize * x
            world_pos = Point(worldx, worldy, wallz)

            ray_direct = Vector(0, 0, 0)
            diff = world_pos.coord - ray_origin.coord

            ray_direct.set_coord(diff / np.linalg.norm(diff))
            ray = Ray(ray_origin, ray_direct)

            xpoints = intersect(sphere, ray)
            h = hit(xpoints)

            if h:
                point = position(ray, h.t)

                normal = normal_at(h.object, point)

                eye_direct = Vector()
                eye_direct.set_coord(-ray_direct.coord)

                color = lighting(h.object.material, light, point, eye_direct, normal)

                color_arr = color.arrayize()
                clamp = lambda x: int(max(0.0, min(1.0, x)) * 255)

                r, g, b = map(clamp, color_arr)

                canvas.write_pixel(x, y, Color(r, g, b))

    canvas.to_ppm()


if __name__ == "__main__":
    main()
