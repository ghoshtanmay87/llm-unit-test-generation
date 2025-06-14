def check_monthnumber_number(monthnum3):
  if(monthnum3==4 or monthnum3==6 or monthnum3==9 or monthnum3==11):
    return True
  else:
    return False

import pytest

def test_month_4_has_30_days():
    assert check_monthnumber_number(monthnum3=4) is True

def test_month_6_has_30_days():
    assert check_monthnumber_number(monthnum3=6) is True

def test_month_9_has_30_days():
    assert check_monthnumber_number(monthnum3=9) is True

def test_month_11_has_30_days():
    assert check_monthnumber_number(monthnum3=11) is True

def test_month_1_does_not_have_30_days():
    assert check_monthnumber_number(monthnum3=1) is False

def test_month_2_does_not_have_30_days():
    assert check_monthnumber_number(monthnum3=2) is False

def test_month_12_does_not_have_30_days():
    assert check_monthnumber_number(monthnum3=12) is False