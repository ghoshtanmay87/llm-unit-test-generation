import math
def volume_cone(r,h):
  volume = (1.0/3) * math.pi * r * r * h
  return volume

import pytest

def test_volume_cone_radius_1_height_1():
    # Calculate volume of cone with radius 1 and height 1
    result = volume_cone(r=1, h=1)
    assert result == 1.0471975511965976

def test_volume_cone_radius_0_height_10():
    # Calculate volume of cone with radius 0 and height 10
    result = volume_cone(r=0, h=10)
    assert result == 0.0

def test_volume_cone_radius_3_height_5():
    # Calculate volume of cone with radius 3 and height 5
    result = volume_cone(r=3, h=5)
    assert result == 47.12388980384689

def test_volume_cone_radius_2_5_height_4_2():
    # Calculate volume of cone with radius 2.5 and height 4.2
    result = volume_cone(r=2.5, h=4.2)
    assert result == 27.46345626423244

def test_volume_cone_radius_10_height_0():
    # Calculate volume of cone with radius 10 and height 0
    result = volume_cone(r=10, h=0)
    assert result == 0.0