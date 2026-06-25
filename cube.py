import numpy as np

from util.mathematics import Vector, Point, EPSILON
from intersect import Intersection
from entities.ray import Ray
from shape import Shape

from material import Material
from util.transformation import Transformation


def check_axis(origin: Point, direction: Vector):
    tmin_numerator = -1 - origin
    tmax_numerator = 1 - origin

    if abs(direction) >= EPSILON:
        tmin = tmin_numerator / direction
        tmax = tmax_numerator / direction
    else:
        tmin = tmin_numerator * float("inf")
        tmax = tmax_numerator * float("inf")

    if tmin > tmax:
        tmin, tmax = tmax, tmin

    return tmin, tmax


class Cube(Shape):
    def __init__(self):
        self._transformation = Transformation()
        self._material = Material()

    def local_intersect(self, ray: Ray) -> list[Intersection]:
        xtmin, xtmax = check_axis(ray.origin.x, ray.direction.x)
        ytmin, ytmax = check_axis(ray.origin.y, ray.direction.y)
        ztmin, ztmax = check_axis(ray.origin.z, ray.direction.z)

        tmin = max(xtmin, ytmin, ztmin)
        tmax = min(xtmax, ytmax, ztmax)

        if tmin > tmax:
            return []

        return [
            Intersection(tmin, self),
            Intersection(tmax, self),
        ]

    def local_normal_at(self, point: Point) -> Vector:
        maxc = max(abs(point.x), abs(point.y), abs(point.z))

        if maxc == abs(point.x):
            return Vector(point.x, 0, 0)
        elif maxc == abs(point.y):
            return Vector(0, point.y, 0)
        else:
            return Vector(0, 0, point.z)
