def check_tuplex(tuplex,tuple1): 
  if tuple1 in tuplex:
    return True
  else:
     return False

import pytest

def test_check_tuplex_tuple1_present():
    tuplex = [(1, 2), (3, 4), (5, 6)]
    tuple1 = (3, 4)
    expected_output = True
    assert check_tuplex(tuplex, tuple1) == expected_output

def test_check_tuplex_tuple1_not_present():
    tuplex = [(1, 2), (3, 4), (5, 6)]
    tuple1 = (7, 8)
    expected_output = False
    assert check_tuplex(tuplex, tuple1) == expected_output

def test_check_tuplex_empty_tuplex():
    tuplex = []
    tuple1 = (1, 2)
    expected_output = False
    assert check_tuplex(tuplex, tuple1) == expected_output

def test_check_tuplex_empty_tuple1_present():
    tuplex = [(), (1,)]
    tuple1 = ()
    expected_output = True
    assert check_tuplex(tuplex, tuple1) == expected_output

def test_check_tuplex_empty_tuple1_not_present():
    tuplex = [(1,), (2, 3)]
    tuple1 = ()
    expected_output = False
    assert check_tuplex(tuplex, tuple1) == expected_output