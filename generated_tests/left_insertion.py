import bisect
def left_insertion(a, x):
    i = bisect.bisect_left(a, x)
    return i

import pytest

def test_insert_element_smaller_than_all_elements():
    a = [10, 20, 30, 40]
    x = 5
    expected = 0
    assert left_insertion(a, x) == expected

def test_insert_element_equal_to_existing_element():
    a = [10, 20, 30, 40]
    x = 20
    expected = 1
    assert left_insertion(a, x) == expected

def test_insert_element_between_two_elements():
    a = [10, 20, 30, 40]
    x = 25
    expected = 2
    assert left_insertion(a, x) == expected

def test_insert_element_greater_than_all_elements():
    a = [10, 20, 30, 40]
    x = 50
    expected = 4
    assert left_insertion(a, x) == expected

def test_insert_element_into_empty_list():
    a = []
    x = 10
    expected = 0
    assert left_insertion(a, x) == expected

def test_insert_element_equal_to_multiple_identical_elements():
    a = [10, 20, 20, 20, 30]
    x = 20
    expected = 1
    assert left_insertion(a, x) == expected

def test_insert_element_smaller_than_all_elements_with_duplicates():
    a = [10, 10, 20, 20, 30]
    x = 5
    expected = 0
    assert left_insertion(a, x) == expected

def test_insert_element_greater_than_all_elements_with_duplicates():
    a = [10, 10, 20, 20, 30]
    x = 40
    expected = 5
    assert left_insertion(a, x) == expected