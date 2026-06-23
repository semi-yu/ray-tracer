import numpy as np

from shape import Shape
from util.mathematics import Vector, Point


def normal_at(shape: Shape, point: Point) -> Vector:
    local_point = Point().set_coord(np.linalg.inv(shape.transform.matrix) @ point.coord)
    local_normal = shape.local_normal_at(local_point)

    world_normal = np.linalg.inv(shape.transform.matrix).T @ local_normal.coord

    result = Vector().set_coord(world_normal)

    return result.normalize()
