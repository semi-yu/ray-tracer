import math
import numpy as np

from entities.ray import transform


def intersect(shape, ray):
    local_ray = ray.transform(np.linalg.inv(shape.transform.matrix))
    return shape.local_intersect(local_ray)


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
