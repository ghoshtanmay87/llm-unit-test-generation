def perimeter_triangle(a,b,c):
  perimeter=a+b+c
  return perimeter

import pytest

def test_perimeter_triangle_all_sides_equal():
    # Calculate perimeter of a triangle with all sides equal
    result = perimeter_triangle(a=3, b=3, c=3)
    assert result == 9

def test_perimeter_triangle_different_side_lengths():
    # Calculate perimeter of a triangle with different side lengths
    result = perimeter_triangle(a=4, b=5, c=6)
    assert result == 15

def test_perimeter_triangle_one_side_zero():
    # Calculate perimeter of a triangle with one side zero
    result = perimeter_triangle(a=0, b=7, c=8)
    assert result == 15

def test_perimeter_triangle_floating_point_sides():
    # Calculate perimeter of a triangle with floating point sides
    result = perimeter_triangle(a=2.5, b=3.5, c=4.0)
    assert result == 10.0

def test_perimeter_triangle_large_side_lengths():
    # Calculate perimeter of a triangle with large side lengths
    result = perimeter_triangle(a=1000, b=2000, c=3000)
    assert result == 6000