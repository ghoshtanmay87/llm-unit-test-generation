def surface_Area(b,s): 
    return 2 * b * s + pow(b,2)

import pytest

def test_surface_area_base_1_side_1():
    # Calculate surface area with base 1 and side 1
    result = surface_Area(b=1, s=1)
    assert result == 3

def test_surface_area_base_2_side_3():
    # Calculate surface area with base 2 and side 3
    result = surface_Area(b=2, s=3)
    assert result == 16

def test_surface_area_base_0_side_5():
    # Calculate surface area with base 0 and side 5
    result = surface_Area(b=0, s=5)
    assert result == 0

def test_surface_area_base_4_side_0():
    # Calculate surface area with base 4 and side 0
    result = surface_Area(b=4, s=0)
    assert result == 16

def test_surface_area_base_3_side_3():
    # Calculate surface area with base 3 and side 3
    result = surface_Area(b=3, s=3)
    assert result == 27