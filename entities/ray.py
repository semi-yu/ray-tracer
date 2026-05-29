import numpy as np

from util.mathematics import Point, Vector
from util.transformation import Transformation


class Ray:
    def __init__(self, origin: Point, direction: Vector):
        self._origin = origin
        self._direction = direction

    @property
    def origin(self) -> Point:
        return self._origin

    @property
    def direction(self) -> Vector:
        return self._direction


def transform(ray: Ray, transform_matrix: Transformation) -> Ray:
    origin = Point()
    origin.set_coord(transform_matrix @ ray.origin.coord)

    direction = Vector()
    direction.set_coord(transform_matrix @ ray.direction.coord)

    nray = Ray(origin, direction)

    return nray
