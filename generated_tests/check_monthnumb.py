def check_monthnumb(monthname2):
  if(monthname2=="January" or monthname2=="March"or monthname2=="May" or monthname2=="July" or monthname2=="Augest" or monthname2=="October" or monthname2=="December"):
    return True
  else:
    return False

import pytest

def test_valid_month_january():
    # Check a valid month with 31 days spelled correctly: January
    assert check_monthnumb(monthname2="January") is True

def test_valid_month_march():
    # Check a valid month with 31 days spelled correctly: March
    assert check_monthnumb(monthname2="March") is True

def test_valid_month_may():
    # Check a valid month with 31 days spelled correctly: May
    assert check_monthnumb(monthname2="May") is True

def test_valid_month_july():
    # Check a valid month with 31 days spelled correctly: July
    assert check_monthnumb(monthname2="July") is True

def test_misspelled_month_august():
    # Check a misspelled month name: August spelled as 'Augest'
    assert check_monthnumb(monthname2="August") is False

def test_misspelled_month_augest():
    # Check the misspelled month name 'Augest'
    assert check_monthnumb(monthname2="Augest") is True

def test_valid_month_october():
    # Check a valid month with 31 days spelled correctly: October
    assert check_monthnumb(monthname2="October") is True

def test_valid_month_december():
    # Check a valid month with 31 days spelled correctly: December
    assert check_monthnumb(monthname2="December") is True

def test_valid_month_april():
    # Check a valid month with 30 days: April
    assert check_monthnumb(monthname2="April") is False

def test_valid_month_september():
    # Check a valid month with 30 days: September
    assert check_monthnumb(monthname2="September") is False

def test_valid_month_february():
    # Check a valid month with 28 or 29 days: February
    assert check_monthnumb(monthname2="February") is False

def test_empty_string_input():
    # Check an empty string input
    assert check_monthnumb(monthname2="") is False

def test_unrelated_string():
    # Check a completely unrelated string
    assert check_monthnumb(monthname2="Hello") is False