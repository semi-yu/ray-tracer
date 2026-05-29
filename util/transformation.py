import math

import numpy as np


def translate(x: float, y: float, z: float):
    return np.array([[1, 0, 0, x], [0, 1, 0, y], [0, 0, 1, z], [0, 0, 0, 1]])


def scale(x: float, y: float, z: float):
    return np.array([[x, 0, 0, 0], [0, y, 0, 0], [0, 0, z, 0], [0, 0, 0, 1]])


def rotate(rad: float, axis: str):
    if axis == "x":
        return np.array(
            [
                [1, 0, 0, 0],
                [0, math.cos(rad), -math.sin(rad), 0],
                [0, math.sin(rad), math.cos(rad), 0],
                [0, 0, 0, 1],
            ]
        )
    elif axis == "y":
        return np.array(
            [
                [math.cos(rad), 0, math.sin(rad), 0],
                [0, 1, 0, 0],
                [-math.sin(rad), 0, math.cos(rad), 0],
                [0, 0, 0, 1],
            ]
        )
    elif axis == "z":
        return np.array(
            [
                [math.cos(rad), -math.sin(rad), 0, 0],
                [math.sin(rad), math.cos(rad), 0, 0],
                [0, 0, 1, 0],
                [0, 0, 0, 1],
            ]
        )
    else:
        raise Exception("rotating axis must be x, y or z")


def shear(xy: float, xz: float, yx: float, yz: float, zx: float, zy: float):
    return np.array([[1, xy, xz, 0], [yx, 1, yz, 0], [zx, zy, 1, 0], [0, 0, 0, 1]])


class Transformation:
    def __init__(self):
        self._matrix = np.identity(4)

    def translate(self, x: float, y: float, z: float):
        self._matrix = translate(x, y, z) @ self._matrix
        return self

    def scale(self, x: float, y: float, z: float):
        self._matrix = scale(x, y, z) @ self._matrix
        return self

    def rotate(self, rad: float, axis: str):
        self._matrix = rotate(rad, axis) @ self._matrix
        return self

    def shear(self, xy: float, xz: float, yx: float, yz: float, zx: float, zy: float):
        self._matrix = shear(xy, xz, yx, yz, zx, zy) @ self._matrix
        return self

    def inverse(self):
        return np.linalg.inv(self._matrix)

    @property
    def matrix(self):
        return self._matrix
