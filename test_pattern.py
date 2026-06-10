from pytest import approx

from pattern import StripePattern

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

    assert p.stripe_at(Point(0, 0, 0)).arrayize() == approx(white.arrayize())
    assert p.stripe_at(Point(0, 1, 0)).arrayize() == approx(white.arrayize())
    assert p.stripe_at(Point(0, 2, 0)).arrayize() == approx(white.arrayize())


def test_a_stripe_pattern_is_constant_in_z():
    black, white = black_and_white()

    p = StripePattern(white, black)

    assert p.stripe_at(Point(0, 0, 0)).arrayize() == approx(white.arrayize())
    assert p.stripe_at(Point(0, 0, 1)).arrayize() == approx(white.arrayize())
    assert p.stripe_at(Point(0, 0, 2)).arrayize() == approx(white.arrayize())


def test_a_stripe_pattern_is_constant_in_x():
    black, white = black_and_white()

    p = StripePattern(white, black)

    assert p.stripe_at(Point(0, 0, 0)).arrayize() == approx(white.arrayize())
    assert p.stripe_at(Point(0.9, 0, 0)).arrayize() == approx(white.arrayize())
    assert p.stripe_at(Point(1.0, 0, 0)).arrayize() == approx(black.arrayize())

    assert p.stripe_at(Point(-0.1, 0, 0)).arrayize() == approx(black.arrayize())
    assert p.stripe_at(Point(-1.0, 0, 0)).arrayize() == approx(black.arrayize())
    assert p.stripe_at(Point(-1.1, 0, 0)).arrayize() == approx(white.arrayize())

def test_stripes_with_an_object_transformation():
    obj = Sphere() \
          .set_transform(
              Transformation() \
              .scale(2.0, 2.0, 2.0)
          )

    black, white = black_and_white()
    p = StripePattern(white, black)

    color = p.stripe_at_object(obj, Point(1.5, 0.0, 0.0))

    assert color.arrayize() == approx(white.arrayize())

def test_stripes_with_a_pattern_transformation():
    obj = Sphere()

    black, white = black_and_white()
    p = StripePattern(white, black) \
        .set_transform(
            Transformation()
            .scale(2.0, 2.0, 2.0)
        )
    
    color = p.stripe_at_object(obj, Point(1.5, 0.0, 0.0))

    assert color.arrayize() == approx(white.arrayize())

def test_stripes_with_both_an_object_and_a_pattern_transformation():
    obj = Sphere()
    
    black, white = black_and_white()
    p = StripePattern(white, black) \
        .set_transform(
            Transformation()
            .translate(0.5, 0.0, 0.0)
        )
    
    color = p.stripe_at_object(obj, Point(2.5, 0.0, 0.0))

    assert color.arrayize() == approx(white.arrayize())
