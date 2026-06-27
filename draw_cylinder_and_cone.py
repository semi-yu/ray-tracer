import numpy as np

from image.canvas import Color
from util.transformation import Transformation
from util.mathematics import Vector, Point

from material import Material
from cylinder import Cylinder
from cone import Cone
from plane import Plane
from light import Light
from world import World
from camera import Camera, render
from pattern import StripePattern


def main():
    stripe = StripePattern(Color(0.2, 0.2, 0.2), Color(0.8, 0.8, 0.8), Transformation()) \
            .set_transform(Transformation().scale(0.5, 0.5, 0.5))

    floor = (
        Plane()
        .set_material(
            Material(
                color=Color(1.0, 1.0, 1.0),
                diffuse=0.7,
                specular=0.1,
                pattern=stripe
            )
        )
    )

    left_cylinder = (
        Cylinder(minimum=-1, maximum=1, closed=True)
        .set_transform(
            Transformation()
            .scale(0.8, 1.0, 0.8)
            .translate(-2.0, 1.0, -0.5)
        )
        .set_material(
            Material(
                color=Color(0.1, 0.8, 0.1),
                diffuse=0.7,
                specular=0.3
            )
        )
    )

    center_cone = (
        Cone(minimum=-1, maximum=0, closed=True)
        .set_transform(
            Transformation()
            .scale(1.5, 2.0, 1.5)
            .translate(0.0, 2.0, 0.0)
        )
        .set_material(
            Material(
                color=Color(0.8, 0.2, 0.2),
                diffuse=0.7,
                specular=0.3,
                reflective=0.1
            )
        )
    )

    right_cylinder = (
        Cylinder(minimum=-1, maximum=1, closed=False)
        .set_transform(
            Transformation()
            .scale(0.8, 1.0, 0.8)
            .translate(2.0, 1.0, -0.5)
        )
        .set_material(
            Material(
                color=Color(0.0, 0.0, 0.0),
                diffuse=0.0,
                specular=0.9,
                transparency=0.9,
                refractive_index=1.5
            )
        )
    )

    world = (
        World()
        .set_light(Light(Point(-5, 10, -5), Color(1.0, 1.0, 1.0)))
        .add_object(floor)
        .add_object(left_cylinder)
        .add_object(center_cone)
        .add_object(right_cylinder)
    )

    cam = Camera(600, 300, np.pi / 3)
    cam.set_view(Point(0, 3, -8), Point(0, 1, 0), Vector(0, 1, 0))

    canvas = render(cam, world)
    canvas.to_ppm()

if __name__ == "__main__":
    main()