from pytest import approx

from entities.sphere import Sphere

from image.canvas import Color
from util.mathematics import Point

from entities.light import Light
from entities.material import Material


def test_default_material():
    m = Material()

    assert m.ambient == approx(0.1)
    assert m.diffuse == approx(0.9)
    assert m.specular == approx(0.9)
    assert m.shininess == approx(200.0)
