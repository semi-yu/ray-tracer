from pytest import approx

from obj_file import parse_obj, obj_to_group

from util.mathematics import Point


def test_ignoring_unrecognized_lines():
    content = [
        "There was a young lady named Bright",
        "who traveled much faster than light.",
        "She set out one day",
        "in a relative way,",
        "and came back the previous night."
    ]

    parser = parse_obj(content)

    assert parser.ignored == 5

def test_vertex_records():
    content = [
        "v -1 1 0",
        "v -1.0000 0.50000 0.0000",
        "v 1 0 0",
        "v 1 1 0",
    ]

    parser = parse_obj(content)

    assert parser.vertices[1].coord == approx(Point(-1.0, 1.0, 0.0).coord)
    assert parser.vertices[2].coord == approx(Point(-1.0, 0.5, 0.0).coord)
    assert parser.vertices[3].coord == approx(Point( 1.0, 0.0, 0.0).coord)
    assert parser.vertices[4].coord == approx(Point( 1.0, 1.0, 0.0).coord)

def test_parsing_triangle_faces():
    content = [
        "v -1 1 0",
        "v -1 0 0",
        "v 1 0 0",
        "v 1 1 0",
        "f 1 2 3",
        "f 1 3 4",
    ]

    parser = parse_obj(content)

    g = parser.default_group
    t1 = g[0]
    t2 = g[1]

    assert t1.p1.coord == approx(parser.vertices[1].coord)
    assert t1.p2.coord == approx(parser.vertices[2].coord)
    assert t1.p3.coord == approx(parser.vertices[3].coord)

    assert t2.p1.coord == approx(parser.vertices[1].coord)
    assert t2.p2.coord == approx(parser.vertices[3].coord)
    assert t2.p3.coord == approx(parser.vertices[4].coord)

def test_triangulating_polygons():
    content = [
        "v -1 1 0",
        "v -1 0 0",
        "v 1 0 0",
        "v 1 1 0",
        "v 0 2 0",
        "f 1 2 3 4 5",
    ]

    parser = parse_obj(content)

    g = parser.default_group
    t1 = g[0]
    t2 = g[1]
    t3 = g[2]

    assert t1.p1.coord == approx(parser.vertices[1].coord)
    assert t1.p2.coord == approx(parser.vertices[2].coord)
    assert t1.p3.coord == approx(parser.vertices[3].coord)

    assert t2.p1.coord == approx(parser.vertices[1].coord)
    assert t2.p2.coord == approx(parser.vertices[3].coord)
    assert t2.p3.coord == approx(parser.vertices[4].coord)

    assert t3.p1.coord == approx(parser.vertices[1].coord)
    assert t3.p2.coord == approx(parser.vertices[4].coord)
    assert t3.p3.coord == approx(parser.vertices[5].coord)
    
def test_triangles_in_groups():
    content = [
        "v -1 1 0",
        "v -1 0 0",
        "v 1 0 0",
        "v 1 1 0",
        "g FirstGroup",
        "f 1 2 3",
        "g SecondGroup",
        "f 1 3 4"
    ]

    parser = parse_obj(content)

    print(parser.group)

    g1 = parser[1]
    g2 = parser[2]

    t1 = g1[0]
    t2 = g2[0]

    assert t1.p1.coord == approx(parser.vertices[1].coord)
    assert t1.p2.coord == approx(parser.vertices[2].coord)
    assert t1.p3.coord == approx(parser.vertices[3].coord)

    assert t2.p1.coord == approx(parser.vertices[1].coord)
    assert t2.p2.coord == approx(parser.vertices[3].coord)
    assert t2.p3.coord == approx(parser.vertices[4].coord)

def test_converting_an_obj_file_to_a_group():
    content = [
        "v -1 1 0",
        "v -1 0 0",
        "v 1 0 0",
        "v 1 1 0",
        "g FirstGroup",
        "f 1 2 3",
        "g SecondGroup",
        "f 1 3 4"
    ]

    obj = parse_obj(content)
    g = obj_to_group(obj)

    lgroup = g[0]
    rgroup = g[1]

    t1 = lgroup[0]
    t2 = rgroup[0]

    assert t1.p1.coord == approx(obj.vertices[1].coord)
    assert t1.p2.coord == approx(obj.vertices[2].coord)
    assert t1.p3.coord == approx(obj.vertices[3].coord)

    assert t2.p1.coord == approx(obj.vertices[1].coord)
    assert t2.p2.coord == approx(obj.vertices[3].coord)
    assert t2.p3.coord == approx(obj.vertices[4].coord)
