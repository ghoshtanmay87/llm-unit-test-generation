import math
def perimeter_pentagon(a):
  perimeter=(5*a)
  return perimeter

import pytest

def test_perimeter_pentagon_side_length_1():
    # Calculate perimeter for a regular pentagon with side length 1
    result = perimeter_pentagon(a=1)
    assert result == 5

def test_perimeter_pentagon_side_length_0():
    # Calculate perimeter for a regular pentagon with side length 0
    result = perimeter_pentagon(a=0)
    assert result == 0

def test_perimeter_pentagon_side_length_2_point_5():
    # Calculate perimeter for a regular pentagon with side length 2.5
    result = perimeter_pentagon(a=2.5)
    assert result == 12.5

def test_perimeter_pentagon_side_length_10():
    # Calculate perimeter for a regular pentagon with side length 10
    result = perimeter_pentagon(a=10)
    assert result == 50

def test_perimeter_pentagon_side_length_0_point_1():
    # Calculate perimeter for a regular pentagon with side length 0.1
    result = perimeter_pentagon(a=0.1)
    assert result == 0.5