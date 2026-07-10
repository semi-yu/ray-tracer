from pytest import approx

from util.mathematics import Vector, Point
from entities.ray import Ray

from sphere import Sphere
from cube import Cube
from csg import Csg, intersection_allowed, filter_intersections

from util.transformation import Transformation
from intersect import Intersection

def test_CSG_is_created_with_an_operation_and_two_shapes():
    s1 = Sphere()
    s2 = Cube()

    c = Csg("union", s1, s2)

    assert c.operation == "union"
    assert c.left == s1
    assert c.right == s2
    assert s1.parent == c
    assert s2.parent == c

def test_evaluating_the_rule_for_a_CSG_operation():
    values = (True, False)

    expected_result = [
        False, True, False, True, False, False, True, True, # union
        True, False, True, False, True, True, False, False, # intersection
        False, True, False, True, True, True, False, False, # difference
    ]

    idx = 0

    for op in ("union", "intersection", "difference"):
        for has_left_hit in values:
            for in_left in values:
                for in_right in values:
                    result = intersection_allowed(op, has_left_hit, in_left, in_right)

                    assert result == expected_result[idx]
                    idx += 1

def test_filtering_a_list_of_intersections():
    s1 = Sphere()
    s2 = Cube()

    xs = [
            Intersection(1, s1),
            Intersection(2, s2),
            Intersection(3, s1),
            Intersection(4, s2),
    ]
    
    expected_index = [
        (0, 3),
        (1, 2),
        (0, 1),
    ]
    
    for idx, op in enumerate(("union", "intersection", "difference")):
        c = Csg(op, s1, s2)


        result = filter_intersections(c, xs)

        i1, i2 = expected_index[idx]

        assert result[0] == xs[i1]
        assert result[1] == xs[i2]

def test_a_ray_misses_a_CSG_object():
    c = Csg("union", Sphere(), Cube())

    r = Ray(Point(0, 2, -5), Vector(0, 0, 1))

    xs = c.local_intersect(r)

    assert len(xs) == 0

def test_a_ray_hits_a_CSG_object():
    s1 = Sphere()
    s2 = Sphere() \
        .set_transform(
            Transformation()
            .translate(0, 0, 0.5)
        )

    c = Csg("union", s1, s2)

    r = Ray(Point(0, 0, -5), Vector(0, 0, 1))

    xs = c.local_intersect(r)

    print(xs)

    assert len(xs) == 2

    assert xs[0].t == approx(4)
    assert xs[0].object == s1

    assert xs[1].t == approx(6.5)
    assert xs[1].object == s2
