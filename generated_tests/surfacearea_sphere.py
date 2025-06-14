import math
def surfacearea_sphere(r):
  surfacearea=4*math.pi*r*r
  return surfacearea

import pytest

def test_surfacearea_sphere_radius_1():
    # Calculate surface area for radius 1
    r = 1
    expected = 12.566370614359172
    result = surfacearea_sphere(r)
    assert result == expected

def test_surfacearea_sphere_radius_0():
    # Calculate surface area for radius 0
    r = 0
    expected = 0.0
    result = surfacearea_sphere(r)
    assert result == expected

def test_surfacearea_sphere_radius_2_5():
    # Calculate surface area for radius 2.5
    r = 2.5
    expected = 78.53981633974483
    result = surfacearea_sphere(r)
    assert result == expected

def test_surfacearea_sphere_radius_10():
    # Calculate surface area for radius 10
    r = 10
    expected = 1256.6370614359173
    result = surfacearea_sphere(r)
    assert result == expected

def test_surfacearea_sphere_radius_0_1():
    # Calculate surface area for radius 0.1
    r = 0.1
    expected = 0.12566370614359174
    result = surfacearea_sphere(r)
    assert result == expected