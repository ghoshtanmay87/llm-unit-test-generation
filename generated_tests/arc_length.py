def arc_length(d,a):
    pi=22/7
    if a >= 360:
        return None
    arclength = (pi*d) * (a/360)
    return arclength

import pytest

def test_arc_length_semicircle_diameter_14():
    # Calculate arc length for a semicircle (180 degrees) with diameter 14
    result = arc_length(d=14, a=180)
    assert result == 22.0

def test_arc_length_quarter_circle_diameter_7():
    # Calculate arc length for a quarter circle (90 degrees) with diameter 7
    result = arc_length(d=7, a=90)
    assert result == 5.5

def test_arc_length_small_angle_diameter_28():
    # Calculate arc length for a small angle (45 degrees) with diameter 28
    result = arc_length(d=28, a=45)
    assert result == 11.0

def test_arc_length_angle_equal_360_returns_none():
    # Return None for angle equal to 360 degrees with diameter 10
    result = arc_length(d=10, a=360)
    assert result is None

def test_arc_length_angle_greater_than_360_returns_none():
    # Return None for angle greater than 360 degrees (400) with diameter 5
    result = arc_length(d=5, a=400)
    assert result is None