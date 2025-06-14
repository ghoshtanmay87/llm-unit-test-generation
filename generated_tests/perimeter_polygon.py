from math import tan, pi
def perimeter_polygon(s,l):
  perimeter = s*l
  return perimeter

import pytest

def test_perimeter_polygon_three_sides_length_five():
    # Calculate perimeter of a polygon with 3 sides each of length 5
    result = perimeter_polygon(s=3, l=5)
    assert result == 15

def test_perimeter_polygon_four_sides_length_ten():
    # Calculate perimeter of a polygon with 4 sides each of length 10
    result = perimeter_polygon(s=4, l=10)
    assert result == 40

def test_perimeter_polygon_six_sides_length_seven_point_five():
    # Calculate perimeter of a polygon with 6 sides each of length 7.5
    result = perimeter_polygon(s=6, l=7.5)
    assert result == 45.0

def test_perimeter_polygon_zero_sides_length_ten():
    # Calculate perimeter of a polygon with 0 sides and length 10
    result = perimeter_polygon(s=0, l=10)
    assert result == 0

def test_perimeter_polygon_five_sides_length_zero():
    # Calculate perimeter of a polygon with 5 sides each of length 0
    result = perimeter_polygon(s=5, l=0)
    assert result == 0