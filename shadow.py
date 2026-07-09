from entities.ray import Ray
from util.mathematics import Vector, Point, EPSILON

from world import World

from intersect import intersect_world, UVIntersection


def is_shadowed(world: World, point: Point) -> bool:
    v = Vector().set_coord(world.light.position.coord - point.coord)

    distance = v.magnitude()
    direction = v.normalize()

    r = Ray(point, direction)
    intersections = intersect_world(world, r)

    h = hit(intersections)

    return True if h is not None and EPSILON < h.t < distance else False


def hit(xpoints: list[UVIntersection]):
    nonnegatives = filter(lambda x: x.t > 0, xpoints)
    return min(nonnegatives, key=lambda x: x.t, default=None)
