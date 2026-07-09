from pytest import approx

from entities.ray import Ray
from util.mathematics import Vector, Point

from triangle import Triangle, SmoothTriangle
from intersect import UVIntersection

from computation import prepare_computation

from entities.normal import normal_at

def generate_triangle():
    tri = SmoothTriangle(
        Point(0, 1, 0), Point(-1, 0, 0), Point(1, 0, 0),
        Vector(0, 1, 0), Vector(-1, 0, 0), Vector(1, 0, 0), 
    )

    return tri

def test_contructing_a_smooth_triangle():
    s = generate_triangle()

    assert s.p1.coord == approx(Point(0, 1, 0).coord, abs=1e-5)
    assert s.p2.coord == approx(Point(-1, 0, 0).coord, abs=1e-5)
    assert s.p3.coord == approx(Point(1, 0, 0).coord, abs=1e-5)
    assert s.n1.coord == approx(Vector(0, 1, 0).coord, abs=1e-5)
    assert s.n2.coord == approx(Vector(-1, 0, 0).coord, abs=1e-5)
    assert s.n3.coord == approx(Vector(1, 0, 0).coord, abs=1e-5)

def test_an_intersection_can_encapsulate_u_and_v():
    s = Triangle(
        Point(0, 1, 0), Point(-1, 0, 0), Point(1, 0, 0)
    )

    i = UVIntersection(3.5, s, 0.2, 0.4)

    assert i.u == approx(0.2)
    assert i.v == approx(0.4)

def test_an_intersection_with_a_smooth_triangle_stores_u_and_v():
    s = generate_triangle()

    r = Ray(Point(-0.2, 0.3, -2), Vector(0, 0, 1))

    xs = s.local_intersect(r)

    assert xs[0].u == approx(0.45)
    assert xs[0].v == approx(0.25)

def test_a_smooth_triangle_uses_u_and_v_to_interpolate_the_normal():
    s = generate_triangle()

    i = UVIntersection(1, s, 0.45, 0.25)

    n = normal_at(s, Point(0, 0, 0), i)

    assert n.coord == approx(Vector(-0.5547, 0.83205, 0.0).coord)

def test_preparing_the_normal_on_a_smooth_triangle():
    s = generate_triangle()

    i = UVIntersection(1, s, 0.45, 0.25)

    xs = [i]
    r = Ray(Point(-0.2, 0.3, -2), Vector(0, 0, 1))

    comps = prepare_computation(i, r, xs)

    assert comps.normal.coord == approx(Vector(-0.5547, 0.83205, 0.0).coord)
