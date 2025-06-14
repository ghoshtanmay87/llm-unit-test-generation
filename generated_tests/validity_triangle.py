def validity_triangle(a,b,c):
 total = a + b + c
 if total == 180:
    return True
 else:
    return False

import pytest

def test_all_angles_sum_exactly_180_degrees():
    # The sum of angles 60 + 60 + 60 equals 180, so the function returns True.
    assert validity_triangle(60, 60, 60) is True

def test_angles_sum_less_than_180_degrees():
    # The sum of angles 50 + 60 + 60 equals 170, which is not 180, so the function returns False.
    assert validity_triangle(50, 60, 60) is False

def test_angles_sum_greater_than_180_degrees():
    # The sum of angles 90 + 60 + 40 equals 190, which is not 180, so the function returns False.
    assert validity_triangle(90, 60, 40) is False

def test_one_angle_is_zero_sum_equals_180():
    # The sum of angles 0 + 90 + 90 equals 180, so the function returns True even though one angle is zero.
    assert validity_triangle(0, 90, 90) is True

def test_zero_angle_included_sum_equals_180():
    # The sum of angles 100 + 80 + 0 equals 180, so the function returns True despite zero angle.
    assert validity_triangle(100, 80, 0) is True

def test_negative_angle_included_sum_not_equal_180():
    # The sum of angles 100 + 80 + (-10) equals 170, which is not 180, so the function returns False.
    assert validity_triangle(100, 80, -10) is False

def test_floating_point_angles_summing_to_180():
    # The sum of angles 59.5 + 60.5 + 60.0 equals exactly 180.0, so the function returns True.
    assert validity_triangle(59.5, 60.5, 60.0) is True

def test_floating_point_angles_summing_close_but_not_equal_180():
    # The sum of angles 59.5 + 60.5 + 59.9 equals 179.9, which is not exactly 180, so the function returns False.
    assert validity_triangle(59.5, 60.5, 59.9) is False