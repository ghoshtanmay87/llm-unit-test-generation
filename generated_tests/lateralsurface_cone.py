import math
def lateralsurface_cone(r,h):
  l = math.sqrt(r * r + h * h)
  LSA = math.pi * r  * l
  return LSA

import pytest

def test_lateral_surface_area_cone_radius_3_height_4():
    # Calculate lateral surface area of a cone with radius 3 and height 4
    r = 3
    h = 4
    expected = 47.12388980384689
    result = lateralsurface_cone(r, h)
    assert result == expected

def test_lateral_surface_area_cone_radius_0_height_5():
    # Calculate lateral surface area of a cone with radius 0 and height 5
    r = 0
    h = 5
    expected = 0.0
    result = lateralsurface_cone(r, h)
    assert result == expected

def test_lateral_surface_area_cone_radius_5_height_0():
    # Calculate lateral surface area of a cone with radius 5 and height 0
    r = 5
    h = 0
    expected = 78.53981633974483
    result = lateralsurface_cone(r, h)
    assert result == expected

def test_lateral_surface_area_cone_radius_1_height_1():
    # Calculate lateral surface area of a cone with radius 1 and height 1
    r = 1
    h = 1
    expected = 4.442882938158366
    result = lateralsurface_cone(r, h)
    assert result == expected

def test_lateral_surface_area_cone_radius_10_height_10():
    # Calculate lateral surface area of a cone with radius 10 and height 10
    r = 10
    h = 10
    expected = 443.2887701912593
    result = lateralsurface_cone(r, h)
    assert result == expected