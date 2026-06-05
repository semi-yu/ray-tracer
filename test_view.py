import numpy as np

from pytest import approx

from view import view_transform
from util.transformation import Transformation
from util.mathematics import Vector, Point


def test_transformation_matrix_for_the_default_orientation():
    from_point = Point(0, 0, 0)
    to_point = Point(0, 0, -1)
    up_vector = Vector(0, 1, 0)

    t = view_transform(from_point, to_point, up_vector)

    assert t == approx(np.identity(4))


def test_view_transformation_matrix_looking_in_positive_z_direction():
    from_point = Point(0, 0, 0)
    to_point = Point(0, 0, 1)
    up_vector = Vector(0, 1, 0)

    t = view_transform(from_point, to_point, up_vector)

    assert t == approx(Transformation().scale(-1, 1, -1).matrix)


def test_view_transformation_moves_the_world():
    from_point = Point(0, 0, 8)
    to_point = Point(0, 0, 0)
    up_vector = Vector(0, 1, 0)

    t = view_transform(from_point, to_point, up_vector)

    assert t == approx(Transformation().translate(0, 0, -8).matrix)


def test_an_arbitrary_view_transformation():
    from_point = Point(1, 3, 2)
    to_point = Point(4, -2, 8)
    up_vector = Vector(1, 1, 0)

    t = view_transform(from_point, to_point, up_vector)

    assert t == approx(
        np.array(
            [
                [-0.50709, 0.50709, 0.67612, -2.36643],
                [0.76772, 0.60609, 0.12122, -2.82843],
                [-0.35857, 0.59761, -0.71714, 0.00000],
                [0.00000, 0.00000, 0.00000, 1.00000],
            ]
        ),
        abs=1e-5,
    )
