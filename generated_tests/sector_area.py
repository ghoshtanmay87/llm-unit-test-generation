def sector_area(r,a):
    pi=22/7
    if a >= 360:
        return None
    sectorarea = (pi*r**2) * (a/360)
    return sectorarea

import pytest

def test_sector_area_radius_7_angle_90():
    # Calculate sector area for radius 7 and angle 90 degrees
    result = sector_area(7, 90)
    assert result == 38.5

def test_sector_area_radius_10_angle_180():
    # Calculate sector area for radius 10 and angle 180 degrees
    result = sector_area(10, 180)
    assert result == 157.14285714285714

def test_sector_area_angle_equal_360_returns_none():
    # Return None for angle equal to 360 degrees
    result = sector_area(5, 360)
    assert result is None

def test_sector_area_angle_greater_than_360_returns_none():
    # Return None for angle greater than 360 degrees
    result = sector_area(3, 400)
    assert result is None

def test_sector_area_radius_0_angle_45():
    # Calculate sector area for radius 0 and angle 45 degrees
    result = sector_area(0, 45)
    assert result == 0.0

def test_sector_area_radius_1_angle_0():
    # Calculate sector area for radius 1 and angle 0 degrees
    result = sector_area(1, 0)
    assert result == 0.0