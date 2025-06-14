def next_smallest(lst):
    lst = sorted(set(lst))
    return None if len(lst) < 2 else lst[1]

import pytest

def test_next_smallest_multiple_distinct_elements():
    # List with multiple distinct elements
    result = next_smallest([4, 1, 3, 2])
    assert result == 2

def test_next_smallest_all_duplicates():
    # List with duplicates
    result = next_smallest([5, 5, 5, 5])
    assert result is None

def test_next_smallest_two_distinct_elements():
    # List with two distinct elements
    result = next_smallest([10, 20])
    assert result == 20

def test_next_smallest_single_element():
    # List with one element
    result = next_smallest([42])
    assert result is None

def test_next_smallest_empty_list():
    # Empty list
    result = next_smallest([])
    assert result is None

def test_next_smallest_negative_and_positive_numbers():
    # List with negative and positive numbers
    result = next_smallest([-1, -3, 0, 2, -3])
    assert result == -1