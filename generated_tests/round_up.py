import math
def round_up(a, digits):
    n = 10**-digits
    return round(math.ceil(a / n) * n, digits)

import pytest

def test_round_up_positive_2_decimal_places():
    # Rounding up a positive number with 2 decimal places
    result = round_up(1.234, 2)
    assert result == 1.24

def test_round_up_positive_0_decimal_places():
    # Rounding up a positive number with 0 decimal places
    result = round_up(1.2, 0)
    assert result == 2.0

def test_round_up_negative_1_decimal_place():
    # Rounding up a negative number with 1 decimal place
    result = round_up(-1.25, 1)
    assert result == -1.2

def test_round_up_positive_negative_1_digits():
    # Rounding up a positive number with -1 digits (rounding to tens)
    result = round_up(123, -1)
    assert result == 130.0

def test_round_up_zero_3_decimal_places():
    # Rounding up zero with 3 decimal places
    result = round_up(0, 3)
    assert result == 0.0

def test_round_up_positive_on_boundary():
    # Rounding up a positive number exactly on rounding boundary
    result = round_up(2.5, 0)
    assert result == 3.0

def test_round_up_negative_on_boundary():
    # Rounding up a negative number exactly on rounding boundary
    result = round_up(-2.0, 0)
    assert result == -2.0