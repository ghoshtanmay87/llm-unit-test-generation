import math
def radian_degree(degree):
 radian = degree*(math.pi/180)
 return radian

import pytest

def test_convert_0_degrees_to_radians():
    # 0 degrees multiplied by pi/180 equals 0 radians.
    result = radian_degree(0)
    assert result == 0.0

def test_convert_180_degrees_to_radians():
    # 180 degrees multiplied by pi/180 equals pi radians, approximately 3.141592653589793.
    result = radian_degree(180)
    assert result == 3.141592653589793

def test_convert_90_degrees_to_radians():
    # 90 degrees multiplied by pi/180 equals pi/2 radians, approximately 1.5707963267948966.
    result = radian_degree(90)
    assert result == 1.5707963267948966

def test_convert_45_degrees_to_radians():
    # 45 degrees multiplied by pi/180 equals pi/4 radians, approximately 0.7853981633974483.
    result = radian_degree(45)
    assert result == 0.7853981633974483

def test_convert_negative_90_degrees_to_radians():
    # -90 degrees multiplied by pi/180 equals -pi/2 radians, approximately -1.5707963267948966.
    result = radian_degree(-90)
    assert result == -1.5707963267948966