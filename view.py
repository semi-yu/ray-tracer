import numpy as np

from util.transformation import Transformation
from util.mathematics import Vector, Point


def view_transform(fromv: Point, tov: Point, upv: Vector):
    forward = Vector().set_coord(tov.coord - fromv.coord).normalize().coord

    left = np.cross(forward[:3], upv.normalize().coord[:3]).astype(np.float64)
    true_up = np.cross(left[:3], forward[:3]).astype(np.float64)

    orientation = np.eye(4, dtype=np.float64)
    orientation[0, :3] = left
    orientation[1, :3] = true_up
    orientation[2, :3] = -forward[:3]

    t = Transformation().translate(-fromv.coord[0], -fromv.coord[1], -fromv.coord[2])

    return orientation @ t.matrix
