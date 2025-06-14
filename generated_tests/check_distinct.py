def check_distinct(test_tup):
  res = True
  temp = set()
  for ele in test_tup:
    if ele in temp:
      res = False
      break
    temp.add(ele)
  return (res)

import pytest

def test_all_elements_unique():
    test_tup = (1, 2, 3, 4)
    expected_output = True
    assert check_distinct(test_tup) == expected_output

def test_tuple_contains_duplicate_elements():
    test_tup = (1, 2, 2, 3)
    expected_output = False
    assert check_distinct(test_tup) == expected_output

def test_empty_tuple_input():
    test_tup = ()
    expected_output = True
    assert check_distinct(test_tup) == expected_output

def test_tuple_with_one_element():
    test_tup = (5,)
    expected_output = True
    assert check_distinct(test_tup) == expected_output

def test_tuple_with_multiple_duplicates():
    test_tup = (7, 8, 7, 8)
    expected_output = False
    assert check_distinct(test_tup) == expected_output