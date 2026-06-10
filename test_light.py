import numpy as np
from pytest import approx

from material import Material
from image.canvas import Color
from util.mathematics import Point, Vector, EPSILON

from light import Light, lighting


def test_point_light_has_a_position_and_intensity():
    point = Point(0, 0, 0)
    color = Color(1.0, 1.0, 1.0)

    l = Light(point, color)

    assert l.position.coord == approx(point.coord, abs=EPSILON)
    assert l.intensity.arrayize() == approx(color.arrayize(), abs=EPSILON)


def test_lighting_with_the_eye_between_the_light_and_the_surface():
    m = Material()
    pos = Point(0, 0, 0)

    eye = Vector(0, 0, -1)
    normal = Vector(0, 0, -1)

    light = Light(Point(0, 0, -10), Color(1.0, 1.0, 1.0))

    result = lighting(m, light, pos, eye, normal)

    assert result.arrayize() == approx(Color(1.9, 1.9, 1.9).arrayize(), abs=EPSILON)


def test_lighting_with_the_eye_between_light_and_surface_eye_offset_45():
    m = Material()
    pos = Point(0, 0, 0)

    eye = Vector(0, np.sqrt(2) / 2, -np.sqrt(2) / 2)
    normal = Vector(0, 0, -1)

    light = Light(Point(0, 0, -10), Color(1.0, 1.0, 1.0))

    result = lighting(m, light, pos, eye, normal)

    assert result.arrayize() == approx(Color(1.0, 1.0, 1.0).arrayize(), abs=EPSILON)


def test_lighting_with_the_eye_opposite_surface_light_offset_45():
    m = Material()
    pos = Point(0, 0, 0)

    eye = Vector(0, 0, -1)
    normal = Vector(0, 0, -1)

    light = Light(Point(0, 10, -10), Color(1.0, 1.0, 1.0))

    result = lighting(m, light, pos, eye, normal)

    assert result.arrayize() == approx(
        Color(0.7364, 0.7364, 0.7364).arrayize(), abs=EPSILON
    )


def test_with_eye_in_the_path_of_the_reflection_vector():
    m = Material()
    pos = Point(0, 0, 0)

    eye = Vector(0, -np.sqrt(2) / 2, -np.sqrt(2) / 2)
    normal = Vector(0, 0, -1)

    light = Light(Point(0, 10, -10), Color(1.0, 1.0, 1.0))

    result = lighting(m, light, pos, eye, normal)

    assert result.arrayize() == approx(
        Color(1.6364, 1.6364, 1.6364).arrayize(), abs=EPSILON
    )


def test_lighting_with_the_light_behind_the_surface():
    m = Material()
    pos = Point(0, 0, 0)

    eye = Vector(0, 0, -1)
    normal = Vector(0, 0, -1)

    light = Light(Point(0, 0, 10), Color(1.0, 1.0, 1.0))

    result = lighting(m, light, pos, eye, normal)

    assert result.arrayize() == approx(Color(0.1, 0.1, 0.1).arrayize(), abs=EPSILON)


def test_lighting_with_the_surface_in_shadow():
    m = Material()
    pos = Point(0, 0, 0)

    eye = Vector(0, 0, -1)
    normal = Vector(0, 0, -1)

    light = Light(Point(0, 0, -10), Color(1.0, 1.0, 1.0))

    result = lighting(m, light, pos, eye, normal, in_shadow=True)

    assert result.arrayize() == approx(Color(0.1, 0.1, 0.1).arrayize(), abs=EPSILON)
