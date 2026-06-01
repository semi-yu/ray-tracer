from pytest import approx
import numpy as np


from util.mathematics import Point, Vector
from util.transformation import Transformation
from entities.ray import Ray, transform


def test_translate_a_ray():
    r = Ray(Point(1, 2, 3), Vector(0, 1, 0))
    t = Transformation().translate(3, 4, 5)

    nray = transform(r, t.matrix)

    assert nray.origin.coord[:3] == approx(np.array([4, 6, 8]))
    assert nray.direction.coord[:3] == approx(np.array([0, 1, 0]))


def test_scale_a_ray():
    r = Ray(Point(1, 2, 3), Vector(0, 1, 0))
    t = Transformation().scale(2, 3, 4)

    nray = transform(r, t.matrix)

    assert nray.origin.coord[:3] == approx(np.array([2, 6, 12]))
    assert nray.direction.coord[:3] == approx(np.array([0, 3, 0]))
