def surfacearea_cylinder(r,h):
  surfacearea=((2*3.1415*r*r) +(2*3.1415*r*h))
  return surfacearea

import pytest

def test_surface_area_cylinder_radius_1_height_1():
    # Calculate surface area for a cylinder with radius 1 and height 1
    r = 1
    h = 1
    expected_output = 12.566
    result = surfacearea_cylinder(r, h)
    assert result == expected_output

def test_surface_area_cylinder_radius_0_height_5():
    # Calculate surface area for a cylinder with radius 0 and height 5
    r = 0
    h = 5
    expected_output = 0.0
    result = surfacearea_cylinder(r, h)
    assert result == expected_output

def test_surface_area_cylinder_radius_2_height_3():
    # Calculate surface area for a cylinder with radius 2 and height 3
    r = 2
    h = 3
    expected_output = 62.831
    result = surfacearea_cylinder(r, h)
    assert result == expected_output

def test_surface_area_cylinder_radius_5_height_0():
    # Calculate surface area for a cylinder with radius 5 and height 0
    r = 5
    h = 0
    expected_output = 157.075
    result = surfacearea_cylinder(r, h)
    assert result == expected_output

def test_surface_area_cylinder_radius_3_5_height_7_2():
    # Calculate surface area for a cylinder with radius 3.5 and height 7.2
    r = 3.5
    h = 7.2
    expected_output = 197.9203
    result = surfacearea_cylinder(r, h)
    assert result == expected_output