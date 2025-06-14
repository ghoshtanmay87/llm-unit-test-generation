def volume_cube(l):
  volume = l * l * l
  return volume

import pytest

def test_volume_cube_side_length_3():
    # Calculate volume of a cube with side length 3
    result = volume_cube(l=3)
    assert result == 27

def test_volume_cube_side_length_0():
    # Calculate volume of a cube with side length 0
    result = volume_cube(l=0)
    assert result == 0

def test_volume_cube_side_length_1():
    # Calculate volume of a cube with side length 1
    result = volume_cube(l=1)
    assert result == 1

def test_volume_cube_side_length_2_point_5():
    # Calculate volume of a cube with side length 2.5
    result = volume_cube(l=2.5)
    assert result == 15.625

def test_volume_cube_side_length_10():
    # Calculate volume of a cube with side length 10
    result = volume_cube(l=10)
    assert result == 1000