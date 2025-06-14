def check_monthnumber(monthname3):
  if monthname3 =="April" or monthname3== "June" or monthname3== "September" or monthname3== "November":
    return True
  else:
    return False

import pytest

def test_check_monthnumber_april_30_day():
    assert check_monthnumber(monthname3="April") is True

def test_check_monthnumber_june_30_day():
    assert check_monthnumber(monthname3="June") is True

def test_check_monthnumber_september_30_day():
    assert check_monthnumber(monthname3="September") is True

def test_check_monthnumber_november_30_day():
    assert check_monthnumber(monthname3="November") is True

def test_check_monthnumber_january_not_30_day():
    assert check_monthnumber(monthname3="January") is False

def test_check_monthnumber_february_not_30_day():
    assert check_monthnumber(monthname3="February") is False

def test_check_monthnumber_december_not_30_day():
    assert check_monthnumber(monthname3="December") is False

def test_check_monthnumber_april_lowercase_case_sensitive():
    assert check_monthnumber(monthname3="april") is False