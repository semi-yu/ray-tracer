import numpy as np
from image.canvas import Color
from material import Material
from util.transformation import Transformation
from sphere import Sphere
from cube import Cube
from csg import Csg
from util.mathematics import Vector, Point
from light import Light
from world import World
from plane import Plane
from camera import Camera, render
from pattern import CheckerPattern

def main():
    checkers = CheckerPattern(Color(0.2, 0.2, 0.2), Color(0.8, 0.8, 0.8), Transformation()).set_transform(Transformation().scale(0.5, 0.5, 0.5))
    
    floor = Plane().set_material(Material(color=Color(1.0, 1.0, 1.0), diffuse=0.7, specular=0.1, pattern=checkers))
    
    mat_left = Material(color=Color(0.8, 0.2, 0.2), diffuse=0.7, specular=0.3)
    mat_right = Material(color=Color(0.2, 0.2, 0.8), diffuse=0.7, specular=0.3)
    
    s1 = Sphere().set_transform(Transformation().translate(-0.5, 0.0, 0.0)).set_material(mat_left)
    c1 = Cube().set_transform(Transformation().scale(0.8, 0.8, 0.8).translate(0.5, 0.0, 0.0)).set_material(mat_right)
    csg_union = Csg("union", s1, c1).set_transform(Transformation().translate(-2.5, 1.0, 0.0))
    
    c2 = Cube().set_material(mat_left)
    s2 = Sphere().set_transform(Transformation().scale(1.3, 1.3, 1.3)).set_material(mat_right)
    csg_difference = Csg("difference", c2, s2).set_transform(Transformation().translate(0.0, 1.0, 0.0))
    
    s3 = Sphere().set_transform(Transformation().translate(-0.5, 0.0, 0.0)).set_material(mat_left)
    s4 = Sphere().set_transform(Transformation().translate(0.5, 0.0, 0.0)).set_material(mat_right)
    csg_intersection = Csg("intersection", s3, s4).set_transform(Transformation().translate(2.5, 1.0, 0.0))
    
    world = World().set_light(Light(Point(-5, 10, -5), Color(1.0, 1.0, 1.0))).add_object(floor).add_object(csg_union).add_object(csg_difference).add_object(csg_intersection)
    
    cam = Camera(400, 200, np.pi / 3)
    cam.set_view(Point(0, 3, -7), Point(0, 1, 0), Vector(0, 1, 0))
    
    canvas = render(cam, world)
    canvas.to_ppm()

if __name__ == "__main__":
    main()