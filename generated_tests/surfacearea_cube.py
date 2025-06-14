def surfacearea_cube(l):
  surfacearea= 6*l*l
  return surfacearea

import pytest

def test_surface_area_cube_side_length_1():
    # Calculate surface area for a cube with side length 1
    result = surfacearea_cube(l=1)
    assert result == 6

def test_surface_area_cube_side_length_0():
    # Calculate surface area for a cube with side length 0
    result = surfacearea_cube(l=0)
    assert result == 0

def test_surface_area_cube_side_length_2():
    # Calculate surface area for a cube with side length 2
    result = surfacearea_cube(l=2)
    assert result == 24

def test_surface_area_cube_side_length_3_point_5():
    # Calculate surface area for a cube with side length 3.5
    result = surfacearea_cube(l=3.5)
    assert result == 73.5

def test_surface_area_cube_side_length_10():
    # Calculate surface area for a cube with side length 10
    result = surfacearea_cube(l=10)
    assert result == 600