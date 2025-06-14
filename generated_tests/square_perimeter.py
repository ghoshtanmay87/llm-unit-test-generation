def square_perimeter(a):
  perimeter=4*a
  return perimeter

import pytest

def test_perimeter_positive_integer():
    # Calculate perimeter for a positive integer side length
    result = square_perimeter(a=5)
    assert result == 20

def test_perimeter_zero_length():
    # Calculate perimeter for zero side length
    result = square_perimeter(a=0)
    assert result == 0

def test_perimeter_positive_float():
    # Calculate perimeter for a positive float side length
    result = square_perimeter(a=2.5)
    assert result == 10.0

def test_perimeter_negative_length():
    # Calculate perimeter for a negative side length
    result = square_perimeter(a=-3)
    assert result == -12

def test_perimeter_large_length():
    # Calculate perimeter for a large side length
    result = square_perimeter(a=1000)
    assert result == 4000