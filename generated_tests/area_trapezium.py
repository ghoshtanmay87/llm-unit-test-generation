def area_trapezium(base1,base2,height):
 area = 0.5 * (base1 + base2) * height
 return area

import pytest

def test_area_trapezium_equal_bases_positive_height():
    # Calculate area with equal bases and positive height
    result = area_trapezium(base1=4, base2=4, height=5)
    assert result == 20.0

def test_area_trapezium_different_bases_positive_height():
    # Calculate area with different bases and positive height
    result = area_trapezium(base1=3, base2=7, height=6)
    assert result == 30.0

def test_area_trapezium_one_base_zero_positive_height():
    # Calculate area with one base zero and positive height
    result = area_trapezium(base1=0, base2=10, height=4)
    assert result == 20.0

def test_area_trapezium_zero_height():
    # Calculate area with zero height
    result = area_trapezium(base1=5, base2=7, height=0)
    assert result == 0.0

def test_area_trapezium_floating_point_bases_height():
    # Calculate area with floating point bases and height
    result = area_trapezium(base1=3.5, base2=4.5, height=2.0)
    assert result == 8.0