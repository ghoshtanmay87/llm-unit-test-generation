def parallelogram_perimeter(b,h):
  perimeter=2*(b*h)
  return perimeter

import pytest

def test_perimeter_base_5_height_10():
    # Calculate perimeter with base 5 and height 10
    result = parallelogram_perimeter(b=5, h=10)
    assert result == 100

def test_perimeter_base_3_height_4():
    # Calculate perimeter with base 3 and height 4
    result = parallelogram_perimeter(b=3, h=4)
    assert result == 24

def test_perimeter_base_0_height_10():
    # Calculate perimeter with base 0 and height 10
    result = parallelogram_perimeter(b=0, h=10)
    assert result == 0

def test_perimeter_base_7_5_height_2_5():
    # Calculate perimeter with base 7.5 and height 2.5
    result = parallelogram_perimeter(b=7.5, h=2.5)
    assert result == 37.5

def test_perimeter_base_1_height_1():
    # Calculate perimeter with base 1 and height 1
    result = parallelogram_perimeter(b=1, h=1)
    assert result == 2