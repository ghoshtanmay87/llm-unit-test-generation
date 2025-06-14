import bisect
def right_insertion(a, x):
    i = bisect.bisect_right(a, x)
    return i

import pytest

def test_insert_element_greater_than_all_elements():
    a = [1, 2, 3, 4, 5]
    x = 6
    expected_output = 5
    assert right_insertion(a, x) == expected_output

def test_insert_element_smaller_than_all_elements():
    a = [10, 20, 30, 40]
    x = 5
    expected_output = 0
    assert right_insertion(a, x) == expected_output

def test_insert_element_equal_to_existing_with_duplicates():
    a = [1, 2, 2, 2, 3]
    x = 2
    expected_output = 4
    assert right_insertion(a, x) == expected_output

def test_insert_element_equal_to_unique_element():
    a = [1, 3, 5, 7]
    x = 5
    expected_output = 3
    assert right_insertion(a, x) == expected_output

def test_insert_element_in_middle_no_duplicates():
    a = [10, 20, 30, 40, 50]
    x = 25
    expected_output = 2
    assert right_insertion(a, x) == expected_output