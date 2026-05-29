import numpy as np

from util.mathematics import Point
from util.transformation import Transformation


class Sphere:
    def __init__(self, center: Point, radius):
        self._center = center
        self._radius = radius

        self._transform = Transformation()

    def set_transform(self, transform):
        self._transform = transform

    @property
    def transform(self) -> Transformation:
        return self._transform

    @property
    def center(self) -> Point:
        return self._center

    @property
    def radius(self) -> float:
        return self._radius
