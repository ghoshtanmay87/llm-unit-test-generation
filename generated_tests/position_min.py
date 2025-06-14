def position_min(list1):
    min_val = min(list1)
    min_result = [i for i, j in enumerate(list1) if j == min_val]
    return min_result

import pytest

def test_position_min_distinct_min_at_start():
    # List with distinct elements, minimum at the start
    input_list = [3, 5, 7, 9]
    expected = [0]
    assert position_min(input_list) == expected

def test_position_min_distinct_min_at_end():
    # List with distinct elements, minimum at the end
    input_list = [10, 20, 5]
    expected = [2]
    assert position_min(input_list) == expected

def test_position_min_multiple_min_occurrences():
    # List with multiple occurrences of the minimum value
    input_list = [4, 2, 2, 3]
    expected = [1, 2]
    assert position_min(input_list) == expected

def test_position_min_all_elements_equal():
    # List with all elements equal
    input_list = [7, 7, 7, 7]
    expected = [0, 1, 2, 3]
    assert position_min(input_list) == expected

def test_position_min_negative_and_positive_numbers():
    # List with negative and positive numbers
    input_list = [0, -1, 5, -1, 3]
    expected = [1, 3]
    assert position_min(input_list) == expected

def test_position_min_single_element():
    # List with a single element
    input_list = [42]
    expected = [0]
    assert position_min(input_list) == expected