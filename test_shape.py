import numpy as np
from pytest import approx

from intersect import intersect

from entities.ray import Ray

from entities.normal import normal_at
from material import Material

from util.mathematics import Vector, Point
from util.transformation import Transformation


from shape import Shape


def test_default_transformation():
    s = Shape()

    assert s.transform.matrix == approx(np.identity(4))


def test_assigning_transformation():
    s = Shape().set_transform(Transformation().translate(2, 3, 4))

    t = Transformation().translate(2, 3, 4)

    assert s.transform.matrix == approx(t.matrix)


def test_default_material():
    s = Shape()

    m = Material()

    assert s.material.color.arrayize() == approx(m.color.arrayize())
    assert s.material.ambient == approx(m.ambient)
    assert s.material.diffuse == approx(m.diffuse)
    assert s.material.specular == approx(m.specular)
    assert s.material.shininess == approx(m.shininess)


def test_assigning_material():
    m = Material(ambient=1.0)

    s = Shape().set_material(m)

    assert s.material.color.arrayize() == approx(m.color.arrayize())
    assert s.material.ambient == approx(m.ambient)
    assert s.material.diffuse == approx(m.diffuse)
    assert s.material.specular == approx(m.specular)
    assert s.material.shininess == approx(m.shininess)

def test_shape_has_a_parent_attribute():
    s = Shape()

    assert s.parent is None
