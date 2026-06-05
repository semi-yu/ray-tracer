import math

from pytest import approx
import numpy as np

from util.mathematics import Point, Vector
from entities.ray import Ray
from intersect import prepare_computation
from entities.sphere import Sphere
from intersect import intersect, hit, Intersection


def test_ray_intersects_a_sphere_at_two_points():
    ray = Ray(Point(0, 0, -5), Vector(0, 0, 1))

    sphere = Sphere(Point(0, 0, 0), 1.0)
    xpoints = intersect(sphere, ray)

    assert len(xpoints) == 2
    assert math.isclose(xpoints[0].t, 4.0)
    assert math.isclose(xpoints[1].t, 6.0)
    assert xpoints[0].object is sphere
    assert xpoints[1].object is sphere


def test_ray_intersects_a_sphere_at_a_tangent():
    ray = Ray(Point(0, 1, -5), Vector(0, 0, 1))

    sphere = Sphere(Point(0, 0, 0), 1.0)
    xpoints = intersect(sphere, ray)

    assert len(xpoints) == 2
    assert math.isclose(xpoints[0].t, 5.0)
    assert math.isclose(xpoints[1].t, 5.0)
    assert xpoints[0].object is sphere
    assert xpoints[1].object is sphere


def test_ray_misses_a_sphere():
    ray = Ray(Point(0, 2, -5), Vector(0, 0, 1))

    sphere = Sphere(Point(0, 0, 0), 1.0)
    xpoints = intersect(sphere, ray)

    assert len(xpoints) == 0


def test_ray_originates_inside_a_sphere():
    ray = Ray(Point(0, 0, 0), Vector(0, 0, 1))

    sphere = Sphere(Point(0, 0, 0), 1.0)
    xpoints = intersect(sphere, ray)

    assert len(xpoints) == 2
    assert math.isclose(xpoints[0].t, -1.0)
    assert math.isclose(xpoints[1].t, 1.0)
    assert xpoints[0].object is sphere
    assert xpoints[1].object is sphere


def test_sphere_is_behind_a_ray():
    ray = Ray(Point(0, 0, 5), Vector(0, 0, 1))

    sphere = Sphere(Point(0, 0, 0), 1.0)
    xpoints = intersect(sphere, ray)

    assert len(xpoints) == 2
    assert math.isclose(xpoints[0].t, -6.0)
    assert math.isclose(xpoints[1].t, -4.0)
    assert xpoints[0].object is sphere
    assert xpoints[1].object is sphere


def test_hit_when_all_intersections_have_positive_t():
    sphere = Sphere(Point(0, 0, 0), 1.0)

    xpoints = [
        Intersection(1, sphere),
        Intersection(2, sphere),
    ]

    h = hit(xpoints)

    assert h is xpoints[0]


def test_hit_when_some_intersections_have_negative_t():
    sphere = Sphere(Point(0, 0, 0), 1.0)

    xpoints = [
        Intersection(-1, sphere),
        Intersection(1, sphere),
    ]

    h = hit(xpoints)

    assert h is xpoints[1]


def test_hit_when_all_intersections_have_negative_t():
    sphere = Sphere(Point(0, 0, 0), 1.0)

    xpoints = [
        Intersection(-2, sphere),
        Intersection(-1, sphere),
    ]

    h = hit(xpoints)

    assert h is None


def test_hit_is_always_the_lowest_nonnegative_intersection():
    sphere = Sphere(Point(0, 0, 0), 1.0)

    xpoints = [
        Intersection(5, sphere),
        Intersection(7, sphere),
        Intersection(-3, sphere),
        Intersection(2, sphere),
    ]

    h = hit(xpoints)

    assert h is xpoints[3]


def test_precompute_the_state_of_an_intersection():
    s = Sphere(Point(0, 0, 0), 1.0)

    r = Ray(Point(0, 0, -5), Vector(0, 0, 1))

    i = Intersection(4, s)

    comps = prepare_computation(i, r)

    assert comps.t == i.t
    assert comps.object == i.object
    assert comps.point.coord == approx(Point(0, 0, -1).coord)
    assert comps.eye.coord == approx(Vector(0, 0, -1).coord)
    assert comps.normal.coord == approx(Vector(0, 0, -1).coord)
    assert comps.inside == False


def test_the_hit_when_an_intersection_occurs_on_the_outside():
    s = Sphere(Point(0, 0, 0), 1.0)

    r = Ray(Point(0, 0, -5), Vector(0, 0, 1))

    i = Intersection(4, s)

    comps = prepare_computation(i, r)

    assert comps.inside == False


def test_the_hit_when_an_intersection_occurs_on_the_inside():
    s = Sphere(Point(0, 0, 0), 1.0)

    r = Ray(Point(0, 0, 0), Vector(0, 0, 1))

    i = Intersection(1, s)

    comps = prepare_computation(i, r)

    assert comps.point.coord == approx(Point(0, 0, 1).coord)
    assert comps.eye.coord == approx(Vector(0, 0, -1).coord)
    assert comps.inside == True
    assert comps.normal.coord == approx(Vector(0, 0, -1).coord)
