import numpy as np

from image.canvas import Color
from util.mathematics import Point, Vector

from reflect import reflect


class Light:
    def __init__(self, position: Point, intensity: Color):
        self._position = position
        self._intensity = intensity

    @property
    def position(self) -> Point:
        return self._position

    @property
    def intensity(self) -> Color:
        return self._intensity


def lighting(material, light, position, eye, normal) -> Color:
    effective_color = material.color.arrayize() * light.intensity.arrayize()

    diff = light.position.coord - position.coord
    light_vector = diff / np.linalg.norm(diff)

    ambient = effective_color * material.ambient

    light_dot_normal = np.dot(light_vector, normal.coord)

    diffuse, specular = np.array([0, 0, 0]), np.array([0, 0, 0])

    if light_dot_normal >= 0:
        diffuse = effective_color * material.diffuse * light_dot_normal

        rev_light = Vector()
        rev_light.set_coord(-light_vector)

        reflect_vector = reflect(rev_light, normal)
        reflect_dot_eye = np.dot(reflect_vector.coord, eye.coord)

        if reflect_dot_eye > 0:
            factor = np.power(reflect_dot_eye, material.shininess)
            specular = light.intensity.arrayize() * material.specular * factor

    result = Color()
    result.set_coord(ambient + diffuse + specular)

    return result


def shade_hit(world, comps) -> Color:
    return lighting(
        comps.object.material, world.light, comps.point, comps.eye, comps.normal
    )
