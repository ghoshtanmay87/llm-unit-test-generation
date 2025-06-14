def count_Rotation(arr,n):   
    for i in range (1,n): 
        if (arr[i] < arr[i - 1]): 
            return i  
    return 0

import pytest

def test_no_rotation_array_sorted_ascending():
    arr = [1, 2, 3, 4, 5]
    n = 5
    expected = 0
    assert count_Rotation(arr, n) == expected

def test_rotation_once_smallest_at_index_1():
    arr = [5, 1, 2, 3, 4]
    n = 5
    expected = 1
    assert count_Rotation(arr, n) == expected

def test_rotation_three_times_smallest_at_index_3():
    arr = [3, 4, 5, 1, 2]
    n = 5
    expected = 3
    assert count_Rotation(arr, n) == expected

def test_rotation_four_times_smallest_at_index_4():
    arr = [2, 3, 4, 5, 1]
    n = 5
    expected = 4
    assert count_Rotation(arr, n) == expected

def test_all_elements_equal_no_rotation():
    arr = [7, 7, 7, 7, 7]
    n = 5
    expected = 0
    assert count_Rotation(arr, n) == expected

def test_rotation_twice_smallest_at_index_2():
    arr = [4, 5, 1, 2, 3]
    n = 5
    expected = 2
    assert count_Rotation(arr, n) == expected

def test_single_element_array_no_rotation():
    arr = [10]
    n = 1
    expected = 0
    assert count_Rotation(arr, n) == expected