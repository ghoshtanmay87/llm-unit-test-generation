def lateralsuface_cylinder(r,h):
  lateralsurface= 2*3.1415*r*h
  return lateralsurface

import pytest

def test_lateral_surface_area_radius_1_height_1():
    # Calculate lateral surface area for radius 1 and height 1
    r = 1
    h = 1
    expected_output = 6.283
    assert lateralsuface_cylinder(r, h) == expected_output

def test_lateral_surface_area_radius_2_height_3():
    # Calculate lateral surface area for radius 2 and height 3
    r = 2
    h = 3
    expected_output = 37.698
    assert lateralsuface_cylinder(r, h) == expected_output

def test_lateral_surface_area_radius_0_height_5():
    # Calculate lateral surface area for radius 0 and height 5
    r = 0
    h = 5
    expected_output = 0.0
    assert lateralsuface_cylinder(r, h) == expected_output

def test_lateral_surface_area_radius_5_height_0():
    # Calculate lateral surface area for radius 5 and height 0
    r = 5
    h = 0
    expected_output = 0.0
    assert lateralsuface_cylinder(r, h) == expected_output

def test_lateral_surface_area_radius_3_5_height_4_2():
    # Calculate lateral surface area for radius 3.5 and height 4.2
    r = 3.5
    h = 4.2
    expected_output = 92.3994
    assert lateralsuface_cylinder(r, h) == expected_output