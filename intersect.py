import math

import numpy as np

from image.canvas import Color
from util.mathematics import Vector
from entities.normal import normal_at
from entities.ray import transform, position, Ray
from entities.light import shade_hit

from world import World


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


def hit(xpoints: list[Intersection]):
    nonnegatives = filter(lambda x: x.t > 0, xpoints)
    return min(nonnegatives, key=lambda x: x.t, default=None)


def intersect_world(world, ray) -> list[Intersection]:
    result = []

    for object in world.objects:
        result += intersect(object, ray)

    result.sort(key=lambda s: s.t)

    return result


class Computation:
    def __init__(self, t, object, point, eye, normal, inside):
        self._t = t
        self._object = object
        self._point = point
        self._eye = eye
        self._normal = normal
        self._inside = inside

    @property
    def t(self):
        return self._t

    @property
    def object(self):
        return self._object

    @property
    def point(self):
        return self._point

    @property
    def eye(self):
        return self._eye

    @property
    def normal(self):
        return self._normal

    @property
    def inside(self):
        return self._inside


def prepare_computation(intersection, ray):
    v = Vector()
    v.set_coord(-1 * ray.direction.coord)
    p = position(ray, intersection.t)

    n = normal_at(intersection.object, p)
    is_inside = np.dot(n.coord, v.coord) < 0

    n.set_coord(-1 * n.coord if is_inside else n.coord)

    return Computation(
        t=intersection.t,
        object=intersection.object,
        point=p,
        eye=v,
        normal=n,
        inside=is_inside,
    )


def color_at(world: World, ray: Ray):
    mhit = hit(intersect_world(world, ray))

    if mhit is None:
        return Color(0.0, 0.0, 0.0)

    comps = prepare_computation(mhit, ray)

    return shade_hit(world, comps)
