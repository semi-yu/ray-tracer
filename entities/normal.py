import numpy as np

from shape import Shape
from util.mathematics import Vector, Point


def normal_at(shape: Shape, world_point: Point, hit = None) -> Vector:
    local_point = world_to_object(shape, world_point)
    local_normal = shape.local_normal_at(local_point, hit)
    
    return normal_to_world(shape, local_normal)

def normal_to_world(shape: Shape, normal: Vector):
    normal_coord = shape.transform.inverse().matrix.T @ normal.coord

    normal = Vector().set_coord(normal_coord).normalize()

    if shape.parent is not None:
        normal = normal_to_world(shape.parent, normal)
    
    return normal

def world_to_object(shape, point: Point):
    if shape.parent is not None:
        point = world_to_object(shape.parent, point)

    return Point().set_coord(shape.transform.inverse().matrix @ point.coord)
