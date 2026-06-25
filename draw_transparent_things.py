import numpy as np

from image.canvas import Color
from material import Material
from util.transformation import Transformation
from sphere import Sphere

from util.mathematics import Vector, Point

from light import Light
from world import World
from plane import Plane

from camera import Camera, render

from pattern import StripePattern


def main():
    stripe = StripePattern(
        Color(0.2, 0.2, 0.2), Color(0.8, 0.8, 0.8), Transformation()
    ).set_transform(Transformation().scale(0.2, 0.2, 0.2))

    wall = (
        Plane()
        .set_transform(Transformation().rotate(np.pi / 2, axis="x").translate(0, 0, 5))
        .set_material(
            Material(
                color=Color(1.0, 1.0, 1.0), diffuse=0.7, specular=0.0, pattern=stripe
            )
        )
    )

    floor = Plane().set_material(
        Material(
            color=Color(1.0, 1.0, 1.0),
            diffuse=0.7,
            specular=0.3,
            reflective=0.3,
            pattern=stripe,
        )
    )

    middle = (
        Sphere()
        .set_transform(Transformation().translate(0.0, 1.0, 0.0))
        .set_material(
            Material(
                color=Color(0.0, 0.0, 0.0),
                diffuse=0.0,
                specular=0.9,
                reflective=0.9,
                transparency=1.0,
                refractive_index=1.5,
            )
        )
    )

    inner = (
        Sphere()
        .set_transform(Transformation().scale(0.5, 0.5, 0.5).translate(0.0, 1.0, 0.0))
        .set_material(Material(color=Color(0.8, 0.1, 0.1), diffuse=0.7, specular=0.3))
    )

    right = (
        Sphere()
        .set_transform(
            Transformation().scale(0.75, 0.75, 0.75).translate(2.0, 0.75, -0.5)
        )
        .set_material(
            Material(
                color=Color(0.0, 0.0, 0.0),
                diffuse=0.1,
                specular=0.9,
                reflective=0.8,
                transparency=0.9,
                refractive_index=1.33,
            )
        )
    )

    world = (
        World()
        .set_light(Light(Point(-10, 10, -10), Color(1.0, 1.0, 1.0)))
        .add_object(floor)
        .add_object(wall)
        .add_object(middle)
        .add_object(inner)
        .add_object(right)
    )

    cam = Camera(600, 300, np.pi / 3)
    cam.set_view(Point(0, 2.5, -6), Point(0, 1, 0), Vector(0, 1, 0))

    canvas = render(cam, world)
    canvas.to_ppm()


if __name__ == "__main__":
    main()
