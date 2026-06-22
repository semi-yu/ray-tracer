import math
import numpy as np

from image.canvas import Color
from entities.ray import Ray

from world import World
from shadow import hit
from intersect import intersect_world
from computation import prepare_computation

from shadow import is_shadowed
from light import lighting

from computation import Computation

from intersect import schlick


REMANINING = 5


def color_at(world, ray: Ray, remaining: int = REMANINING):
    mhit = hit(intersect_world(world, ray))

    if mhit is None:
        return Color(0.0, 0.0, 0.0)

    comps = prepare_computation(mhit, ray)

    return shade_hit(world, comps, remaining)


def shade_hit(world, comps, remaining: int = REMANINING) -> Color:
    in_shadow = is_shadowed(world, comps.over_point)

    surface = lighting(
        comps.object.material,
        world.light,
        comps.over_point,
        comps.eye,
        comps.normal,
        in_shadow = in_shadow,
        object    = comps.object
    )

    reflected = reflected_color(world, comps, remaining)
    refracted = refracted_color(world, comps, remaining)

    material = comps.object.material

    if material.reflective > 0 and material.transparency > 0:
        reflectance = schlick(comps)

        return surface + reflected * reflectance + refracted * (1 - reflectance)
    else:
        return surface + reflected + refracted


def reflected_color(world: World, comps: Computation, remaining: int = REMANINING) -> Color:
    if remaining <= 0: return Color()

    if math.isclose(0.0, comps.object.material.reflective):
        return Color()
    
    reflected_ray = Ray(comps.over_point, comps.reflect)
    color = color_at(world, reflected_ray, remaining - 1)

    return color * comps.object.material.reflective

def refracted_color(world: World, comps: Computation, remaining: int) -> Color:
    if comps.object.material.transparency == 0:
        return Color()
    
    n_ratio = comps.n1 / comps.n2
    cos_i = np.dot(comps.eye.coord, comps.normal.coord)
    sin2_t = n_ratio * n_ratio * (1 - cos_i * cos_i)

    print(comps.n1, comps.n2, n_ratio)

    if sin2_t > 1.0: return Color()
    
    cos_t = np.sqrt(1.0 - sin2_t)
    direction = comps.normal * (n_ratio * cos_i - cos_t) - \
                comps.eye * n_ratio
    
    print(comps.eye, comps.normal)
    
    print(cos_i, sin2_t, cos_t)

    refract_ray = Ray(comps.under_point, direction)

    print(refract_ray)
    
    color = color_at(world, refract_ray, remaining - 1) * \
            comps.object.material.transparency

    return color
