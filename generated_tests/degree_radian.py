import math
def degree_radian(radian):
 degree = radian*(180/math.pi)
 return degree

import pytest

def test_convert_0_radians_to_degrees():
    # 0 radians multiplied by 180/pi equals 0 degrees.
    result = degree_radian(0)
    assert result == 0.0

def test_convert_pi_radians_to_degrees():
    # pi radians multiplied by 180/pi equals 180 degrees.
    result = degree_radian(3.141592653589793)
    assert result == 180.0

def test_convert_pi_over_2_radians_to_degrees():
    # pi/2 radians multiplied by 180/pi equals 90 degrees.
    result = degree_radian(1.5707963267948966)
    assert result == 90.0

def test_convert_negative_pi_radians_to_degrees():
    # Negative pi radians multiplied by 180/pi equals -180 degrees.
    result = degree_radian(-3.141592653589793)
    assert result == -180.0

def test_convert_2_pi_radians_to_degrees():
    # 2*pi radians multiplied by 180/pi equals 360 degrees.
    result = degree_radian(6.283185307179586)
    assert result == 360.0