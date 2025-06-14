def lateralsurface_cuboid(l,w,h):
  LSA = 2*h*(l+w)
  return LSA

import pytest

def test_lateralsurface_cuboid_all_sides_equal_1():
    # Calculate lateral surface area for a cuboid with all sides equal to 1
    result = lateralsurface_cuboid(l=1, w=1, h=1)
    assert result == 4

def test_lateralsurface_cuboid_length_2_width_3_height_4():
    # Calculate lateral surface area for a cuboid with length 2, width 3, height 4
    result = lateralsurface_cuboid(l=2, w=3, h=4)
    assert result == 40

def test_lateralsurface_cuboid_length_0_width_5_height_10():
    # Calculate lateral surface area for a cuboid with length 0, width 5, height 10
    result = lateralsurface_cuboid(l=0, w=5, h=10)
    assert result == 100

def test_lateralsurface_cuboid_length_7_5_width_2_5_height_3_0():
    # Calculate lateral surface area for a cuboid with length 7.5, width 2.5, height 3.0
    result = lateralsurface_cuboid(l=7.5, w=2.5, h=3.0)
    assert result == 60.0

def test_lateralsurface_cuboid_length_10_width_0_height_0():
    # Calculate lateral surface area for a cuboid with length 10, width 0, height 0
    result = lateralsurface_cuboid(l=10, w=0, h=0)
    assert result == 0