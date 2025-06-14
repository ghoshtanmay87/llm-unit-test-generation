def check_monthnum_number(monthnum1):
  if monthnum1 == 2:
    return True
  else:
    return False

import pytest

def test_check_monthnum_number_with_2_returns_true():
    # Input is 2, the function should return True
    result = check_monthnum_number(monthnum1=2)
    assert result is True

def test_check_monthnum_number_with_1_returns_false():
    # Input is 1, the function should return False
    result = check_monthnum_number(monthnum1=1)
    assert result is False

def test_check_monthnum_number_with_12_returns_false():
    # Input is 12, the function should return False
    result = check_monthnum_number(monthnum1=12)
    assert result is False

def test_check_monthnum_number_with_0_returns_false():
    # Input is 0, the function should return False
    result = check_monthnum_number(monthnum1=0)
    assert result is False

def test_check_monthnum_number_with_negative_2_returns_false():
    # Input is -2, the function should return False
    result = check_monthnum_number(monthnum1=-2)
    assert result is False