def increment_numerics(test_list, K):
  res = [str(int(ele) + K) if ele.isdigit() else ele for ele in test_list]
  return res

import pytest

def test_increment_all_numeric_strings_by_K():
    # Each element is a digit string, so each is converted to int, incremented by 5, then converted back to string.
    test_list = ['1', '2', '3']
    K = 5
    expected_output = ['6', '7', '8']
    assert increment_numerics(test_list, K) == expected_output

def test_list_with_mixed_digit_and_non_digit_strings():
    # '10' and '5' are digit strings and incremented by 3; 'abc' is non-digit and remains unchanged.
    test_list = ['10', 'abc', '5']
    K = 3
    expected_output = ['13', 'abc', '8']
    assert increment_numerics(test_list, K) == expected_output

def test_list_with_no_digit_strings():
    # No elements are digit strings, so none are incremented; all remain unchanged.
    test_list = ['hello', 'world']
    K = 10
    expected_output = ['hello', 'world']
    assert increment_numerics(test_list, K) == expected_output

def test_empty_list_input():
    # Empty list returns empty list regardless of K.
    test_list = []
    K = 100
    expected_output = []
    assert increment_numerics(test_list, K) == expected_output

def test_digit_strings_with_leading_zeros():
    # '007' and '000' are digit strings; converted to int 7 and 0, incremented by 1, then converted back to strings '8' and '1' (leading zeros removed).
    test_list = ['007', '000']
    K = 1
    expected_output = ['8', '1']
    assert increment_numerics(test_list, K) == expected_output

def test_digit_strings_with_negative_sign_non_digit_strings():
    # '-1' is not digit (due to '-'), so unchanged; '2' is digit string incremented by 4 to '6'.
    test_list = ['-1', '2']
    K = 4
    expected_output = ['-1', '6']
    assert increment_numerics(test_list, K) == expected_output