import numpy as np

from pytest import approx

from group import Group

def test_creating_a_group():
    g = Group()

    assert g.transformation.matrix == approx(np.identity(4))
    assert len(g.shapes) == 0
