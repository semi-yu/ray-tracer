import math
from pytest import approx
import numpy as np

from entities.ray import Ray
from util.mathematics import Vector, Point
from cone import Cone


def test_intersecting_a_cone_with_a_ray():
    s = Cone()

    defined_xs = [
        (Point(0, 0, -5), Vector(0, 0, 1), 5, 5),
        (Point(0, 0, -5), Vector(1, 1, 1), 8.66025, 8.66025),
        (Point(1, 1, -5), Vector(-0.5, -1, 1), 4.55006, 49.44994),
    ]

    for origin, direction, t1, t2 in defined_xs:
        ray = Ray(origin, direction.normalize())

        xs = s.local_intersect(ray)

        assert len(xs) == 2
        assert xs[0].t == approx(t1)
        assert xs[1].t == approx(t2)


def test_intersecting_a_cone_with_a_ray_parallel_to_one_of_its_halves():
    s = Cone()

    ray = Ray(Point(0, 0, -1), Vector(0, 1, 1).normalize())

    xs = s.local_intersect(ray)

    assert len(xs) == 1
    assert xs[0].t == approx(0.35355, abs=1e-5)


def test_intersecting_a_cones_end_caps():
    s = Cone(minimum=-0.5, maximum=0.5, closed=True)

    defined_xs = [
        (
            Point(0, 0, -5),
            Vector(0, 1, 0),
            0,
        ),
        (
            Point(0, 0, -0.25),
            Vector(0, 1, 1),
            2,
        ),
        (
            Point(0, 0, -0.25),
            Vector(0, 1, 0),
            4,
        ),
    ]

    for origin, direction, count in defined_xs:
        ray = Ray(origin, direction.normalize())

        xs = s.local_intersect(ray)

        assert len(xs) == count


def test_computing_the_normal_vector_on_a_cone():
    s = Cone()

    defined_normal = [
        (
            Point(0, 0, 0),
            Vector(0, 0, 0),
        ),
        (
            Point(1, 1, 1),
            Vector(1, -np.sqrt(2), 1),
        ),
        (
            Point(-1, -1, 0),
            Vector(-1, 1, 0),
        ),
    ]

    for point, normal in defined_normal:
        n = s.local_normal_at(point)

        assert normal.coord == approx(n.coord)
