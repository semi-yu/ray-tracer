import numpy as np

from util.mathematics import Vector


def reflect(incidence: Vector, normal: Vector) -> Vector:
    result_coord = incidence.coord - normal.coord * 2 * np.dot(
        incidence.coord, normal.coord
    )

    result = Vector()
    result.set_coord(result_coord)

    return result
