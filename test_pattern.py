from pytest import approx

from pattern import StripePattern

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

