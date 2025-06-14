def move_last(num_list):
    a = [num_list[0] for i in range(num_list.count(num_list[0]))]
    x = [ i for i in num_list if i != num_list[0]]
    x.extend(a)
    return (x)

import pytest

def test_all_elements_same():
    # All elements are the same in the list
    input_list = [5, 5, 5, 5]
    expected = [5, 5, 5, 5]
    assert move_last(input_list) == expected

def test_first_element_multiple_times_mixed():
    # First element appears multiple times, mixed with other elements
    input_list = [2, 3, 2, 4, 2]
    expected = [3, 4, 2, 2, 2]
    assert move_last(input_list) == expected

def test_first_element_appears_once():
    # First element appears only once
    input_list = [7, 1, 2, 3]
    expected = [1, 2, 3, 7]
    assert move_last(input_list) == expected

def test_first_element_appears_twice_with_others():
    # First element appears twice, with other elements
    input_list = [4, 5, 4, 6, 7]
    expected = [5, 6, 7, 4, 4]
    assert move_last(input_list) == expected

def test_single_element_list():
    # List with only one element
    input_list = [9]
    expected = [9]
    assert move_last(input_list) == expected