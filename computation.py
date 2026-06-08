import numpy as np

from util.mathematics import Vector, Point, EPSILON
from entities.normal import normal_at
from entities.ray import position


class Computation:
    def __init__(self, t, object, point, eye, normal, inside, over_point):
        self._t = t
        self._object = object
        self._point = point
        self._eye = eye
        self._normal = normal
        self._inside = inside

        self._over_point = over_point

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

    @property
    def over_point(self):
        return self._over_point


def prepare_computation(intersection, ray):
    v = Vector()
    v.set_coord(-1 * ray.direction.coord)
    p = position(ray, intersection.t)

    n = normal_at(intersection.object, p)
    is_inside = np.dot(n.coord, v.coord) < 0

    n.set_coord(-1 * n.coord if is_inside else n.coord)

    over_point = Point().set_coord(p.coord + n.coord * EPSILON)

    return Computation(
        t=intersection.t,
        object=intersection.object,
        point=p,
        eye=v,
        normal=n,
        inside=is_inside,
        over_point=over_point,
    )
