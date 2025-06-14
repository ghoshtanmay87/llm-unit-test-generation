def move_one_ball(arr):
    if len(arr) == 0:
        return True
    sorted_array = sorted(arr)
    my_arr = []
    min_value = min(arr)
    min_index = arr.index(min_value)
    my_arr = arr[min_index:] + arr[0:min_index]
    for i in range(len(arr)):
        if my_arr[i] != sorted_array[i]:
            return False
    return True

import pytest

def test_empty_array_returns_true():
    arr = []
    expected = True
    assert move_one_ball(arr) == expected

def test_array_already_sorted_returns_true():
    arr = [1, 2, 3, 4]
    expected = True
    assert move_one_ball(arr) == expected

def test_array_is_rotation_of_sorted_array_returns_true():
    arr = [3, 4, 1, 2]
    expected = True
    assert move_one_ball(arr) == expected

def test_array_not_rotation_of_sorted_array_returns_false():
    arr = [2, 1, 3, 4]
    expected = False
    assert move_one_ball(arr) == expected

def test_array_with_all_equal_elements_returns_true():
    arr = [5, 5, 5, 5]
    expected = True
    assert move_one_ball(arr) == expected

def test_array_with_one_element_returns_true():
    arr = [10]
    expected = True
    assert move_one_ball(arr) == expected

def test_array_with_minimum_value_at_end_returns_true():
    arr = [2, 3, 4, 1]
    expected = True
    assert move_one_ball(arr) == expected

def test_array_with_minimum_in_middle_but_not_rotation_returns_false():
    arr = [3, 1, 4, 2]
    expected = False
    assert move_one_ball(arr) == expected