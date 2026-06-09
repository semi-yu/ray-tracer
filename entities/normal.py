import numpy as np

from shape import Shape
from util.mathematics import Vector, Point


def normal_at(shape: Shape, point: Point) -> Vector:
    local_point = np.linalg.inv(shape.transform.matrix) @ point.coord
    local_normal = shape.local_normal_at(local_point)

    world_normal = np.linalg.inv(shape.transform.matrix).T @ local_normal.coord
    world_normal[3] = 0.0

    result = Vector().set_coord(world_normal)

    return result.normalize()
