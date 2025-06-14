def check_isosceles(x,y,z):
  if x==y or y==z or z==x:
	   return True
  else:
     return False

import pytest

def test_all_sides_equal_equilateral_triangle():
    # Since x == y == z, at least two sides are equal, so the function returns True.
    assert check_isosceles(5, 5, 5) is True

def test_two_sides_equal_one_different_xy_equal():
    # x equals y, so the function returns True because at least two sides are equal.
    assert check_isosceles(7, 7, 10) is True

def test_two_sides_equal_one_different_yz_equal():
    # y equals z, so the function returns True because at least two sides are equal.
    assert check_isosceles(4, 6, 6) is True

def test_two_sides_equal_one_different_xz_equal():
    # x equals z, so the function returns True because at least two sides are equal.
    assert check_isosceles(8, 3, 8) is True

def test_no_sides_equal():
    # No two sides are equal, so the function returns False.
    assert check_isosceles(3, 4, 5) is False

def test_all_sides_different_floating_point_values():
    # No two sides are equal, so the function returns False.
    assert check_isosceles(2.5, 3.5, 4.5) is False

def test_two_sides_equal_floating_point_values():
    # x equals y, so the function returns True because at least two sides are equal.
    assert check_isosceles(7.1, 7.1, 9.0) is True