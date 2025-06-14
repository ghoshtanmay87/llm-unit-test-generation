def sum_of_alternates(test_tuple):
  sum1 = 0
  sum2 = 0
  for idx, ele in enumerate(test_tuple):
    if idx % 2:
      sum1 += ele
    else:
      sum2 += ele
  return ((sum1),(sum2))

import pytest

def test_sum_of_alternates_multiple_integers():
    # Sum of alternates for a tuple with multiple integers
    test_tuple = (1, 2, 3, 4, 5)
    expected_output = (6, 9)
    assert sum_of_alternates(test_tuple) == expected_output

def test_sum_of_alternates_single_element():
    # Sum of alternates for a tuple with a single element
    test_tuple = (10,)
    expected_output = (0, 10)
    assert sum_of_alternates(test_tuple) == expected_output

def test_sum_of_alternates_empty_tuple():
    # Sum of alternates for an empty tuple
    test_tuple = ()
    expected_output = (0, 0)
    assert sum_of_alternates(test_tuple) == expected_output

def test_sum_of_alternates_negative_and_positive():
    # Sum of alternates for a tuple with negative and positive numbers
    test_tuple = (-1, 2, -3, 4, -5, 6)
    expected_output = (12, -9)
    assert sum_of_alternates(test_tuple) == expected_output

def test_sum_of_alternates_all_zeros():
    # Sum of alternates for a tuple with all zeros
    test_tuple = (0, 0, 0, 0)
    expected_output = (0, 0)
    assert sum_of_alternates(test_tuple) == expected_output