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

    if comp.n1 > comp.n2:
        n = comp.n1 / comp.n2

        sin2_t = n * n * (1.0 - cos * cos)

        if sin2_t > 1.0: return 1.0

        cos_t = np.sqrt(1.0 - sin2_t)

        cos = cos_t
    
    r0 = ((comp.n1 - comp.n2) / (comp.n1 + comp.n2)) ** 2
    return r0 + (1 - r0) * (1 - cos) ** 5
