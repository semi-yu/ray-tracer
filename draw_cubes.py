import numpy as np

from image.canvas import Color
from material import Material
from util.transformation import Transformation
from cube import Cube
from util.mathematics import Vector, Point
from light import Light
from world import World
from camera import Camera, render
from pattern import StripePattern

def main():
    stripe = StripePattern(Color(0.2, 0.2, 0.2), Color(0.8, 0.8, 0.8), Transformation()) \
            .set_transform(Transformation().scale(0.2, 0.2, 0.2))

    floor = (
        Cube()
        .set_transform(Transformation().scale(10.0, 0.1, 10.0).translate(0.0, -0.1, 0.0))
        .set_material(
            Material(
                color=Color(1.0, 1.0, 1.0),
                diffuse=0.7,
                specular=0.3,
                pattern=stripe
            )
        )
    )

    left_cube = (
        Cube()
        .set_transform(
            Transformation()
            .scale(0.5, 0.8, 0.5)
            .rotate(np.pi / 4, axis='y')
            .translate(-1.5, 0.8, -0.5)
        )
        .set_material(
            Material(
                color=Color(0.8, 0.2, 0.2),
                diffuse=0.7,
                specular=0.3
            )
        )
    )

    center_cube = (
        Cube()
        .set_transform(
            Transformation()
            .scale(0.6, 0.6, 0.6)
            .rotate(np.pi / 6, axis='x')
            .rotate(np.pi / 4, axis='y')
            .translate(0.0, 0.6, 0.0)
        )
        .set_material(
            Material(
                color=Color(0.1, 0.1, 0.1),
                diffuse=0.2,
                specular=0.9,
                reflective=0.8
            )
        )
    )

    right_cube = (
        Cube()
        .set_transform(
            Transformation()
            .scale(0.5, 0.5, 0.5)
            .translate(1.5, 0.5, -0.5)
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
        .add_object(left_cube)
        .add_object(center_cube)
        .add_object(right_cube)
    )

    cam = Camera(600, 300, np.pi / 3)
    cam.set_view(Point(0, 3, -6), Point(0, 1, 0), Vector(0, 1, 0))

    canvas = render(cam, world)
    canvas.to_ppm()

if __name__ == "__main__":
    main()
