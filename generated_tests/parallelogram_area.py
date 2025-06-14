def parallelogram_area(b,h):
  area=b*h
  return area

import pytest

def test_calculate_area_with_positive_integers():
    # The function multiplies base 5 by height 10, resulting in area 50.
    assert parallelogram_area(b=5, h=10) == 50

def test_calculate_area_with_zero_base():
    # Base is zero, so area is 0 regardless of height.
    assert parallelogram_area(b=0, h=10) == 0

def test_calculate_area_with_zero_height():
    # Height is zero, so area is 0 regardless of base.
    assert parallelogram_area(b=5, h=0) == 0

def test_calculate_area_with_floating_point_numbers():
    # The function multiplies base 3.5 by height 2.0, resulting in area 7.0.
    assert parallelogram_area(b=3.5, h=2.0) == 7.0

def test_calculate_area_with_both_base_and_height_as_floats():
    # The function multiplies base 4.2 by height 3.3, resulting in area 13.86.
    assert parallelogram_area(b=4.2, h=3.3) == 13.86

def test_calculate_area_with_negative_base():
    # The function multiplies base -5 by height 10, resulting in area -50.
    assert parallelogram_area(b=-5, h=10) == -50

def test_calculate_area_with_negative_height():
    # The function multiplies base 5 by height -10, resulting in area -50.
    assert parallelogram_area(b=5, h=-10) == -50

def test_calculate_area_with_both_base_and_height_negative():
    # The function multiplies base -5 by height -10, resulting in area 50 because negative times negative is positive.
    assert parallelogram_area(b=-5, h=-10) == 50