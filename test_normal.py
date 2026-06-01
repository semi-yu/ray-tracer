import math

import numpy as np
from pytest import approx

from util.transformation import Transformation
from entities.normal import normal_at
from util.mathematics import Vector, Point
from entities.sphere import Sphere


def test_normal_on_sphere_on_x_axis():
    s = Sphere(Point(0, 0, 0), 1.0)
    n = normal_at(s, Point(1, 0, 0))

    assert n.coord == approx(Vector(1, 0, 0).coord)


def test_normal_on_sphere_on_y_axis():
    s = Sphere(Point(0, 0, 0), 1.0)
    n = normal_at(s, Point(0, 1, 0))

    assert n.coord == approx(Vector(0, 1, 0).coord)


def test_normal_on_sphere_on_z_axis():
    s = Sphere(Point(0, 0, 0), 1.0)
    n = normal_at(s, Point(0, 0, 1))

    assert n.coord == approx(Vector(0, 0, 1).coord)


def test_normal_on_sphere_on_non_axial_axis():
    s = Sphere(Point(0, 0, 0), 1.0)
    n = normal_at(s, Point(1 / math.sqrt(3), 1 / math.sqrt(3), 1 / math.sqrt(3)))

    assert n.coord == approx(
        Vector(1 / math.sqrt(3), 1 / math.sqrt(3), 1 / math.sqrt(3)).coord
    )


def test_normal_on_translated_sphere():
    s = Sphere(Point(0, 0, 0), 1.0)

    t = Transformation().translate(0, 1, 0)

    s.set_transform(t)

    n = normal_at(s, Point(0, 1.70711, -0.70711))

    assert n.coord == approx(Vector(0.0, 0.70711, -0.70711).coord, abs=1e-5)


def test_normal_on_transformed_sphere():
    s = Sphere(Point(0, 0, 0), 1.0)

    t = Transformation().rotate(math.pi / 5, axis="z").scale(1, 0.5, 1)

    s.set_transform(t)

    n = normal_at(s, Point(0, math.sqrt(2) / 2, -math.sqrt(2) / 2))

    assert n.coord == approx(Vector(0, 0.97014, -0.24254).coord, abs=1e-5)
