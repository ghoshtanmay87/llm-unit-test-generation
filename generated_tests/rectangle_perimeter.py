def rectangle_perimeter(l,b):
  perimeter=2*(l+b)
  return perimeter

import pytest

def test_perimeter_rectangle_length_5_breadth_3():
    # Calculate perimeter for a rectangle with length 5 and breadth 3
    result = rectangle_perimeter(l=5, b=3)
    assert result == 16

def test_perimeter_square_side_length_4():
    # Calculate perimeter for a square with side length 4 (length and breadth equal)
    result = rectangle_perimeter(l=4, b=4)
    assert result == 16

def test_perimeter_rectangle_length_0_breadth_7():
    # Calculate perimeter for a rectangle with length 0 and breadth 7
    result = rectangle_perimeter(l=0, b=7)
    assert result == 14

def test_perimeter_rectangle_length_10_5_breadth_4_5():
    # Calculate perimeter for a rectangle with length 10.5 and breadth 4.5
    result = rectangle_perimeter(l=10.5, b=4.5)
    assert result == 30.0

def test_perimeter_rectangle_length_1_breadth_1():
    # Calculate perimeter for a rectangle with length 1 and breadth 1
    result = rectangle_perimeter(l=1, b=1)
    assert result == 4