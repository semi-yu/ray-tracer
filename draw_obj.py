import numpy as np

from image.canvas import Color
from material import Material
from util.transformation import Transformation
from util.mathematics import Vector, Point
from light import Light
from world import World
from plane import Plane
from camera import Camera, render
from pattern import CheckerPattern

from obj_file import parse_obj, obj_to_group, read_obj

def main():
    checkers = CheckerPattern(Color(0.2, 0.2, 0.2), Color(0.8, 0.8, 0.8), Transformation()) \
            .set_transform(Transformation().scale(0.5, 0.5, 0.5))

    floor = (
        Plane()
        .set_material(
            Material(
                color=Color(1.0, 1.0, 1.0),
                diffuse=0.7,
                specular=0.1,
                pattern=checkers
            )
        )
    )

    wall = (
        Plane()
        .set_transform(Transformation().rotate(np.pi / 2, axis='x').translate(0, 0, 5))
        .set_material(
            Material(
                color=Color(1.0, 1.0, 1.0),
                diffuse=0.7,
                specular=0.1,
                pattern=checkers
            )
        )
    )

    content = read_obj("dodecahedron.obj")
    parsed_data = parse_obj(content)

    teapot = obj_to_group(parsed_data)

    if len(teapot) == 0:
        for s in parsed_data.shapes:
            teapot.add_child(s)

    teapot.set_transform(
        Transformation()
        .scale(0.2, 0.2, 0.2)
        .rotate(-np.pi / 2, axis='x')
        .rotate(np.pi / 4, axis='y')
        .translate(0.0, 0.35, 0.0)
    )
    
    teapot_material = Material(
        color=Color(0.8, 0.3, 0.3),
        diffuse=0.7,
        specular=0.3
    )

    for shape in teapot.shapes:
        shape.set_material(teapot_material)

    world = (
        World()
        .set_light(Light(Point(-5, 10, -5), Color(1.0, 1.0, 1.0)))
        .add_object(floor)
        .add_object(wall)
        .add_object(teapot)
    )

    cam = Camera(400, 200, np.pi / 3)
    cam.set_view(Point(0, 3, -6), Point(0, 1.0, 0), Vector(0, 1, 0))

    canvas = render(cam, world)
    canvas.to_ppm()

if __name__ == "__main__":
    main()
