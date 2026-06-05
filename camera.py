import numpy as np

from pytest import approx

from view import view_transform

from entities.ray import Ray

from util.mathematics import Vector, Point
from util.transformation import Transformation

from intersect import color_at

from image.canvas import Canvas


class Camera:
    def __init__(self, hsize, vsize, fov):
        self._hsize = hsize
        self._vsize = vsize
        self._fov = fov

        half_view = np.tan(fov / 2)
        aspect = self._hsize / self._vsize

        self._half_width = half_view if aspect >= 1 else (half_view * aspect)
        self._half_height = (half_view / aspect) if aspect >= 1 else half_view

        self._pixel_size = self._half_width * 2 / self._hsize

        self._view_matrix = np.identity(4)

        self._transformation = Transformation()

    def set_view(self, fromp, top, upv):
        self._view_matrix = (
            view_transform(fromp, top, upv) @ self._transformation.matrix
        )
        return self

    def set_transform(self, t):
        self._transformation = t
        return self

    @property
    def hsize(self):
        return self._hsize

    @property
    def vsize(self):
        return self._vsize

    @property
    def fov(self):
        return self._fov

    @property
    def pixel_size(self):
        return self._pixel_size

    @property
    def view_matrix(self):
        return self._view_matrix

    @property
    def half_width(self):
        return self._half_width

    @property
    def half_height(self):
        return self._half_height

    @property
    def transformation(self):
        return self._transformation


def ray_for_pixel(camera, px, py) -> Ray:
    xoffset = (px + 0.5) * camera.pixel_size
    yoffset = (py + 0.5) * camera.pixel_size

    worldx = camera.half_width - xoffset
    worldy = camera.half_height - yoffset

    pixel = np.linalg.inv(camera.view_matrix) @ np.array([worldx, worldy, -1, 1])
    origin = np.linalg.inv(camera.view_matrix) @ np.array([0, 0, 0, 1])
    direct = Vector().set_coord(pixel - origin).normalize()

    return Ray(Point().set_coord(origin), direct)


def render(camera, world):
    image = Canvas(camera.hsize, camera.vsize)

    for y in range(camera.vsize):
        for x in range(camera.hsize):
            color = color_at(world, ray_for_pixel(camera, x, y))

            image.write_pixel(x, y, color)

    return image
