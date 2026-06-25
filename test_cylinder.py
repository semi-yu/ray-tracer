from pytest import approx

from entities.ray import Ray
from util.mathematics import Vector, Point
from cylinder import Cylinder


def test_a_ray_misses_a_cylinder():
    s = Cylinder()

    defined_xs = [
        (
            Point(1, 0, 0),
            Vector(0, 1, 0),
        ),
        (
            Point(0, 0, 0),
            Vector(0, 1, 0),
        ),
        (
            Point(0, 0, -5),
            Vector(1, 1, 1),
        ),
    ]

    for origin, direction in defined_xs:
        ray = Ray(origin, direction.normalize())

        xs = s.local_intersect(ray)

        assert len(xs) == 0


def test_a_ray_hits_a_cylinder():
    s = Cylinder()

    defined_xs = [
        (Point(1, 0, -5), Vector(0, 0, 1), 5, 5),
        (Point(0, 0, -5), Vector(0, 0, 1), 4, 6),
        (Point(0.5, 0, -5), Vector(0.1, 1, 1), 6.80798, 7.08872),
    ]

    for origin, direction, t1, t2 in defined_xs:
        ray = Ray(origin, direction.normalize())

        xs = s.local_intersect(ray)

        assert len(xs) == 2
        assert xs[0].t == approx(t1)
        assert xs[1].t == approx(t2)


def test_normal_vector_on_a_cylinder():
    s = Cylinder()

    defined_n = [
        (
            Point(1, 0, 0),
            Vector(1, 0, 0),
        ),
        (
            Point(0, 5, -1),
            Vector(0, 0, -1),
        ),
        (
            Point(0, -2, 1),
            Vector(0, 0, 1),
        ),
        (
            Point(-1, 1, 0),
            Vector(-1, 0, 0),
        ),
    ]

    for point, normal in defined_n:
        n = s.local_normal_at(point)

        print(point, normal, n)

        assert normal.coord == approx(n.coord)


def test_the_defulat_minimum_and_maximum_for_a_cylinder():
    s = Cylinder()

    assert s.minimum == approx(float("-inf"))
    assert s.maximum == approx(float("inf"))


def test_intersecting_a_constrained_cylinder():
    s = Cylinder(minimum=1, maximum=2)

    defined_ray = [
        (
            Point(0, 1.5, 0),
            Vector(0.1, 1, 0),
            0,
        ),
        (
            Point(0, 3, -5),
            Vector(0, 0, 1),
            0,
        ),
        (
            Point(0, 0, -5),
            Vector(0, 0, 1),
            0,
        ),
        (
            Point(0, 2, -5),
            Vector(0, 0, 1),
            0,
        ),
        (
            Point(0, 1, -5),
            Vector(0, 0, 1),
            0,
        ),
        (
            Point(0, 1.5, -2),
            Vector(0, 0, 1),
            2,
        ),
    ]

    for origin, direction, count in defined_ray:
        ray = Ray(origin, direction.normalize())

        xs = s.local_intersect(ray)

        assert len(xs) == count


def test_the_default_closed_value_for_a_cylinder():
    s = Cylinder()

    assert s.closed == False


def test_intersecting_the_caps_of_a_closed_cylinder():
    s = Cylinder(minimum=1, maximum=2, closed=True)

    defined_xs = [
        (Point(0, 3, 0), Vector(0, -1, 0), 2),
        (Point(0, 3, -2), Vector(0, -1, 2), 2),
        (Point(0, 4, -2), Vector(0, -1, 1), 2),
        (Point(0, 0, -2), Vector(0, 1, 2), 2),
        (Point(0, -1, -2), Vector(0, 1, 1), 2),
    ]

    for origin, direction, count in defined_xs:
        ray = Ray(origin, direction.normalize())

        xs = s.local_intersect(ray)

        assert len(xs) == count


def test_the_normal_vector_on_a_cylinders_end_caps():
    s = Cylinder(minimum=1, maximum=2, closed=True)

    defined_normal = [
        (
            Point(0, 1, 0),
            Vector(0, -1, 0),
        ),
        (
            Point(0.5, 1, 0),
            Vector(0, -1, 0),
        ),
        (
            Point(0, 1, 0.5),
            Vector(0, -1, 0),
        ),
        (
            Point(0, 2, 0),
            Vector(0, 1, 0),
        ),
        (
            Point(0.5, 2, 0),
            Vector(0, 1, 0),
        ),
        (
            Point(0, 2, 0.5),
            Vector(0, 1, 0),
        ),
    ]

    for point, normal in defined_normal:
        n = s.local_normal_at(point)

        assert normal.coord == approx(n.coord)
