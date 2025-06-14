def common_element(list1, list2):
     result = False
     for x in list1:
         for y in list2:
             if x == y:
                 result = True
                 return result

import pytest

def test_lists_with_one_common_element():
    list1 = [1, 2, 3]
    list2 = [3, 4, 5]
    expected = True
    assert common_element(list1, list2) == expected

def test_lists_with_no_common_elements():
    list1 = [1, 2, 3]
    list2 = [4, 5, 6]
    expected = False
    assert common_element(list1, list2) == expected

def test_empty_first_list():
    list1 = []
    list2 = [1, 2, 3]
    expected = False
    assert common_element(list1, list2) == expected

def test_empty_second_list():
    list1 = [1, 2, 3]
    list2 = []
    expected = False
    assert common_element(list1, list2) == expected

def test_both_lists_empty():
    list1 = []
    list2 = []
    expected = False
    assert common_element(list1, list2) == expected

def test_multiple_common_elements_returns_on_first_found():
    list1 = [1, 2, 3, 4]
    list2 = [4, 3, 2, 1]
    expected = True
    assert common_element(list1, list2) == expected

def test_common_element_is_last_element_in_list2():
    list1 = [7]
    list2 = [1, 2, 3, 4, 5, 6, 7]
    expected = True
    assert common_element(list1, list2) == expected