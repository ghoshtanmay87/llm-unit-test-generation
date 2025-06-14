def surfacearea_cuboid(l,w,h):
  SA = 2*(l*w + l * h + w * h)
  return SA

import pytest

def test_surface_area_all_sides_equal_1():
    # Calculate surface area for a cuboid with all sides equal to 1
    result = surfacearea_cuboid(l=1, w=1, h=1)
    assert result == 6

def test_surface_area_length_2_width_3_height_4():
    # Calculate surface area for a cuboid with length 2, width 3, height 4
    result = surfacearea_cuboid(l=2, w=3, h=4)
    assert result == 52

def test_surface_area_length_0_width_5_height_7():
    # Calculate surface area for a cuboid with length 0, width 5, height 7
    result = surfacearea_cuboid(l=0, w=5, h=7)
    assert result == 70

def test_surface_area_length_1_5_width_2_5_height_3_5():
    # Calculate surface area for a cuboid with length 1.5, width 2.5, height 3.5
    result = surfacearea_cuboid(l=1.5, w=2.5, h=3.5)
    assert result == 40.5

def test_surface_area_length_10_width_10_height_10():
    # Calculate surface area for a cuboid with length 10, width 10, height 10
    result = surfacearea_cuboid(l=10, w=10, h=10)
    assert result == 600