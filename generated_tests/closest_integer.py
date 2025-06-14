def closest_integer(value):
    from math import floor, ceil
    if value.count('.') == 1:
        while value[-1] == '0':
            value = value[:-1]
    num = float(value)
    if value[-2:] == '.5':
        if num > 0:
            res = ceil(num)
        else:
            res = floor(num)
    elif len(value) > 0:
        res = int(round(num))
    else:
        res = 0
    return res

import pytest

def test_positive_decimal_ending_with_point_five_should_round_up():
    # Input is a positive decimal ending with .5, should round up
    result = closest_integer('2.5')
    assert result == 3

def test_negative_decimal_ending_with_point_five_should_round_down():
    # Input is a negative decimal ending with .5, should round down
    result = closest_integer('-2.5')
    assert result == -3

def test_positive_decimal_with_trailing_zeros_ending_with_point_five_should_round_up():
    # Input is a positive decimal with trailing zeros after decimal, should trim zeros and round normally
    result = closest_integer('3.5000')
    assert result == 4

def test_negative_decimal_with_trailing_zeros_ending_with_point_five_should_round_down():
    # Input is a negative decimal with trailing zeros after decimal, should trim zeros and round normally
    result = closest_integer('-3.5000')
    assert result == -4

def test_positive_decimal_not_ending_with_point_five_should_round_normally():
    # Input is a positive decimal not ending with .5, should round normally
    result = closest_integer('2.49')
    assert result == 2

def test_negative_decimal_not_ending_with_point_five_should_round_normally():
    # Input is a negative decimal not ending with .5, should round normally
    result = closest_integer('-2.49')
    assert result == -2

def test_integer_string_should_convert_directly():
    # Input is an integer string, should convert directly
    result = closest_integer('5')
    assert result == 5

def test_zero_string_should_return_zero():
    # Input is zero as a string, should return zero
    result = closest_integer('0')
    assert result == 0

def test_decimal_with_multiple_trailing_zeros_not_ending_with_point_five_should_round():
    # Input is a decimal with multiple zeros after decimal, not ending with .5, should trim zeros and round
    result = closest_integer('4.0000')
    assert result == 4

def test_decimal_no_trailing_zeros_not_ending_with_point_five_should_round_normally():
    # Input is a decimal with no trailing zeros and not ending with .5, should round normally
    result = closest_integer('7.3')
    assert result == 7