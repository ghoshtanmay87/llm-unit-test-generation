def rombus_area(p,q):
  area=(p*q)/2
  return area

import pytest

def test_area_with_positive_integers():
    # Calculate area of rhombus with positive integers
    p = 10
    q = 8
    expected = 40.0
    assert rombus_area(p, q) == expected

def test_area_with_one_side_zero():
    # Calculate area of rhombus with one side zero
    p = 0
    q = 5
    expected = 0.0
    assert rombus_area(p, q) == expected

def test_area_with_floating_point_diagonals():
    # Calculate area of rhombus with floating point diagonals
    p = 7.5
    q = 4.2
    expected = 15.75
    assert rombus_area(p, q) == expected

def test_area_with_equal_diagonals():
    # Calculate area of rhombus with equal diagonals
    p = 6
    q = 6
    expected = 18.0
    assert rombus_area(p, q) == expected

def test_area_with_large_diagonals():
    # Calculate area of rhombus with large diagonals
    p = 1000
    q = 2000
    expected = 1000000.0
    assert rombus_area(p, q) == expected