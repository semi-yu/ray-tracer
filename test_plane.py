from pytest import approx

from entities.ray import Ray

from util.mathematics import Vector, Point
from plane import Plane


def test_the_normal_of_a_plane_is_constant_everywhere():
    p = Plane()

    assert p.local_normal_at(Point(0, 0, 0)).coord == approx(Vector(0, 1, 0).coord)
    assert p.local_normal_at(Point(10, 0, -10)).coord == approx(Vector(0, 1, 0).coord)
    assert p.local_normal_at(Point(-5, 0, 150)).coord == approx(Vector(0, 1, 0).coord)


def test_intersecting_with_a_ray_parallel_to_the_plane():
    p = Plane()

    r = Ray(Point(0, 10, 0), Vector(0, 0, 1))

    xs = p.local_intersect(r)

    assert len(xs) == 0


def test_intersecting_with_a_ray_coplanar_ray():
    p = Plane()

    r = Ray(Point(0, 0, 0), Vector(0, 0, 1))

    xs = p.local_intersect(r)

    assert len(xs) == 0


def test_intersecting_with_a_ray_coplanar_ray():
    p = Plane()

    r = Ray(Point(0, 1, 0), Vector(0, -1, 0))

    xs = p.local_intersect(r)

    assert len(xs) == 1
    assert xs[0].t == 1
    assert xs[0].object == p


def test_intersecting_with_a_ray_coplanar_ray():
    p = Plane()

    r = Ray(Point(0, -1, 0), Vector(0, 1, 0))

    xs = p.local_intersect(r)

    assert len(xs) == 1
    assert xs[0].t == 1
    assert xs[0].object == p
