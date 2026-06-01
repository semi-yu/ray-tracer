import math
from pytest import approx

from util.mathematics import Vector

from reflect import reflect


def test_reflecting_a_vector_approaching_at_45():
    v = Vector(1, -1, 0)

    n = Vector(0, 1, 0)

    r = reflect(v, n)

    assert r.coord == approx(Vector(1, 1, 0).coord)


def test_reflecting_a_vector_slanted():
    v = Vector(0, -1, 0)

    n = Vector(math.sqrt(2) / 2, math.sqrt(2) / 2, 0)

    r = reflect(v, n)

    assert r.coord == approx(Vector(1, 0, 0).coord)
