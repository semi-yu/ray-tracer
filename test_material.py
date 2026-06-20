from pytest import approx

from image.canvas import Color
from material import Material
from util.mathematics import Vector, Point, EPSILON

from pattern import StripePattern
from light import Light, lighting

from sphere import Sphere, glass_sphere

def test_default_material():
    m = Material()

    assert m.ambient == approx(0.1)
    assert m.diffuse == approx(0.9)
    assert m.specular == approx(0.9)
    assert m.shininess == approx(200.0)


def test_lighting_with_a_pattern_applied():
    p = StripePattern(Color(1.0, 1.0, 1.0), Color(0.0, 0.0, 0.0))

    m = Material(ambient=1.0, diffuse=0.0, specular=0.0, pattern=p)

    eye_vector = Vector(0, 0, -1.0)

    normal_vector = Vector(0, 0, -1.0)

    light = Light(Point(0, 0, -10.0), Color(1.0, 1.0, 1.0))

    c1 = lighting(m, light, Point(0.9, 0, 0), eye_vector, normal_vector, False, object = Sphere())
    c2 = lighting(m, light, Point(1.1, 0, 0), eye_vector, normal_vector, False, object = Sphere())

    assert c1.arrayize() == approx(Color(1.0, 1.0, 1.0).arrayize(), abs=EPSILON)
    assert c2.arrayize() == approx(Color(0.0, 0.0, 0.0).arrayize(), abs=EPSILON)

def test_reflectivity_for_the_default_material():
    m = Material()
    
    assert m.reflective == approx(0.0)

def test_transparency_and_reflective_index_for_the_default_material():
    m = Material()

    assert m.transparency == approx(0.0)
    assert m.reflective_index == approx(1.0)

def test_a_helper_for_producing_a_sphere_with_a_glassy_material():    
    s = glass_sphere()

    assert s.material.transparency == approx(1.0)
    assert s.material.reflective_index == approx(1.5)
