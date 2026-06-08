import math
import numpy as np

from entities.ray import transform


def intersect(sphere, ray):
    inverse = sphere.transform.inverse()

    nray = transform(ray, inverse)
    diff = nray.origin.coord - sphere.center.coord

    a = np.dot(nray.direction.coord, nray.direction.coord)
    b = 2 * np.dot(nray.direction.coord, diff)
    c = np.dot(diff, diff) - 1

    discriminant = b * b - 4 * a * c

    if discriminant < 0:
        return []
    else:
        return [
            Intersection((-b - math.sqrt(discriminant)) / (2 * a), sphere),
            Intersection((-b + math.sqrt(discriminant)) / (2 * a), sphere),
        ]


class Intersection:
    def __init__(self, t: float, object):
        self._t = t
        self._object = object

    @property
    def t(self):
        return self._t

    @property
    def object(self):
        return self._object


def intersect_world(world, ray) -> list[Intersection]:
    result = []

    for object in world.objects:
        result += intersect(object, ray)

    result.sort(key=lambda s: s.t)

    return result
