from pytest import approx

from util.mathematics import Vector, Point
from entities.ray import Ray

from cube import Cube


def test_a_ray_intersects_a_cube():
    c = Cube()

    defined_xs = [
        (
            Point(5, 0.5, 0),
            Vector(-1, 0, 0),
            4,
            6,
        ),
        (
            Point(-5, 0.5, 0),
            Vector(1, 0, 0),
            4,
            6,
        ),
        (
            Point(0.5, 5, 0),
            Vector(0, -1, 0),
            4,
            6,
        ),
        (
            Point(0.5, -5, 0),
            Vector(0, 1, 0),
            4,
            6,
        ),
        (
            Point(0.5, 0, 5),
            Vector(0, 0, -1),
            4,
            6,
        ),
        (
            Point(0.5, 0, -5),
            Vector(0, 0, 1),
            4,
            6,
        ),
        (
            Point(0, 0.5, 0),
            Vector(0, 0, 1),
            -1,
            1,
        ),
    ]

    for origin, direct, t1, t2 in defined_xs:
        r = Ray(origin, direct)

        xs = c.local_intersect(r)

        assert len(xs) == 2
        assert xs[0].t == t1
        assert xs[1].t == t2


def test_a_ray_misses_a_cube():
    c = Cube()

    defined_xs = [
        (
            Point(-2, 0, 0),
            Vector(0.2673, 0.5345, 0.8018),
        ),
        (
            Point(0, -2, 0),
            Vector(0.8018, 0.2673, 0.5345),
        ),
        (
            Point(0, 0, -2),
            Vector(0.5345, 0.8018, 0.2673),
        ),
        (
            Point(2, 0, 2),
            Vector(0, 0, -1),
        ),
        (
            Point(0, 2, 2),
            Vector(0, -1, 0),
        ),
        (
            Point(2, 2, 0),
            Vector(-1, 0, 0),
        ),
    ]

    for origin, direct in defined_xs:
        r = Ray(origin, direct)

        xs = c.local_intersect(r)

        assert len(xs) == 0


def test_the_normal_on_the_surface_of_a_cube():
    c = Cube()

    defined_ans = [
        (
            Point(1, 0.5, -0.8),
            Vector(1, 0, 0),
        ),
        (
            Point(-1, -0.2, 0.9),
            Vector(-1, 0, 0),
        ),
        (
            Point(-0.4, 1, -0.1),
            Vector(0, 1, 0),
        ),
        (
            Point(0.3, -1, -0.7),
            Vector(0, -1, 0),
        ),
        (
            Point(-0.6, 0.3, 1),
            Vector(0, 0, 1),
        ),
        (
            Point(0.4, 0.4, -1),
            Vector(0, 0, -1),
        ),
        (
            Point(1, 1, 1),
            Vector(1, 0, 0),
        ),
        (
            Point(-1, -1, -1),
            Vector(-1, 0, 0),
        ),
    ]

    for point, normal in defined_ans:
        n = c.local_normal_at(point)

        assert normal.coord == approx(n.coord)
