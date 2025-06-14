def any_int(x, y, z):
    if isinstance(x, int) and isinstance(y, int) and isinstance(z, int):
        if x + y == z or x + z == y or y + z == x:
            return True
        return False
    return False

import pytest

def test_all_integers_x_plus_y_equals_z():
    # All inputs are integers and 2 + 3 equals 5, so the function returns True.
    assert any_int(2, 3, 5) is True

def test_all_integers_x_plus_z_equals_y():
    # All inputs are integers and 4 + 5 equals 9, so the function returns True.
    assert any_int(4, 9, 5) is True

def test_all_integers_y_plus_z_equals_x():
    # All inputs are integers and 6 + 4 equals 10, so the function returns True.
    assert any_int(10, 6, 4) is True

def test_all_integers_no_sum_condition_met():
    # All inputs are integers but none of the sums (1+2, 1+4, 2+4) equal the third number, so the function returns False.
    assert any_int(1, 2, 4) is False

def test_one_input_not_integer_float():
    # x is a float, not an integer, so the function returns False without checking sums.
    assert any_int(1.0, 2, 3) is False

def test_one_input_not_integer_string():
    # y is a string, not an integer, so the function returns False without checking sums.
    assert any_int(1, "2", 3) is False

def test_all_integers_all_zero():
    # All inputs are integers and 0 + 0 equals 0, so the function returns True.
    assert any_int(0, 0, 0) is True

def test_negative_integers_sum_condition_met():
    # All inputs are integers and -1 + -2 equals -3, so the function returns True.
    assert any_int(-1, -2, -3) is True

def test_negative_integers_sum_condition_not_met():
    # All inputs are integers but none of the sums (-1+-2, -1+-4, -2+-4) equal the third number, so the function returns False.
    assert any_int(-1, -2, -4) is False

def test_mixed_types_with_boolean():
    # Booleans are subclasses of int in Python, so isinstance(True, int) is True. 1 + 1 equals 2, so the function returns True.
    assert any_int(True, 1, 2) is True