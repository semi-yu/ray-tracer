import numpy as np

from entities.ray import Ray
from entities.material import Material

from util.transformation import Transformation
from util.mathematics import Vector, Point


class Shape:
    def __init__(self):
        self._transformation = Transformation()
        self._material = Material()

        self._saved_ray = None

    def set_transform(self, transform: Transformation):
        self._transformation = transform
        return self

    def set_material(self, material: Material):
        self._material = material
        return self

    def local_intersect(self, ray: Ray):
        self._saved_ray = ray

        return

    def local_normal_at(self, point: Point) -> Vector:
        return Vector().set_coord(point)

    @property
    def transform(self):
        return self._transformation

    @property
    def material(self):
        return self._material

    @property
    def saved_ray(self):
        return self._saved_ray
