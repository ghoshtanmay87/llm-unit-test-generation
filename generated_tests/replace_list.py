def replace_list(list1,list2):
 list1[-1:] = list2
 replace_list=list1
 return replace_list

import pytest

def test_replace_last_element_with_multiple_elements():
    # Replace last element of list1 with list2 when list2 has multiple elements
    list1 = [1, 2, 3]
    list2 = [4, 5]
    expected = [1, 2, 4, 5]
    assert replace_list(list1, list2) == expected

def test_replace_last_element_with_single_element():
    # Replace last element of list1 with list2 when list2 has a single element
    list1 = [10, 20, 30]
    list2 = [99]
    expected = [10, 20, 99]
    assert replace_list(list1, list2) == expected

def test_replace_last_element_with_empty_list():
    # Replace last element of list1 with an empty list2
    list1 = [7, 8, 9]
    list2 = []
    expected = [7, 8]
    assert replace_list(list1, list2) == expected

def test_replace_last_element_of_single_element_list():
    # Replace last element of a single-element list1 with list2 having multiple elements
    list1 = [100]
    list2 = [1, 2, 3]
    expected = [1, 2, 3]
    assert replace_list(list1, list2) == expected

def test_replace_last_element_with_identical_element():
    # Replace last element of list1 with list2 having one element identical to last element
    list1 = [5, 6, 7]
    list2 = [7]
    expected = [5, 6, 7]
    assert replace_list(list1, list2) == expected