import math

from image.canvas import Color
from entities.ray import Ray

from world import World
from shadow import hit
from intersect import intersect_world
from computation import prepare_computation

from shadow import is_shadowed
from light import lighting

from computation import Computation


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

    return surface + reflected


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
    
    return Color(1.0, 1.0, 1.0)