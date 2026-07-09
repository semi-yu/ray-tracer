from intersect import UVIntersection

from entities.ray import Ray
from util.mathematics import Vector, Point, EPSILON
from shape import Shape


class Plane(Shape):
    def __init__(self):
        super().__init__()

    def local_normal_at(self, point: Point, hit = None) -> Vector:
        return Vector(0, 1, 0)

    def local_intersect(self, ray: Ray) -> list[UVIntersection]:
        if abs(ray.direction.y) < EPSILON:
            return []

        t = -ray.origin.y / ray.direction.y
        return [UVIntersection(t, self)]
