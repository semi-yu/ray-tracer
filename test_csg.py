from sphere import Sphere
from cube import Cube
from csg import Csg

def test_CSG_is_created_with_an_operation_and_two_shapes():
    s1 = Sphere()
    s2 = Cube()

    c = Csg("union", s1, s2)

    assert c.operation == "union"
    assert c.left == s1
    assert c.right == s2
    assert s1.parent == c
    assert s2.parent == c
