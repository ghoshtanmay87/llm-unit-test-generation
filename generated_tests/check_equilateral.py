def check_equilateral(x,y,z):
  if x == y == z:
	   return True
  else:
     return False

import pytest

def test_all_sides_are_equal():
    result = check_equilateral(5, 5, 5)
    assert result is True

def test_two_sides_equal_one_different():
    result = check_equilateral(5, 5, 3)
    assert result is False

def test_all_sides_different():
    result = check_equilateral(2, 3, 4)
    assert result is False

def test_all_sides_zero():
    result = check_equilateral(0, 0, 0)
    assert result is True

def test_sides_are_equal_floating_point_numbers():
    result = check_equilateral(3.5, 3.5, 3.5)
    assert result is True

def test_sides_are_equal_negative_numbers():
    result = check_equilateral(-1, -1, -1)
    assert result is True

def test_two_sides_equal_negative_one_different_positive():
    result = check_equilateral(-1, -1, 1)
    assert result is False