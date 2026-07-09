from sphere import Sphere
from cube import Cube
from csg import Csg, intersection_allowed

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
    expected_result = [False, True, False, True, False, False, True, True]

    values = (True, False)

    idx = 0

    for has_left_hit in values:
        for in_left in values:
            for in_right in values:
                result = intersection_allowed("union", has_left_hit, in_left, in_right)

                assert result == expected_result[idx]

                idx += 1
