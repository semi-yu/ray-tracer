import numpy as np

from entities.ray import Ray
from material import Material

from csg import Csg
from intersect import UVIntersection

from util.transformation import Transformation
from util.mathematics import Vector, Point

from group import Group


class Shape:
    def __init__(self):
        self._transformation = Transformation()
        self._material = Material()

        self._saved_ray = None

        self._parent = None

    def set_transform(self, transform: Transformation):
        self._transformation = transform
        return self

    def set_material(self, material: Material):
        self._material = material
        return self
    
    def set_parent(self, group: Group):
        if not isinstance(group, (Group, Csg)):
            raise Exception("A parent must be a group or a csg")
        self._parent = group

    def local_intersect(self, ray: Ray):
        self._saved_ray = ray

        return

    def local_normal_at(self, point: Point, hit: UVIntersection = None) -> Vector:
        return Vector().set_coord(point.coord)

    @property
    def transform(self):
        return self._transformation

    @property
    def material(self):
        return self._material

    @property
    def saved_ray(self):
        return self._saved_ray

    @property
    def parent(self):
        return self._parent
