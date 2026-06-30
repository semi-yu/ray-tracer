from pytest import approx
from triangle import Triangle
from util.mathematics import Vector, Point

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

