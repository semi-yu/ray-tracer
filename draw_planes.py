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


def main():
    floor = (
        Plane()
        .set_material(Material(color=Color(1, 0.9, 0.9), specular=0.0))
    )

    leftwall = Plane().set_transform(
        Transformation()
        .rotate(np.pi / 2, axis="x")
        .rotate(-np.pi / 4, axis="y")
        .translate(0, 0, 5)
    )

    rightwall = Plane().set_transform(
        Transformation()
        .rotate(np.pi / 2, axis="x")
        .rotate(np.pi / 4, axis="y")
        .translate(0, 0, 5)
    )

    middle = (
        Sphere()
        .set_transform(Transformation().translate(-0.5, 1.0, 0.5))
        .set_material(Material(color=Color(0.1, 1, 0.1), diffuse=0.7, specular=0.3))
    )

    right = (
        Sphere()
        .set_transform(Transformation().scale(0.5, 0.5, 0.5).translate(1.5, 0.5, -0.5))
        .set_material(Material(color=Color(0.1, 1, 0.1), diffuse=0.7, specular=0.3))
    )

    left = (
        Sphere()
        .set_transform(
            Transformation().scale(0.33, 0.33, 0.33).translate(-1.5, 0.33, -0.75)
        )
        .set_material(Material(color=Color(1.0, 0.8, 0.1), diffuse=0.7, specular=0.3))
    )

    world = (
        World()
        .set_light(Light(Point(-10, 10, -10), Color(1.0, 1.0, 1.0)))
        .add_object(floor)
        .add_object(leftwall)
        .add_object(rightwall)
        .add_object(middle)
        .add_object(right)
        .add_object(left)
    )

    cam = Camera(200, 100, np.pi / 3)
    cam.set_view(Point(0, 1.5, -5), Point(0, 1, 0), Vector(0, 1, 0))

    canvas = render(cam, world)
    canvas.to_ppm()


if __name__ == "__main__":
    main()
