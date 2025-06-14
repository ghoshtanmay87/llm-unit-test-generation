def parabola_focus(a, b, c): 
  focus= (((-b / (2 * a)),(((4 * a * c) - (b * b) + 1) / (4 * a))))
  return focus

import pytest

def test_focus_positive_abc():
    # Calculate focus of parabola with positive a, b, c
    a = 1
    b = 2
    c = 3
    expected = (-1.0, 2.25)
    result = parabola_focus(a, b, c)
    assert result == expected

def test_focus_negative_a():
    # Calculate focus of parabola with negative a
    a = -1
    b = 4
    c = -3
    expected = (2.0, 0.75)
    result = parabola_focus(a, b, c)
    assert result == expected

def test_focus_zero_b():
    # Calculate focus of parabola with zero b
    a = 2
    b = 0
    c = 1
    expected = (0.0, 1.125)
    result = parabola_focus(a, b, c)
    assert result == expected

def test_focus_zero_c():
    # Calculate focus of parabola with zero c
    a = 1
    b = 1
    c = 0
    expected = (-0.5, 0.0)
    result = parabola_focus(a, b, c)
    assert result == expected

def test_focus_fractional_coefficients():
    # Calculate focus of parabola with fractional coefficients
    a = 0.5
    b = 1.5
    c = 2.5
    expected = (-1.5, 1.875)
    result = parabola_focus(a, b, c)
    assert result == expected