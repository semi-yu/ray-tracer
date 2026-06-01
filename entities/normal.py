import numpy as np

from entities.sphere import Sphere
from util.mathematics import Vector, Point


def normal_at(s: Sphere, p: Point) -> Vector:
    localp = Point()
    localp.set_coord(np.linalg.inv(s.transform.matrix) @ p.coord)

    diff = localp.coord - Point().coord

    normal = Vector()
    normal.set_coord(diff / np.linalg.norm(diff))

    result_coord = np.linalg.inv(s.transform.matrix).T @ normal.coord
    result_coord[3] = 0.0

    result_coord /= np.linalg.norm(result_coord)

    result = Vector()
    result.set_coord(result_coord)

    return result
