def check_monthnum(monthname1):
  if monthname1 == "February":
    return True
  else:
    return False

import pytest

def test_check_monthnum_february_returns_true():
    # Input is 'February', the only month that should return True
    result = check_monthnum(monthname1='February')
    assert result is True

def test_check_monthnum_january_returns_false():
    # Input is 'January', a month other than February
    result = check_monthnum(monthname1='January')
    assert result is False

def test_check_monthnum_march_returns_false():
    # Input is 'March', another month different from February
    result = check_monthnum(monthname1='March')
    assert result is False

def test_check_monthnum_empty_string_returns_false():
    # Input is an empty string, which is not 'February'
    result = check_monthnum(monthname1='')
    assert result is False

def test_check_monthnum_lowercase_february_returns_false():
    # Input is 'february' in lowercase, testing case sensitivity
    result = check_monthnum(monthname1='february')
    assert result is False