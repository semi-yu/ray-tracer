import math

from entities.ray import Ray
from image.canvas import Color

from shadow import hit, shade_hit
from intersect import intersect_world
from computation import prepare_computation, Computation


from world import World

def color_at(world, ray: Ray):
    mhit = hit(intersect_world(world, ray))

    if mhit is None:
        return Color(0.0, 0.0, 0.0)

    comps = prepare_computation(mhit, ray)

    return shade_hit(world, comps)

def reflected_color(world: World, comps: Computation) -> Color:
    if math.isclose(0.0, comps.object.material.reflective):
        return Color()
    
    reflected_ray = Ray(comps.over_point, comps.reflect)
    color = color_at(world, reflected_ray)

    return color * comps.object.material.reflective
