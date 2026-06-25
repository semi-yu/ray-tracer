import math 
import numpy as np

from util.mathematics import Vector, Point, EPSILON

from entities.ray import Ray
from intersect import Intersection

from shape import Shape

def check_cap(ray, t):
    x = ray.origin.x + t * ray.direction.x
    z = ray.origin.z + t * ray.direction.z

    return (x * x + z * z) <= 1


class Cylinder(Shape):
    def __init__(self, minimum: float = float('-inf'), maximum: float = float('inf'), closed = False):
        self._minimum = minimum
        self._maximum = maximum
        self._closed = closed

    def local_intersect(self, ray: Ray) -> list[Intersection]:
        a = ray.direction.x * ray.direction.x + ray.direction.z * ray.direction.z
        
        xs = []

        if not math.isclose(a, 0.0):
            b = 2 * (ray.origin.x * ray.direction.x + ray.origin.z * ray.direction.z)
            c = ray.origin.x * ray.origin.x + ray.origin.z * ray.origin.z - 1

            disc = b * b - 4 * a * c

            if disc < 0: return []

            t1 = (-b - np.sqrt(disc)) / (2 * a)
            t2 = (-b + np.sqrt(disc)) / (2 * a)

            if t1 > t2: t1, t2 = t2, t1

            y0 = ray.origin.y + t1 * ray.direction.y
            if self._minimum < y0 < self._maximum:
                xs.append(Intersection(t1, self))

            y1 = ray.origin.y + t2 * ray.direction.y
            if self._minimum < y1 < self._maximum:
                xs.append(Intersection(t2, self))

        self.intersect_caps(ray, xs)

        return xs

    def local_normal_at(self, point: Point) -> Vector:
        dist = point.x * point.x + point.z * point.z
        
        if dist < 1.0 and point.y >= self.maximum - EPSILON:
            return Vector(0,  1, 0)
        
        if dist < 1.0 and point.y <= self.minimum + EPSILON:
            return Vector(0, -1, 0)

        return Vector(point.x, 0, point.z)

    def intersect_caps(self, ray: Ray, xs: list[Intersection]) -> None:
        if not self._closed or math.isclose(ray.direction.y, 0.0):
            return

        t = (self.minimum - ray.origin.y) / ray.direction.y
        if check_cap(ray, t): xs.append(Intersection(t, self))

        t = (self.maximum - ray.origin.y) / ray.direction.y
        if check_cap(ray, t): xs.append(Intersection(t, self))


    @property
    def minimum(self): 
        return self._minimum

    @property
    def maximum(self):
        return self._maximum

    @property
    def closed(self):
        return self._closed
