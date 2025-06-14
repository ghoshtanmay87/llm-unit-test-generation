def circle_circumference(r):
  perimeter=2*3.1415*r
  return perimeter

import pytest

def test_circumference_radius_zero():
    # Calculate circumference for radius 0
    result = circle_circumference(r=0)
    assert result == 0.0

def test_circumference_radius_one():
    # Calculate circumference for radius 1
    result = circle_circumference(r=1)
    assert result == 6.283

def test_circumference_radius_two_point_five():
    # Calculate circumference for radius 2.5
    result = circle_circumference(r=2.5)
    assert result == 15.7075

def test_circumference_radius_ten():
    # Calculate circumference for radius 10
    result = circle_circumference(r=10)
    assert result == 62.83

def test_circumference_radius_point_one():
    # Calculate circumference for radius 0.1
    result = circle_circumference(r=0.1)
    assert result == 0.6283