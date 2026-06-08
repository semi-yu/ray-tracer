from pytest import approx

from entities.material import Material


def test_default_material():
    m = Material()

    assert m.ambient == approx(0.1)
    assert m.diffuse == approx(0.9)
    assert m.specular == approx(0.9)
    assert m.shininess == approx(200.0)
