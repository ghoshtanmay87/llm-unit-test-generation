def max_difference(test_list):
  temp = [abs(b - a) for a, b in test_list]
  res = max(temp)
  return (res)

import pytest

def test_max_difference_positive_and_negative_values():
    test_list = [[1, 5], [3, 8], [10, 2]]
    expected_output = 8
    assert max_difference(test_list) == expected_output

def test_max_difference_all_zero_difference():
    test_list = [[4, 4], [7, 7], [0, 0]]
    expected_output = 0
    assert max_difference(test_list) == expected_output

def test_max_difference_negative_and_positive_numbers_corrected():
    test_list = [[-1, 1], [-5, -10], [3, -3]]
    expected_output = 6
    assert max_difference(test_list) == expected_output

def test_max_difference_single_pair():
    test_list = [[100, 50]]
    expected_output = 50
    assert max_difference(test_list) == expected_output

def test_max_difference_empty_list():
    test_list = []
    expected_output = None
    # The function as given will raise an error on empty list.
    # So we test that it raises an exception and return None in that case.
    with pytest.raises(ValueError):
        max_difference(test_list)