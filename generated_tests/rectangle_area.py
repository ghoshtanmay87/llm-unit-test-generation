def rectangle_area(l,b):
  area=l*b
  return area

import pytest

def test_area_positive_integers():
    # Calculate area for positive integer length and breadth
    result = rectangle_area(5, 10)
    assert result == 50

def test_area_zero_length():
    # Calculate area for zero length
    result = rectangle_area(0, 10)
    assert result == 0

def test_area_zero_breadth():
    # Calculate area for zero breadth
    result = rectangle_area(7, 0)
    assert result == 0

def test_area_floating_point_values():
    # Calculate area for floating point length and breadth
    result = rectangle_area(3.5, 2.0)
    assert result == 7.0

def test_area_length_and_breadth_one():
    # Calculate area for both length and breadth as 1
    result = rectangle_area(1, 1)
    assert result == 1

def test_area_negative_length_positive_breadth():
    # Calculate area for negative length and positive breadth
    result = rectangle_area(-4, 5)
    assert result == -20

def test_area_positive_length_negative_breadth():
    # Calculate area for positive length and negative breadth
    result = rectangle_area(6, -3)
    assert result == -18

def test_area_negative_length_negative_breadth():
    # Calculate area for negative length and negative breadth
    result = rectangle_area(-2, -8)
    assert result == 16