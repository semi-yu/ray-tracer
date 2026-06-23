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

    def transform(self, matrix):
        return Ray(
            Point().set_coord(matrix @ self._origin.coord),
            Vector().set_coord(matrix @ self._direction.coord),
        )
    
    def __repr__(self):
        return f"Ray({self._origin}, {self._direction})"


def transform(ray: Ray, transform_matrix: Transformation) -> Ray:
    origin = Point()
    origin.set_coord(transform_matrix @ ray.origin.coord)

    direction = Vector()
    direction.set_coord(transform_matrix @ ray.direction.coord)

    nray = Ray(origin, direction)

    return nray


def position(ray, t) -> Point:
    result = Point()
    result.set_coord(ray.origin.coord + t * ray.direction.coord)

    return result
