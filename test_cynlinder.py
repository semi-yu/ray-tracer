from pytest import approx

from entities.ray import Ray
from util.mathematics import Vector, Point
from cylinder import Cylinder

def test_a_ray_misses_a_cylinder():
    s = Cylinder()

    defined_xs = [
        (Point(1, 0,  0), Vector(0, 1, 0), ),
        (Point(0, 0,  0), Vector(0, 1, 0), ),
        (Point(0, 0, -5), Vector(1, 1, 1), ),
    ]

    for origin, direction in defined_xs:
        ray = Ray(origin, direction.normalize())

        xs = s.local_intersect(ray)

        assert len(xs) == 0

def test_a_ray_hits_a_cylinder():
    s = Cylinder()

    defined_xs = [
        (Point(  1, 0, -5), Vector(0, 0, 1), 5, 5), 
        (Point(  0, 0, -5), Vector(0, 0, 1), 4, 6), 
        (Point(0.5, 0, -5), Vector(0.1, 1, 1), 6.80798, 7.08872), 
    ]

    for origin, direction, t1, t2 in defined_xs:
        ray = Ray(origin, direction.normalize())

        xs = s.local_intersect(ray)

        assert len(xs) == 2
        assert xs[0].t == approx(t1)
        assert xs[1].t == approx(t2)
