from pytest import approx

from image.canvas import Color
from material import Material
from util.mathematics import Vector, Point, EPSILON

from pattern import StripePattern
from light import Light, lighting


def test_default_material():
    m = Material()

    assert m.ambient == approx(0.1)
    assert m.diffuse == approx(0.9)
    assert m.specular == approx(0.9)
    assert m.shininess == approx(200.0)

def testS_lighting_with_a_pattern_applied():
    p = StripePattern(Color(1.0, 1.0, 1.0), Color(0.0, 0.0, 0.0))

    m = Material(
        ambient = 1.0,
        diffuse = 0.0,
        specular = 0.0,
        pattern = p
    )

    eye_vector = Vector(0, 0, -1.0)

    normal_vector = Vector(0, 0, -1.0)

    light = Light(
        Point(0, 0, -10.0),
        Color(1.0, 1.0, 1.0)
    )

    c1 = lighting(m, light, Point(0.9, 0, 0), eye_vector, normal_vector, False)
    c2 = lighting(m, light, Point(1.1, 0, 0), eye_vector, normal_vector, False)

    assert c1 == approx(Color(1.0, 1.0, 1.0), abs=EPSILON)
    assert c2 == approx(Color(0.0, 0.0, 0.0), abs=EPSILON)
