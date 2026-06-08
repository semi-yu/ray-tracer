from entities.ray import Ray
from image.canvas import Color

from shadow import hit, shade_hit
from intersect import intersect_world
from computation import prepare_computation


def color_at(world, ray: Ray):
    mhit = hit(intersect_world(world, ray))

    if mhit is None:
        return Color(0.0, 0.0, 0.0)

    comps = prepare_computation(mhit, ray)

    return shade_hit(world, comps)
