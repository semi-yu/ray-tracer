import numpy as np
from pytest import approx

from util.mathematics import Point, Vector
from util.transformation import Transformation

from entities.ray import Ray, transform
from entities.sphere import Sphere
from entities.material import Material

from intersect import intersect


def test_default_transformation_of_a_sphere():
    s = Sphere(Point(0, 0, 0), 1.0)

    assert s.transform.matrix == approx(np.identity(4))


def test_changing_transformation_of_a_sphere():
    s = Sphere(Point(0, 0, 0), 1.0)

    t = Transformation().translate(2, 3, 4)

    s.set_transform(t)

    assert s.transform.matrix == approx(t.matrix)


def test_sphere_default_transformation():
    s = Sphere(Point(0, 0, 0), 1.0)

    t = Transformation()

    assert s.transform.matrix == approx(t.matrix)


def test_changing_sphere_transformation():
    s = Sphere(Point(0, 0, 0), 1.0)

    t = Transformation().translate(2, 3, 4)

    s.set_transform(t)

    assert s.transform.matrix == approx(t.matrix)


def test_intersecting_a_scaled_sphere_with_a_ray():
    s = Sphere(Point(0, 0, 0), 1.0)

    r = Ray(Point(0, 0, -5), Vector(0, 0, 1))

    t = Transformation().scale(2, 2, 2)

    s.set_transform(t)

    xpoints = intersect(s, r)

    assert len(xpoints) == 2
    assert xpoints[0].t == 3
    assert xpoints[1].t == 7


def test_intersecting_a_translated_sphere_with_a_ray():
    s = Sphere(Point(0, 0, 0), 1.0)

    r = Ray(Point(0, 0, -5), Vector(0, 0, 1))

    t = Transformation().translate(5, 0, 0)

    s.set_transform(t)

    xpoints = intersect(s, r)

    assert len(xpoints) == 0


def test_a_sphere_has_a_default_material():
    s = Sphere(Point(0, 0, 0), 1.0)

    m = Material()

    assert s.material.ambient == approx(m.ambient)
    assert s.material.diffuse == approx(m.diffuse)
    assert s.material.specular == approx(m.specular)
    assert s.material.shininess == approx(m.shininess)


def test_a_sphere_may_be_assigned_a_material():
    s = Sphere(Point(0, 0, 0), 1.0)

    m = Material(ambient=1.0)

    s.set_material(m)

    assert s.material.ambient == approx(m.ambient)
    assert s.material.diffuse == approx(m.diffuse)
    assert s.material.specular == approx(m.specular)
    assert s.material.shininess == approx(m.shininess)
