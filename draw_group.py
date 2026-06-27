import numpy as np

from util.transformation import Transformation
from util.mathematics import Vector, Point

from image.canvas import Color

from material import Material
from sphere import Sphere
from cylinder import Cylinder

from group import Group

from light import Light
from world import World
from camera import Camera, render


def hexagon_corner():
    corner = Sphere()
    corner.set_transform(
        Transformation()
        .scale(0.25, 0.25, 0.25)
        .translate(0.0, 0.0, -1.0)
    )
    return corner

def hexagon_edge():
    edge = Cylinder(minimum=0.0, maximum=1.0, closed=False)
    edge.set_transform(
        Transformation()
        .scale(0.25, 1.0, 0.25)
        .rotate(-np.pi / 2, axis='z')
        .rotate(-np.pi / 6, axis='y')
        .translate(0.0, 0.0, -1.0)
    )
    return edge

def hexagon_side():
    side = Group()
    side.add_child(hexagon_corner())
    side.add_child(hexagon_edge())
    return side

def hexagon():
    hex_group = Group()
    for n in range(6):
        side = hexagon_side()
        side.set_transform(Transformation().rotate(n * np.pi / 3, axis='y'))
        hex_group.add_child(side)
    return hex_group

def main():
    hex_model = hexagon()
    
    hex_model.set_transform(
        Transformation()
        .rotate(np.pi / 3, axis='x')
        .translate(0.0, 1.0, 0.0)
    )
    
    hex_material = Material(
        color=Color(0.8, 0.8, 0.9),
        diffuse=0.7,
        specular=0.3,
        reflective=0.2
    )
    try:
        hex_model.set_material(hex_material)
    except AttributeError:
        pass

    world = (
        World()
        .set_light(Light(Point(-10, 10, -10), Color(1.0, 1.0, 1.0)))
        .add_object(hex_model)
    )

    cam = Camera(400, 200, np.pi / 3)
    cam.set_view(Point(0, 4, -5), Point(0, 1, 0), Vector(0, 1, 0))

    canvas = render(cam, world)
    canvas.to_ppm()

if __name__ == "__main__":
    main()