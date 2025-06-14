def lateralsurface_cube(l):
  LSA = 4 * (l * l)
  return LSA

import pytest

def test_lateralsurface_cube_side_length_1():
    # Calculate lateral surface area for cube with side length 1
    result = lateralsurface_cube(l=1)
    assert result == 4

def test_lateralsurface_cube_side_length_2():
    # Calculate lateral surface area for cube with side length 2
    result = lateralsurface_cube(l=2)
    assert result == 16

def test_lateralsurface_cube_side_length_0():
    # Calculate lateral surface area for cube with side length 0
    result = lateralsurface_cube(l=0)
    assert result == 0

def test_lateralsurface_cube_side_length_3_point_5():
    # Calculate lateral surface area for cube with side length 3.5
    result = lateralsurface_cube(l=3.5)
    assert result == 49.0

def test_lateralsurface_cube_side_length_10():
    # Calculate lateral surface area for cube with side length 10
    result = lateralsurface_cube(l=10)
    assert result == 400