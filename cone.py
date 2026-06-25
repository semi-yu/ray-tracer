import math
import numpy as np

from entities.ray import Ray
from util.mathematics import Vector, Point

from intersect import Intersection
from shape import Shape


def check_cap(ray, t, y):
    x = ray.origin.x + t * ray.direction.x
    z = ray.origin.z + t * ray.direction.z

    return (x * x + z * z) <= abs(y)


class Cone(Shape):
    def __init__(
        self,
        minimum: float = float("-inf"),
        maximum: float = float("inf"),
        closed=False,
    ):
        self._minimum = minimum
        self._maximum = maximum
        self._closed = closed

    def local_intersect(self, ray: Ray) -> list[Intersection]:
        a = ray.direction.x**2 - ray.direction.y**2 + ray.direction.z**2
        b = 2 * (
            ray.origin.x * ray.direction.x
            - ray.origin.y * ray.direction.y
            + ray.origin.z * ray.direction.z
        )
        c = ray.origin.x**2 - ray.origin.y**2 + ray.origin.z**2

        xs = []

        if math.isclose(a, 0.0):
            if not math.isclose(b, 0.0):
                t = -c / (2 * b)
                y = ray.origin.y + t * ray.direction.y
                if self._minimum < y < self._maximum:
                    xs.append(Intersection(t, self))
        else:
            disc = b**2 - 4 * a * c
            if disc < 0:
                return []

            t1 = (-b - np.sqrt(disc)) / (2 * a)
            t2 = (-b + np.sqrt(disc)) / (2 * a)

            if t1 > t2:
                t1, t2 = t2, t1

            y0 = ray.origin.y + t1 * ray.direction.y
            if self._minimum < y0 < self._maximum:
                xs.append(Intersection(t1, self))

            y1 = ray.origin.y + t2 * ray.direction.y
            if self._minimum < y1 < self._maximum:
                xs.append(Intersection(t2, self))

        self.intersect_caps(ray, xs)
        return xs

    def intersect_caps(self, ray: Ray, xs: list[Intersection]) -> None:
        if not self._closed or math.isclose(ray.direction.y, 0.0):
            return

        t = (self.minimum - ray.origin.y) / ray.direction.y
        if check_cap(ray, t, self.minimum):
            xs.append(Intersection(t, self))

        t = (self.maximum - ray.origin.y) / ray.direction.y
        if check_cap(ray, t, self.maximum):
            xs.append(Intersection(t, self))

    def local_normal_at(self, point: Point) -> Vector:
        dist = point.x**2 + point.z**2

        if dist < abs(point.y) and point.y >= self.maximum - 1e-5:
            return Vector(0, 1, 0)

        if dist < abs(point.y) and point.y <= self.minimum + 1e-5:
            return Vector(0, -1, 0)

        y = np.sqrt(dist)
        if point.y > 0:
            y = -y

        if math.isclose(point.x, 0.0) and math.isclose(point.z, 0.0):
            return Vector(0, 0, 0)

        return Vector(point.x, y, point.z)

    @property
    def minimum(self):
        return self._minimum

    @property
    def maximum(self):
        return self._maximum

    @property
    def closed(self):
        return self._closed
