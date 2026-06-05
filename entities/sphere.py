import numpy as np

from .material import Material

from util.mathematics import Point
from util.transformation import Transformation


class Sphere:
    def __init__(self, center: Point = Point(0, 0, 0), radius: float = 1.0):
        self._center = center
        self._radius = radius

        self._transform = Transformation()

        self._material = Material()

    def set_transform(self, transform):
        self._transform = transform
        return self

    def set_material(self, material):
        self._material = material
        return self

    @property
    def transform(self) -> Transformation:
        return self._transform

    @property
    def center(self) -> Point:
        return self._center

    @property
    def radius(self) -> float:
        return self._radius

    @property
    def material(self) -> Material:
        return self._material
