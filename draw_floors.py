import numpy as np

from image.canvas import Color
from entities.material import Material
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
        .set_material(Material(color=Color(0.9, 0.9, 0.9), specular=0.0))
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
        .add_object(middle)
        .add_object(right)
        .add_object(left)
    )
    
    cam = Camera(300, 150, np.pi / 3)
    cam.set_view(Point(0, 3, -6), Point(0, 1, 0), Vector(0, 1, 0))
    
    canvas = render(cam, world)
    canvas.to_ppm()


if __name__ == "__main__":
    main()
