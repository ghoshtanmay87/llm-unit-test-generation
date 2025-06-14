def right_angle_triangle(a, b, c):
    return a * a == b * b + c * c or b * b == a * a + c * c or c * c == a * a + b * b

import pytest

def test_right_angle_triangle_3_4_5():
    # Check if (3, 4, 5) forms a right angle triangle
    assert right_angle_triangle(3, 4, 5) is True

def test_right_angle_triangle_5_12_13():
    # Check if (5, 12, 13) forms a right angle triangle
    assert right_angle_triangle(5, 12, 13) is True

def test_right_angle_triangle_1_1_1():
    # Check if (1, 1, 1) forms a right angle triangle
    assert right_angle_triangle(1, 1, 1) is False

def test_right_angle_triangle_6_8_10():
    # Check if (6, 8, 10) forms a right angle triangle
    assert right_angle_triangle(6, 8, 10) is True

def test_right_angle_triangle_7_24_25():
    # Check if (7, 24, 25) forms a right angle triangle
    assert right_angle_triangle(7, 24, 25) is True

def test_right_angle_triangle_2_3_4():
    # Check if (2, 3, 4) forms a right angle triangle
    assert right_angle_triangle(2, 3, 4) is False

def test_right_angle_triangle_0_0_0():
    # Check if (0, 0, 0) forms a right angle triangle
    assert right_angle_triangle(0, 0, 0) is True

def test_right_angle_triangle_10_6_8():
    # Check if (10, 6, 8) forms a right angle triangle with sides in different order
    assert right_angle_triangle(10, 6, 8) is True