def find_Element(arr,ranges,rotations,index) :  
    for i in range(rotations - 1,-1,-1 ) : 
        left = ranges[i][0] 
        right = ranges[i][1] 
        if (left <= index and right >= index) : 
            if (index == left) : 
                index = right 
            else : 
                index = index - 1 
    return arr[index]

import pytest

def test_no_rotations_direct_index_access():
    arr = [10, 20, 30, 40, 50]
    ranges = []
    rotations = 0
    index = 2
    expected = 30
    assert find_Element(arr, ranges, rotations, index) == expected

def test_single_rotation_index_inside_range_not_left_boundary():
    arr = [10, 20, 30, 40, 50]
    ranges = [[1, 3]]
    rotations = 1
    index = 2
    expected = 20
    assert find_Element(arr, ranges, rotations, index) == expected

def test_single_rotation_index_at_left_boundary():
    arr = [10, 20, 30, 40, 50]
    ranges = [[1, 3]]
    rotations = 1
    index = 1
    expected = 40
    assert find_Element(arr, ranges, rotations, index) == expected

def test_multiple_rotations_index_inside_multiple_ranges():
    arr = [10, 20, 30, 40, 50, 60]
    ranges = [[1, 4], [2, 5]]
    rotations = 2
    index = 3
    expected = 20
    assert find_Element(arr, ranges, rotations, index) == expected

def test_multiple_rotations_index_at_left_boundary_in_one_range():
    arr = [10, 20, 30, 40, 50, 60]
    ranges = [[1, 4], [2, 5]]
    rotations = 2
    index = 2
    expected = 60
    assert find_Element(arr, ranges, rotations, index) == expected

def test_index_outside_all_ranges():
    arr = [10, 20, 30, 40, 50]
    ranges = [[1, 3]]
    rotations = 1
    index = 4
    expected = 50
    assert find_Element(arr, ranges, rotations, index) == expected

def test_multiple_rotations_index_at_left_boundary_in_first_rotation_only():
    arr = [10, 20, 30, 40, 50, 60, 70]
    ranges = [[1, 3], [2, 5], [0, 6]]
    rotations = 3
    index = 1
    expected = 10
    assert find_Element(arr, ranges, rotations, index) == expected