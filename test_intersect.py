import numpy as np
import math

from pytest import approx

from util.mathematics import Point, Vector, EPSILON
from entities.ray import Ray
from sphere import Sphere, glass_sphere
from plane import Plane
from intersect import intersect, Intersection
from util.transformation import Transformation

from computation import prepare_computation
from shadow import hit


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


def test_the_hit_should_offset_the_point():
    r = Ray(Point(0, 0, -5), Vector(0, 0, 1))
    s = Sphere().set_transform(Transformation().translate(0, 0, 1))

    i = Intersection(5, s)

    comps = prepare_computation(i, r)

    assert comps.over_point.z < -EPSILON / 2
    assert comps.point.z > comps.over_point.z

def test_precomputing_the_reflection_vector():
    s = Plane()

    r = Ray(Point(0, 1, -1), Vector(0, -np.sqrt(2) / 2, np.sqrt(2) / 2))
    
    i = Intersection(np.sqrt(2), s)

    comps = prepare_computation(i, r)

    assert comps.reflect.coord == approx(Vector(0, np.sqrt(2) / 2, np.sqrt(2) / 2).coord)

def test_finding_n1_and_n2_at_various_intersections():
    a = glass_sphere() \
        .set_transform(
            Transformation()
            .scale(2, 2, 2)
        )
    a.material.set_reflective_index(1.5)

    b = glass_sphere() \
        .set_transform(
            Transformation()
            .translate(0, 0, -0.25)
        )
    b.material.set_reflective_index(2.0)

    c = glass_sphere() \
        .set_transform(
            Transformation()
            .translate(0, 0, 0.25)
        )
    c.material.set_reflective_index(2.5)

    r = Ray(Point(0, 0, -4), Vector(0, 0, 1))

    xs = [
        Intersection(2, a),
        Intersection(2.75, b),
        Intersection(3.25, c),
        Intersection(4.75, b),
        Intersection(5.25, c),
        Intersection(6, a),
    ]

    ns = [
        (1.0, 1.5),
        (1.5, 2.0),
        (2.0, 2.5), 
        (2.5, 2.5), 
        (2.5, 1.5),  
        (1.5, 1.0), 
    ]

    n_ans = len(ns)

    for idx in range(n_ans):
        comps = prepare_computation(xs[idx], r, xs)
        n1, n2 = ns[idx]
        
        assert comps.n1 == n1
        assert comps.n2 == n2
