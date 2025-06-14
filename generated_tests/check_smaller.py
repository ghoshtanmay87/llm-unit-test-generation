def check_smaller(test_tup1, test_tup2):
  res = all(x > y for x, y in zip(test_tup1, test_tup2))
  return (res)

import pytest

def test_all_elements_greater():
    test_tup1 = (5, 10, 15)
    test_tup2 = (1, 2, 3)
    expected_output = True
    assert check_smaller(test_tup1, test_tup2) == expected_output

def test_at_least_one_not_greater():
    test_tup1 = (5, 2, 15)
    test_tup2 = (1, 3, 3)
    expected_output = False
    assert check_smaller(test_tup1, test_tup2) == expected_output

def test_elements_equal():
    test_tup1 = (4, 4, 4)
    test_tup2 = (4, 4, 4)
    expected_output = False
    assert check_smaller(test_tup1, test_tup2) == expected_output

def test_all_elements_smaller():
    test_tup1 = (1, 2, 3)
    test_tup2 = (4, 5, 6)
    expected_output = False
    assert check_smaller(test_tup1, test_tup2) == expected_output

def test_different_lengths_compare_shortest():
    test_tup1 = (10, 20)
    test_tup2 = (5, 15, 25)
    expected_output = True
    assert check_smaller(test_tup1, test_tup2) == expected_output