def topbottom_surfacearea(r):
  toporbottomarea=3.1415*r*r
  return toporbottomarea

import pytest

def test_surface_area_radius_zero():
    # Calculate surface area of top or bottom of a circle with radius 0
    result = topbottom_surfacearea(0)
    assert result == 0.0

def test_surface_area_radius_one():
    # Calculate surface area of top or bottom of a circle with radius 1
    result = topbottom_surfacearea(1)
    assert result == 3.1415

def test_surface_area_radius_two():
    # Calculate surface area of top or bottom of a circle with radius 2
    result = topbottom_surfacearea(2)
    assert result == 12.566

def test_surface_area_radius_three_point_five():
    # Calculate surface area of top or bottom of a circle with radius 3.5
    result = topbottom_surfacearea(3.5)
    assert result == 38.484125

def test_surface_area_radius_ten():
    # Calculate surface area of top or bottom of a circle with radius 10
    result = topbottom_surfacearea(10)
    assert result == 314.15