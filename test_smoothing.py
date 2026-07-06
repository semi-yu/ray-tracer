from pytest import approx

from util.mathematics import Vector, Point

from triangle import Triangle
from smoothing import SmoothTriangle

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
