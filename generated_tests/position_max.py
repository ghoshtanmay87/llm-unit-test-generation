def position_max(list1):
    max_val = max(list1)
    max_result = [i for i, j in enumerate(list1) if j == max_val]
    return max_result

import pytest

def test_single_maximum_value_at_beginning():
    # The maximum value is 10, which occurs only at index 0, so the function returns [0].
    input_list = [10, 2, 3, 4, 5]
    expected = [0]
    assert position_max(input_list) == expected

def test_multiple_maximum_values_scattered():
    # The maximum value is 5, which appears at indices 1 and 3, so the function returns [1, 3].
    input_list = [1, 5, 3, 5, 2]
    expected = [1, 3]
    assert position_max(input_list) == expected

def test_all_elements_are_the_same():
    # All elements are equal to the maximum value 7, so all indices are returned.
    input_list = [7, 7, 7, 7]
    expected = [0, 1, 2, 3]
    assert position_max(input_list) == expected

def test_maximum_value_at_end():
    # The maximum value is 9, which occurs only at index 4, so the function returns [4].
    input_list = [1, 2, 3, 4, 9]
    expected = [4]
    assert position_max(input_list) == expected

def test_maximum_value_in_middle():
    # The maximum value is 10, which occurs only at index 2, so the function returns [2].
    input_list = [1, 3, 10, 3, 1]
    expected = [2]
    assert position_max(input_list) == expected