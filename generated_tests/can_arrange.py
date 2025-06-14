def can_arrange(arr):
    ind = -1
    i = 1
    while i < len(arr):
        if arr[i] < arr[i - 1]:
            ind = i
        i += 1
    return ind

import pytest

def test_array_strictly_increasing():
    # Array is strictly increasing
    arr = [1, 2, 3, 4, 5]
    expected = -1
    assert can_arrange(arr) == expected

def test_array_one_decreasing_point_in_middle():
    # Array has one decreasing point in the middle
    arr = [1, 3, 2, 4, 5]
    expected = 2
    assert can_arrange(arr) == expected

def test_array_multiple_decreasing_points():
    # Array has multiple decreasing points
    arr = [5, 4, 3, 2, 1]
    expected = 4
    assert can_arrange(arr) == expected

def test_array_single_element():
    # Array with a single element
    arr = [10]
    expected = -1
    assert can_arrange(arr) == expected

def test_array_equal_consecutive_elements():
    # Array with equal consecutive elements
    arr = [2, 2, 2, 2]
    expected = -1
    assert can_arrange(arr) == expected

def test_array_decreasing_point_at_end():
    # Array with decreasing point at the end
    arr = [1, 2, 3, 5, 4]
    expected = 4
    assert can_arrange(arr) == expected

def test_array_multiple_decreasing_points_last_not_at_end():
    # Array with multiple decreasing points, last one not at the end
    arr = [1, 3, 2, 4, 3]
    expected = 4
    assert can_arrange(arr) == expected