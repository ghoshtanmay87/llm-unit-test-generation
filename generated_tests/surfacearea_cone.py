import math
def surfacearea_cone(r,h):
  l = math.sqrt(r * r + h * h)
  SA = math.pi * r * (r + l)
  return SA

import pytest

def test_surface_area_cone_radius_3_height_4():
    # Calculate surface area of a cone with radius 3 and height 4
    r = 3
    h = 4
    expected = 75.39822368615503
    result = surfacearea_cone(r, h)
    assert result == expected

def test_surface_area_cone_radius_0_height_5():
    # Calculate surface area of a cone with radius 0 and height 5 (degenerate cone)
    r = 0
    h = 5
    expected = 0.0
    result = surfacearea_cone(r, h)
    assert result == expected

def test_surface_area_cone_radius_5_height_0():
    # Calculate surface area of a cone with radius 5 and height 0 (flat disk)
    r = 5
    h = 0
    expected = 157.07963267948966
    result = surfacearea_cone(r, h)
    assert result == expected

def test_surface_area_cone_radius_1_height_1():
    # Calculate surface area of a cone with radius 1 and height 1
    r = 1
    h = 1
    expected = 7.680829457069631
    result = surfacearea_cone(r, h)
    assert result == expected

def test_surface_area_cone_radius_10_height_10():
    # Calculate surface area of a cone with radius 10 and height 10
    r = 10
    h = 10
    expected = 478.7787204069187
    result = surfacearea_cone(r, h)
    assert result == expected