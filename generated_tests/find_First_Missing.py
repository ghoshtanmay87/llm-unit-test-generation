def find_First_Missing(array,start,end): 
    if (start > end): 
        return end + 1
    if (start != array[start]): 
        return start; 
    mid = int((start + end) / 2) 
    if (array[mid] == mid): 
        return find_First_Missing(array,mid+1,end) 
    return find_First_Missing(array,start,mid)

import pytest

def test_find_first_missing_complete_sequence_starting_from_0():
    array = [0, 1, 2, 3, 4, 5]
    start = 0
    end = 5
    expected = 6
    assert find_First_Missing(array, start, end) == expected

def test_find_first_missing_when_0_is_missing():
    array = [1, 2, 3, 4, 5]
    start = 0
    end = 4
    expected = 0
    assert find_First_Missing(array, start, end) == expected

def test_find_first_missing_with_missing_number_in_middle():
    array = [0, 1, 2, 4, 5]
    start = 0
    end = 4
    expected = 3
    assert find_First_Missing(array, start, end) == expected

def test_find_first_missing_multiple_missing_first_is_2():
    array = [0, 1, 3, 4, 5]
    start = 0
    end = 4
    expected = 2
    assert find_First_Missing(array, start, end) == expected

def test_find_first_missing_in_empty_array():
    array = []
    start = 0
    end = -1
    expected = 0
    assert find_First_Missing(array, start, end) == expected

def test_find_first_missing_array_starts_from_1_instead_of_0():
    array = [1, 2, 3, 4, 5]
    start = 0
    end = 4
    expected = 0
    assert find_First_Missing(array, start, end) == expected

def test_find_first_missing_when_last_number_is_missing():
    array = [0, 1, 2, 3, 4]
    start = 0
    end = 4
    expected = 5
    assert find_First_Missing(array, start, end) == expected

def test_find_first_missing_large_array_missing_in_middle():
    array = [0, 1, 2, 3, 4, 5, 7, 8, 9]
    start = 0
    end = 8
    expected = 6
    assert find_First_Missing(array, start, end) == expected