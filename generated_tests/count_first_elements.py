def count_first_elements(test_tup):
  for count, ele in enumerate(test_tup):
    if isinstance(ele, tuple):
      break
  return (count)

import pytest

def test_all_elements_not_tuples():
    # All elements are not tuples, so loop completes without break
    test_tup = [1, 2, 3, 4]
    expected_output = 4
    assert count_first_elements(test_tup) == expected_output

def test_first_element_is_tuple():
    # First element is a tuple
    test_tup = [(1, 2), 3, 4]
    expected_output = 0
    assert count_first_elements(test_tup) == expected_output

def test_tuple_found_at_second_element():
    # Tuple found at second element
    test_tup = [5, (1, 2), 3]
    expected_output = 1
    assert count_first_elements(test_tup) == expected_output

def test_tuple_found_at_last_element():
    # Tuple found at last element
    test_tup = [5, 6, 7, (8, 9)]
    expected_output = 3
    assert count_first_elements(test_tup) == expected_output

def test_empty_input_list():
    # Empty input list
    test_tup = []
    expected_output = 0
    assert count_first_elements(test_tup) == expected_output

def test_nested_tuples_but_first_element_not_tuple():
    # Input contains nested tuples but first element is not a tuple
    test_tup = [1, [2, 3], (4, 5)]
    expected_output = 2
    assert count_first_elements(test_tup) == expected_output