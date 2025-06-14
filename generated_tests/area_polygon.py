from math import tan, pi
def area_polygon(s,l):
  area = s * (l ** 2) / (4 * tan(pi / s))
  return area

import pytest

def test_area_equilateral_triangle_side_1():
    # Calculate area of an equilateral triangle with side length 1
    result = area_polygon(s=3, l=1)
    expected = 0.43301270189221935
    assert result == expected

def test_area_square_side_2():
    # Calculate area of a square with side length 2
    result = area_polygon(s=4, l=2)
    expected = 4.0
    assert result == expected

def test_area_regular_pentagon_side_3():
    # Calculate area of a regular pentagon with side length 3
    result = area_polygon(s=5, l=3)
    expected = 15.484296605300704
    assert result == expected

def test_area_regular_hexagon_side_1():
    # Calculate area of a regular hexagon with side length 1
    result = area_polygon(s=6, l=1)
    expected = 2.598076211353316
    assert result == expected

def test_area_regular_octagon_side_2_5():
    # Calculate area of a regular octagon with side length 2.5
    result = area_polygon(s=8, l=2.5)
    expected = 30.1270508520413
    assert result == expected