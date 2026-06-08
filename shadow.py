from image.canvas import Color
from entities.ray import Ray
from util.mathematics import Vector, Point

from world import World

from light import lighting
from intersect import intersect_world, Intersection


def is_shadowed(world: World, point: Point) -> bool:
    v = Vector().set_coord(world.light.position.coord - point.coord)

    distance = v.magnitude()
    direction = v.normalize()

    r = Ray(point, direction)
    intersections = intersect_world(world, r)

    h = hit(intersections)

    return True if h is not None and h.t < distance else False


def hit(xpoints: list[Intersection]):
    nonnegatives = filter(lambda x: x.t > 0, xpoints)
    return min(nonnegatives, key=lambda x: x.t, default=None)


def shade_hit(world, comps) -> Color:
    in_shadow = is_shadowed(world, comps.point)

    return lighting(
        comps.object.material,
        world.light,
        comps.point,
        comps.eye,
        comps.normal,
        in_shadow,
    )
