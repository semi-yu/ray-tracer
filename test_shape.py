import numpy as np
from pytest import approx

from entities.normal import normal_at, normal_to_world, world_to_object
from material import Material

from util.mathematics import Vector, Point
from util.transformation import Transformation

from group import Group

from shape import Shape
from sphere import Sphere


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

def test_converting_a_point_from_world_to_object_space():
    g1 = Group() \
         .set_transform(
             Transformation().rotate(np.pi / 2, axis = 'y')
         )

    g2 = Group() \
         .set_transform(
             Transformation().scale(2, 2, 2)
         )

    g1.add_child(g2)

    s = Sphere() \
        .set_transform(
            Transformation().translate(5, 0, 0)
        )
    
    g2.add_child(s)

    p = world_to_object(s, Point(-2, 0, -10))

    assert p.coord == approx(Point(0, 0, -1).coord)

def test_converting_a_normal_from_object_to_world_space():
    g1 = Group() \
        .set_transform(
            Transformation().rotate(np.pi / 2, axis = 'y')
        )
    
    g2 = Group() \
        .set_transform(
            Transformation().scale(1, 2, 3)
        )
    
    g1.add_child(g2)

    s = Sphere() \
        .set_transform(
            Transformation().translate(5, 0, 0)
        )
    
    g2.add_child(s)

    n = normal_to_world(s, Vector(np.sqrt(3) / 3, np.sqrt(3) / 3, np.sqrt(3) / 3))

    assert n.coord == approx(Vector(0.2857, 0.4286, -0.8571).coord, abs=1e-4)

def test_finding_the_normal_on_a_child_object():
    g1 = Group() \
        .set_transform(
            Transformation().rotate(np.pi / 2, axis = 'y')
        )
    
    g2 = Group() \
        .set_transform(
            Transformation().scale(1, 2, 3)
        )
    
    g1.add_child(g2)

    s = Sphere() \
        .set_transform(
            Transformation().translate(5, 0, 0)
        )
    
    g2.add_child(s)

    n = normal_at(s, Vector(1.7321, 1.1547, -5.5774))

    assert n.coord == approx(Vector(0.2857, 0.4286, -0.8571).coord, abs=1e-4)
