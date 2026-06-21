import numpy as np


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

def schlick(comp):
    cos = comp.eye.dot(comp.normal)
    print(cos)

    if comp.n1 > comp.n2:
        n = comp.n1 / comp.n2

        sin2_t = n * n * (1.0 - cos * cos)

        if sin2_t > 1.0: return 1.0

    return 0.0
