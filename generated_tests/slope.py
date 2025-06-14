def slope(x1,y1,x2,y2): 
    return (float)(y2-y1)/(x2-x1)

import pytest

def test_slope_positive_coordinates():
    # Calculate slope for points with positive coordinates
    result = slope(1, 2, 3, 6)
    assert result == 2.0

def test_slope_negative_coordinates():
    # Calculate slope for points with negative coordinates
    result = slope(-1, -2, -3, -6)
    assert result == 2.0

def test_slope_zero_slope_horizontal_line():
    # Calculate slope for points with zero slope (horizontal line)
    result = slope(1, 5, 4, 5)
    assert result == 0.0

def test_slope_negative_slope():
    # Calculate slope for points with negative slope
    result = slope(2, 3, 5, 0)
    assert result == -1.0

def test_slope_fractional_slope():
    # Calculate slope for points with fractional slope
    result = slope(1, 1, 4, 3)
    assert result == 0.6666666666666666