import cmath
def polar_rect(x,y):
 cn = complex(x,y)
 cn=cmath.polar(cn)
 cn1 = cmath.rect(2, cmath.pi)
 return (cn,cn1)

import pytest

def test_polar_rect_point_1_0():
    # Convert point (1, 0) to polar and compute rect(2, pi)
    result = polar_rect(1, 0)
    expected = [(1.0, 0.0), (-2.0, 2.4492935982947064e-16)]
    assert result == expected

def test_polar_rect_point_0_1():
    # Convert point (0, 1) to polar and compute rect(2, pi)
    result = polar_rect(0, 1)
    expected = [(1.0, 1.5707963267948966), (-2.0, 2.4492935982947064e-16)]
    assert result == expected

def test_polar_rect_point_minus1_0():
    # Convert point (-1, 0) to polar and compute rect(2, pi)
    result = polar_rect(-1, 0)
    expected = [(1.0, 3.141592653589793), (-2.0, 2.4492935982947064e-16)]
    assert result == expected

def test_polar_rect_point_0_0():
    # Convert point (0, 0) to polar and compute rect(2, pi)
    result = polar_rect(0, 0)
    expected = [(0.0, 0.0), (-2.0, 2.4492935982947064e-16)]
    assert result == expected

def test_polar_rect_point_1_1():
    # Convert point (1, 1) to polar and compute rect(2, pi)
    result = polar_rect(1, 1)
    expected = [(1.4142135623730951, 0.7853981633974483), (-2.0, 2.4492935982947064e-16)]
    assert result == expected