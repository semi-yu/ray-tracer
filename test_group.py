import numpy as np

from pytest import approx

from group import Group
from shape import Shape

def test_creating_a_group():
    g = Group()

    assert g.transformation.matrix == approx(np.identity(4))
    assert len(g.shapes) == 0

def test_adding_a_child_to_a_group():
    g = Group()
    s = Shape()

    g.add_child(s)

    assert len(g) != 0
    assert s in g
