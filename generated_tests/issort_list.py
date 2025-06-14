def issort_list(list1):
    result = all(list1[i] <= list1[i+1] for i in range(len(list1)-1))
    return result

import pytest

def test_empty_list_is_sorted():
    # An empty list has no elements to compare, so it is trivially sorted.
    input_list = []
    expected = True
    assert issort_list(input_list) == expected

def test_single_element_list_is_sorted():
    # A single-element list has no adjacent pairs to compare, so it is trivially sorted.
    input_list = [5]
    expected = True
    assert issort_list(input_list) == expected

def test_strictly_increasing_list_is_sorted():
    # Each element is less than or equal to the next, so the list is sorted in non-decreasing order.
    input_list = [1, 2, 3, 4, 5]
    expected = True
    assert issort_list(input_list) == expected

def test_non_decreasing_list_with_repeats_is_sorted():
    # All adjacent pairs satisfy list1[i] <= list1[i+1], including repeated elements, so the list is sorted.
    input_list = [1, 2, 2, 3, 4]
    expected = True
    assert issort_list(input_list) == expected

def test_list_with_decreasing_pair_is_not_sorted():
    # The pair (3, 2) violates the non-decreasing order condition, so the list is not sorted.
    input_list = [1, 3, 2, 4, 5]
    expected = False
    assert issort_list(input_list) == expected

def test_strictly_decreasing_list_is_not_sorted():
    # Each adjacent pair violates the condition list1[i] <= list1[i+1], so the list is not sorted.
    input_list = [5, 4, 3, 2, 1]
    expected = False
    assert issort_list(input_list) == expected

def test_list_with_all_equal_elements_is_sorted():
    # All adjacent elements are equal, satisfying list1[i] <= list1[i+1], so the list is sorted.
    input_list = [7, 7, 7, 7]
    expected = True
    assert issort_list(input_list) == expected