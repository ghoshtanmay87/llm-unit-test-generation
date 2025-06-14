def truncate_number(number: float) -> float:
    return number % 1.0

import pytest

def test_truncating_positive_integer():
    # Truncating a positive integer
    result = truncate_number(7.0)
    assert result == 0.0

def test_truncating_positive_float_less_than_one():
    # Truncating a positive float less than 1
    result = truncate_number(0.75)
    assert result == 0.75

def test_truncating_zero():
    # Truncating zero
    result = truncate_number(0.0)
    assert result == 0.0

def test_truncating_negative_integer():
    # Truncating a negative integer
    result = truncate_number(-5.0)
    assert result == 0.0

def test_truncating_negative_float_less_than_minus_one_with_fractional_part():
    # Truncating a negative float less than -1 with fractional part
    result = truncate_number(-10.75)
    assert result == 0.25

def test_truncating_positive_float_with_fractional_part():
    # Truncating a positive float with fractional part
    result = truncate_number(3.1415)
    assert result == 0.14150000000000018

def test_truncating_negative_float_with_fractional_part():
    # Truncating a negative float with fractional part
    result = truncate_number(-2.3)
    assert result == 0.7000000000000002