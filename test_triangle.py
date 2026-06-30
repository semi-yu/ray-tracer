from pytest import approx

from util.mathematics import Vector, Point
from triangle import Triangle

from entities.ray import Ray


def test_constructing_a_triangle():
    p1 = Point( 0, 1, 0)
    p2 = Point(-1, 0, 0)
    p3 = Point( 1, 0, 0)

    s = Triangle(
        p1,
        p2,
        p3
    )

    assert s.p1.coord == approx(p1.coord)
    assert s.p2.coord == approx(p2.coord)
    assert s.p3.coord == approx(p3.coord)
    
    assert s.e1.coord == approx(Vector(-1, -1, 0).coord, abs=1e-5)
    assert s.e2.coord == approx(Vector( 1, -1, 0).coord, abs=1e-5)
    assert s.normal.coord == approx(Vector(0, 0, -1).coord, abs=1e-5)

def test_finding_the_normal_on_a_triangle():
    s = Triangle(
        Point( 0, 1, 0),
        Point(-1, 0, 0),
        Point( 1, 0, 0),
    )

    n1 = s.local_normal_at(Point(0, 0.5, 0))
    n2 = s.local_normal_at(Point(-0.5, 0.75, 0))
    n3 = s.local_normal_at(Point( 0.5, 0.75, 0))

    assert n1.coord == approx(s.normal.coord, abs=1e-5)
    assert n2.coord == approx(s.normal.coord, abs=1e-5)
    assert n3.coord == approx(s.normal.coord, abs=1e-5)

def test_intersecting_a_ray_parallel_to_the_triangle():
    s = Triangle(
        Point( 0, 1, 0),
        Point(-1, 0, 0),
        Point( 1, 0, 0),
    )

    r = Ray(Point(0, -1, -2), Vector(0, 1, 0))

    xs = s.local_intersect(r)

    assert len(xs) == 0

def test_a_ray_misses_the_p1_to_p3_edge():
    s = Triangle(
        Point( 0, 1, 0),
        Point(-1, 0, 0),
        Point( 1, 0, 0),
    )

    r = Ray(Point(1, 1, -2), Vector(0, 0, 1))

    xs = s.local_intersect(r)

    assert len(xs) == 0

def test_a_ray_misses_the_p1_to_p2_edge():
    s = Triangle(
        Point( 0, 1, 0),
        Point(-1, 0, 0),
        Point( 1, 0, 0),
    )

    r = Ray(Point(-1, 1, -2), Vector(0, 0, 1))

    xs = s.local_intersect(r)

    assert len(xs) == 0

def test_a_ray_misses_the_p2_to_p3_edge():
    s = Triangle(
        Point( 0, 1, 0),
        Point(-1, 0, 0),
        Point( 1, 0, 0),
    )

    r = Ray(Point(0, -1, -2), Vector(0, 0, 1))

    xs = s.local_intersect(r)

    assert len(xs) == 0

def test_a_ray_strikes_a_triangle():
    s = Triangle(
        Point( 0, 1, 0),
        Point(-1, 0, 0),
        Point( 1, 0, 0),
    )

    r = Ray(Point(0, 0.5, -2), Vector(0, 0, 1))

    xs = s.local_intersect(r)
    
    assert len(xs) == 1
    assert xs[0].t == approx(2.0)
