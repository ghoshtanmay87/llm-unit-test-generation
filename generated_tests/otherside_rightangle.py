import math
def otherside_rightangle(w,h):
  s=math.sqrt((w*w)+(h*h))
  return s

import pytest

def test_hypotenuse_sides_3_and_4():
    # Calculate hypotenuse for a right triangle with sides 3 and 4
    result = otherside_rightangle(3, 4)
    assert result == 5.0

def test_hypotenuse_sides_5_and_12():
    # Calculate hypotenuse for a right triangle with sides 5 and 12
    result = otherside_rightangle(5, 12)
    assert result == 13.0

def test_hypotenuse_sides_0_and_0():
    # Calculate hypotenuse for a right triangle with sides 0 and 0
    result = otherside_rightangle(0, 0)
    assert result == 0.0

def test_hypotenuse_sides_1_and_1():
    # Calculate hypotenuse for a right triangle with sides 1 and 1
    result = otherside_rightangle(1, 1)
    assert result == 1.4142135623730951

def test_hypotenuse_sides_8_and_15():
    # Calculate hypotenuse for a right triangle with sides 8 and 15
    result = otherside_rightangle(8, 15)
    assert result == 17.0