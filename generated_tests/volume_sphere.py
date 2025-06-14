import math
def volume_sphere(r):
  volume=(4/3)*math.pi*r*r*r
  return volume

import pytest

def test_volume_sphere_radius_zero():
    # Calculate volume of a sphere with radius 0
    r = 0
    expected = 0.0
    assert volume_sphere(r) == expected

def test_volume_sphere_radius_one():
    # Calculate volume of a sphere with radius 1
    r = 1
    expected = 4.1887902047863905
    assert volume_sphere(r) == expected

def test_volume_sphere_radius_two():
    # Calculate volume of a sphere with radius 2
    r = 2
    expected = 33.510321638291124
    assert volume_sphere(r) == expected

def test_volume_sphere_radius_half():
    # Calculate volume of a sphere with radius 0.5
    r = 0.5
    expected = 0.5235987755982988
    assert volume_sphere(r) == expected

def test_volume_sphere_radius_ten():
    # Calculate volume of a sphere with radius 10
    r = 10
    expected = 4188.790204786391
    assert volume_sphere(r) == expected