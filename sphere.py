import numpy as np

from intersect import Intersection

from entities.ray import Ray
from material import Material

from util.mathematics import Vector, Point
from util.transformation import Transformation


class Sphere:
    def __init__(self, center: Point = Point(0, 0, 0), radius: float = 1.0):
        self._center = center
        self._radius = radius

        self._transformation = Transformation()

        self._material = Material()

    def set_transform(self, transform):
        self._transformation = transform
        return self

    def set_material(self, material):
        self._material = material
        return self

    def local_intersect(self, ray: Ray):
        diff = ray.origin.coord - self.center.coord

        a = np.dot(ray.direction.coord, ray.direction.coord)
        b = 2 * np.dot(ray.direction.coord, diff)
        c = np.dot(diff, diff) - 1

        discriminant = b * b - 4 * a * c

        if discriminant < 0:
            return []
        else:
            return [
                Intersection((-b - np.sqrt(discriminant)) / (2 * a), self),
                Intersection((-b + np.sqrt(discriminant)) / (2 * a), self),
            ]

    def local_normal_at(self, point: Point) -> Vector:
        return Vector().set_coord(point)

    @property
    def transform(self) -> Transformation:
        return self._transformation

    @property
    def center(self) -> Point:
        return self._center

    @property
    def radius(self) -> float:
        return self._radius

    @property
    def material(self) -> Material:
        return self._material

def glass_sphere():
        return Sphere() \
            .set_material(
                Material(
                    transparency = 1.0,
                    refractive_index = 1.5))
