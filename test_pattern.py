import numpy as np

from pytest import approx

from pattern import Pattern, StripePattern, GradientPattern, RingPattern

from util.transformation import Transformation

from sphere import Sphere
from util.mathematics import Point
from image.canvas import Color


def black_and_white():
    black = Color(0, 0, 0)
    white = Color(1.0, 1.0, 1.0)

    return black, white


def test_creating_a_stripe_pattern():
    black, white = black_and_white()

    pattern = StripePattern(white, black)

    assert pattern.a.arrayize() == approx(white.arrayize())
    assert pattern.b.arrayize() == approx(black.arrayize())


def test_a_stripe_pattern_is_constant_in_y():
    black, white = black_and_white()

    p = StripePattern(white, black)

    assert p.pattern_at(Point(0, 0, 0)).arrayize() == approx(white.arrayize())
    assert p.pattern_at(Point(0, 1, 0)).arrayize() == approx(white.arrayize())
    assert p.pattern_at(Point(0, 2, 0)).arrayize() == approx(white.arrayize())


def test_a_stripe_pattern_is_constant_in_z():
    black, white = black_and_white()

    p = StripePattern(white, black)

    assert p.pattern_at(Point(0, 0, 0)).arrayize() == approx(white.arrayize())
    assert p.pattern_at(Point(0, 0, 1)).arrayize() == approx(white.arrayize())
    assert p.pattern_at(Point(0, 0, 2)).arrayize() == approx(white.arrayize())


def test_a_stripe_pattern_is_constant_in_x():
    black, white = black_and_white()

    p = StripePattern(white, black)

    assert p.pattern_at(Point(0, 0, 0)).arrayize() == approx(white.arrayize())
    assert p.pattern_at(Point(0.9, 0, 0)).arrayize() == approx(white.arrayize())
    assert p.pattern_at(Point(1.0, 0, 0)).arrayize() == approx(black.arrayize())

    assert p.pattern_at(Point(-0.1, 0, 0)).arrayize() == approx(black.arrayize())
    assert p.pattern_at(Point(-1.0, 0, 0)).arrayize() == approx(black.arrayize())
    assert p.pattern_at(Point(-1.1, 0, 0)).arrayize() == approx(white.arrayize())

def test_stripes_with_an_object_transformation():
    obj = Sphere() \
          .set_transform(
              Transformation() \
              .scale(2.0, 2.0, 2.0)
          )

    black, white = black_and_white()
    p = StripePattern(white, black)

    color = p.pattern_at_object(obj, Point(1.5, 0.0, 0.0))

    assert color.arrayize() == approx(white.arrayize())

def test_stripes_with_a_pattern_transformation():
    obj = Sphere()

    black, white = black_and_white()
    p = StripePattern(white, black) \
        .set_transform(
            Transformation()
            .scale(2.0, 2.0, 2.0)
        )
    
    color = p.pattern_at_object(obj, Point(1.5, 0.0, 0.0))

    assert color.arrayize() == approx(white.arrayize())

def test_stripes_with_both_an_object_and_a_pattern_transformation():
    obj = Sphere()
    
    black, white = black_and_white()
    p = StripePattern(white, black) \
        .set_transform(
            Transformation()
            .translate(0.5, 0.0, 0.0)
        )
    
    color = p.pattern_at_object(obj, Point(2.5, 0.0, 0.0))

    assert color.arrayize() == approx(white.arrayize())

def test_default_pattern_transformation():
    p = Pattern()

    assert p.transform.matrix == approx(np.identity(4))

def test_assigning_a_transformation():
    p = Pattern() \
        .set_transform(
            Transformation()
            .translate(1, 2, 3)
        )
    
    assert p.transform.matrix == approx(Transformation().translate(1, 2, 3).matrix)

def test_a_pattern_with_an_object_transformation():
    s = Sphere() \
        .set_transform(
            Transformation()
            .scale(2.0, 2.0, 2.0)
        )
    
    p = Pattern()
    
    c = p.pattern_at_object(s, Point(2, 3, 4))

    assert c.arrayize() == approx(Color(1.0, 1.5, 2.0).arrayize())

def test_a_pattern_with_a_pattern_transformation():
    s = Sphere()
    
    p = Pattern() \
        .set_transform(
            Transformation()
            .scale(2.0, 2.0, 2.0)
        )

    c = p.pattern_at_object(s, Point(2, 3, 4))

    assert c.arrayize() == approx(Color(1.0, 1.5, 2.0).arrayize())

def test_a_pattern_with_a_pattern_transformation():
    s = Sphere() \
        .set_transform(
            Transformation()
            .scale(2.0, 2.0, 2.0)
        )
    
    p = Pattern() \
        .set_transform(
            Transformation()
            .translate(0.5, 1.0, 1.5)
        )

    c = p.pattern_at_object(s, Point(2.5, 3.0, 3.5))

    assert c.arrayize() == approx(Color(0.75, 0.5, 0.25).arrayize())

def test_a_gradient_linearly_interpolates_between_colors():
    black, white = black_and_white()
    p = GradientPattern(white, black)

    # test case were modified to test smoothed gradient.
    assert p.pattern_at(Point(0, 0, 0)).arrayize() == approx(white.arrayize())
    assert p.pattern_at(Point(0.25, 0, 0)).arrayize() == approx(Color(0.5, 0.5, 0.5).arrayize())
    assert p.pattern_at(Point(0.5, 0, 0)).arrayize() == approx(black.arrayize())
    assert p.pattern_at(Point(0.75, 0, 0)).arrayize() == approx(Color(0.5, 0.5, 0.5).arrayize())

def test_a_ring_should_extend_in_both_x_and_z():
    black, white = black_and_white()
    p = RingPattern(white, black)

    assert p.pattern_at(Point(0, 0, 0)).arrayize() == approx(white.arrayize())
    assert p.pattern_at(Point(1, 0, 0)).arrayize() == approx(black.arrayize())
    assert p.pattern_at(Point(0, 0, 1)).arrayize() == approx(black.arrayize())
    assert p.pattern_at(Point(0.708, 0, 0.708)).arrayize() == approx(black.arrayize())
