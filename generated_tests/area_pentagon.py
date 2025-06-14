import math
def area_pentagon(a):
  area=(math.sqrt(5*(5+2*math.sqrt(5)))*pow(a,2))/4.0
  return area

import pytest

def test_area_pentagon_side_1():
    # Calculate area of a regular pentagon with side length 1
    result = area_pentagon(a=1)
    expected = 1.720477400588967
    assert result == expected

def test_area_pentagon_side_2():
    # Calculate area of a regular pentagon with side length 2
    result = area_pentagon(a=2)
    expected = 6.881909602355868
    assert result == expected

def test_area_pentagon_side_0():
    # Calculate area of a regular pentagon with side length 0
    result = area_pentagon(a=0)
    expected = 0.0
    assert result == expected

def test_area_pentagon_side_5():
    # Calculate area of a regular pentagon with side length 5
    result = area_pentagon(a=5)
    expected = 43.01193501472417
    assert result == expected

def test_area_pentagon_side_0_5():
    # Calculate area of a regular pentagon with side length 0.5
    result = area_pentagon(a=0.5)
    expected = 0.4301193501472417
    assert result == expected