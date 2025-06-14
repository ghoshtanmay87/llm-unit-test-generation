def volume_cylinder(r,h):
  volume=3.1415*r*r*h
  return volume

import pytest

def test_volume_cylinder_radius_1_height_1():
    # Calculate volume with radius 1 and height 1
    result = volume_cylinder(r=1, h=1)
    assert result == 3.1415

def test_volume_cylinder_radius_2_height_3():
    # Calculate volume with radius 2 and height 3
    result = volume_cylinder(r=2, h=3)
    assert result == 37.698

def test_volume_cylinder_radius_0_height_5():
    # Calculate volume with radius 0 and height 5
    result = volume_cylinder(r=0, h=5)
    assert result == 0.0

def test_volume_cylinder_radius_3_5_height_10():
    # Calculate volume with radius 3.5 and height 10
    result = volume_cylinder(r=3.5, h=10)
    assert result == 384.84725

def test_volume_cylinder_radius_5_height_0():
    # Calculate volume with radius 5 and height 0
    result = volume_cylinder(r=5, h=0)
    assert result == 0.0