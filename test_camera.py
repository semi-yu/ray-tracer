from pytest import approx

import numpy as np

from camera import ray_for_pixel

from util.transformation import Transformation
from util.mathematics import Point, Vector

from camera import Camera


def test_constructing_a_camera():
    c = Camera(hsize=160, vsize=120, fov=np.pi / 2)

    assert c.hsize == 160
    assert c.vsize == 120
    assert c.fov == np.pi / 2
    assert c.transformation.matrix == approx(np.identity(4))


def test_the_pixel_size_for_a_horizontal_canvas():
    c = Camera(200, 125, np.pi / 2)
    assert c.pixel_size == approx(0.01)


def test_the_pixel_size_for_a_vertical_canvas():
    c = Camera(125, 200, np.pi / 2)
    assert c.pixel_size == approx(0.01)


def test_constructing_a_ray_through_the_center_of_the_canvas():
    c = Camera(201, 101, np.pi / 2)
    r = ray_for_pixel(c, 100, 50)

    assert r.origin.coord == approx(Point(0, 0, 0).coord, abs=1e-7)
    assert r.direction.coord == approx(Vector(0, 0, -1).coord, abs=1e-7)


def test_constructing_a_ray_through_a_corner_of_the_canvas():
    c = Camera(201, 101, np.pi / 2)
    r = ray_for_pixel(c, 0, 0)

    assert r.origin.coord == approx(Point(0, 0, 0).coord, abs=1e-7)
    assert r.direction.coord == approx(
        Vector(0.66519, 0.33259, -0.66851).coord, abs=1e-5
    )


def test_constructing_a_ray_when_the_camera_is_transformed():
    c = Camera(201, 101, np.pi / 2).set_transform(
        Transformation().translate(0, -2, 5).rotate(np.pi / 4, axis="y")
    )

    r = ray_for_pixel(c, 100, 50)

    assert r.origin.coord == approx(Point(0, 2, -5).coord, abs=1e-7)
    assert r.direction.coord == approx(
        Vector(np.sqrt(2) / 2, 0, -np.sqrt(2) / 2).coord, abs=1e-7
    )
