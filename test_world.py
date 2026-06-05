from pytest import approx

from image.canvas import Color

from util.mathematics import Point, Vector
from util.transformation import Transformation

from entities.ray import Ray, transform
from entities.light import Light, shade_hit
from entities.material import Material
from entities.sphere import Sphere

from world import World

from intersect import intersect_world, prepare_computation, Intersection, color_at


def create_world():
    return World()


def default_world():
    w = create_world()

    l = Light(Point(-10, 10, -10), Color(1.0, 1.0, 1.0))

    s1 = Sphere(Point(0, 0, 0), 1.0)
    s1.set_material(Material(color=Color(0.8, 1.0, 0.6), diffuse=0.7, specular=0.2))

    s2 = Sphere(Point(0, 0, 0), 1.0)
    s2.set_transform(Transformation().scale(0.5, 0.5, 0.5))

    w.set_light(l)
    w.add_object(s1)
    w.add_object(s2)

    return w


def test_world_with_a_ray():
    w = default_world()

    r = Ray(Point(0, 0, -5), Vector(0, 0, 1))

    xs = intersect_world(w, r)

    assert len(xs) == 4
    assert xs[0].t == approx(4)
    assert xs[1].t == approx(4.5)
    assert xs[2].t == approx(5.5)
    assert xs[3].t == approx(6)


def test_shading_an_intersection():
    w = default_world()

    r = Ray(Point(0, 0, -5), Vector(0, 0, 1))

    s = w.objects[0]

    i = Intersection(4, s)

    comps = prepare_computation(i, r)

    c = shade_hit(w, comps)

    assert c.arrayize() == approx(Color(0.38066, 0.47583, 0.2855).arrayize(), abs=10e-6)


def test_shading_an_intersection_from_the_inside():
    w = default_world()

    w.set_light(Light(Point(0, 0.25, 0), Color(1.0, 1.0, 1.0)))

    r = Ray(Point(0, 0, 0), Vector(0, 0, 1))

    s = w.objects[1]

    i = Intersection(0.5, s)

    comps = prepare_computation(i, r)

    c = shade_hit(w, comps)

    assert c.arrayize() == approx(
        Color(0.90498, 0.90498, 0.90498).arrayize(), abs=10e-6
    )


def test_color_when_a_ray_misses():
    w = default_world()

    r = Ray(Point(0, 0, -5), Vector(0, 1, 0))

    c = color_at(w, r)

    assert c.arrayize() == approx(Color(0, 0, 0).arrayize())


def test_color_when_a_ray_hits():
    w = default_world()

    r = Ray(Point(0, 0, -5), Vector(0, 0, 1))

    c = color_at(w, r)

    assert c.arrayize() == approx(Color(0.38066, 0.47583, 0.2855).arrayize(), abs=10e-6)


def test_color_with_an_intersection_behind_the_ray():
    w = default_world()

    outer = w.objects[0]
    outer.material.set_ambient(1.0)
    inner = w.objects[1]
    inner.material.set_ambient(1.0)

    r = Ray(Point(0, 0, 0.75), Vector(0, 0, -1))

    c = color_at(w, r)

    assert c.arrayize() == approx(inner.material.color.arrayize(), abs=10e-6)
