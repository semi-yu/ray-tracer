import math 
import numpy as np

from util.mathematics import Vector, Point

from entities.ray import Ray
from intersect import Intersection

from shape import Shape

class Cylinder(Shape):
    def local_intersect(self, ray: Ray) -> list[Intersection]:
        a = ray.direction.x * ray.direction.x + ray.direction.z * ray.direction.z

        if math.isclose(a, 0.0): return []

        b = 2 * (ray.origin.x * ray.direction.x + ray.origin.z * ray.direction.z)
        c = ray.origin.x * ray.origin.x + ray.origin.z * ray.origin.z - 1

        disc = b * b - 4 * a * c

        if disc < 0: return []

        t1 = (-b - np.sqrt(disc)) / (2 * a)
        t2 = (-b + np.sqrt(disc)) / (2 * a)

        return [Intersection(t1, self), Intersection(t2, self)]
