def check_monthnumb_number(monthnum2):
  if(monthnum2==1 or monthnum2==3 or monthnum2==5 or monthnum2==7 or monthnum2==8 or monthnum2==10 or monthnum2==12):
    return True
  else:
    return False

import pytest

def test_january_has_31_days():
    # Month number 1 is January, which has 31 days, so the function returns True.
    assert check_monthnumb_number(monthnum2=1) is True

def test_february_does_not_have_31_days():
    # Month number 2 is February, which does not have 31 days, so the function returns False.
    assert check_monthnumb_number(monthnum2=2) is False

def test_april_does_not_have_31_days():
    # Month number 4 is April, which has 30 days, so the function returns False.
    assert check_monthnumb_number(monthnum2=4) is False

def test_july_has_31_days():
    # Month number 7 is July, which has 31 days, so the function returns True.
    assert check_monthnumb_number(monthnum2=7) is True

def test_november_does_not_have_31_days():
    # Month number 11 is November, which has 30 days, so the function returns False.
    assert check_monthnumb_number(monthnum2=11) is False

def test_december_has_31_days():
    # Month number 12 is December, which has 31 days, so the function returns True.
    assert check_monthnumb_number(monthnum2=12) is True

def test_september_does_not_have_31_days():
    # Month number 9 is September, which has 30 days, so the function returns False.
    assert check_monthnumb_number(monthnum2=9) is False