def find_angle(a,b):
 c = 180 - (a + b)
 return c

import pytest

def test_third_angle_with_60_and_60():
    # Calculate the third angle of a triangle when given two angles 60 and 60
    result = find_angle(60, 60)
    assert result == 60

def test_third_angle_with_90_and_45():
    # Calculate the third angle of a triangle when given two angles 90 and 45
    result = find_angle(90, 45)
    assert result == 45

def test_third_angle_with_30_and_70():
    # Calculate the third angle of a triangle when given two angles 30 and 70
    result = find_angle(30, 70)
    assert result == 80

def test_third_angle_with_0_and_0():
    # Calculate the third angle of a triangle when given two angles 0 and 0
    result = find_angle(0, 0)
    assert result == 180

def test_third_angle_with_90_and_90():
    # Calculate the third angle of a triangle when given two angles 90 and 90
    result = find_angle(90, 90)
    assert result == 0