import numpy as np

from pytest import approx

from util.mathematics import Point, Vector
from entities.ray import Ray

from group import Group
from shape import Shape

from util.transformation import Transformation
from sphere import Sphere

from intersect import intersect

def test_creating_a_group():
    g = Group()

    assert g.transform.matrix == approx(np.identity(4))
    assert len(g.shapes) == 0

def test_adding_a_child_to_a_group():
    g = Group()
    s = Shape()

    g.add_child(s)

    assert len(g) != 0
    assert s in g

def test_intersecting_a_ray_with_an_empty_group():
    g = Group()

    ray = Ray(Point(0, 0, 0,), Vector(0, 0, 1))

    xs = g.local_intersect(ray)

    assert len(xs) == 0

def test_intersecting_a_ray_with_a_nonempty_group():
    g = Group()

    s1 = Sphere()
    s2 = Sphere().set_transform(Transformation().translate(0, 0, -3))
    s3 = Sphere().set_transform(Transformation().translate(5, 0, 0))

    g.add_child(s1).add_child(s2).add_child(s3)

    ray = Ray(Point(0, 0, -5), Vector(0, 0, 1))

    xs = g.local_intersect(ray)

    assert len(xs) == 4
    assert xs[0].object == s2
    assert xs[1].object == s2
    assert xs[2].object == s1
    assert xs[3].object == s1

def test_intersecting_a_transformed_group():
    g = Group() \
        .set_transform(
            Transformation()
            .scale(2, 2, 2)
        )
    
    s = Sphere() \
        .set_transform(
            Transformation()
            .translate(5, 0, 0)
        )

    g.add_child(s)

    r = Ray(Point(10, 0, -10), Vector(0, 0, 1))

    xs = intersect(g, r)

    assert len(xs) == 2
