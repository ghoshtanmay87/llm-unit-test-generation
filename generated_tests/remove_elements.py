def remove_elements(list1, list2):
    result = [x for x in list1 if x not in list2]
    return result

import pytest

def test_remove_elements_with_some_common_elements():
    list1 = [1, 2, 3, 4, 5]
    list2 = [2, 4]
    expected = [1, 3, 5]
    assert remove_elements(list1, list2) == expected

def test_remove_elements_when_list2_is_empty():
    list1 = [1, 2, 3]
    list2 = []
    expected = [1, 2, 3]
    assert remove_elements(list1, list2) == expected

def test_remove_elements_when_list1_is_empty():
    list1 = []
    list2 = [1, 2, 3]
    expected = []
    assert remove_elements(list1, list2) == expected

def test_remove_elements_when_no_common_elements():
    list1 = [1, 2, 3]
    list2 = [4, 5, 6]
    expected = [1, 2, 3]
    assert remove_elements(list1, list2) == expected

def test_remove_elements_when_all_elements_removed():
    list1 = [1, 2, 3]
    list2 = [1, 2, 3]
    expected = []
    assert remove_elements(list1, list2) == expected

def test_remove_elements_with_duplicates_in_list1():
    list1 = [1, 2, 2, 3, 4, 4, 5]
    list2 = [2, 4]
    expected = [1, 3, 5]
    assert remove_elements(list1, list2) == expected

def test_remove_elements_with_duplicates_in_list2():
    list1 = [1, 2, 3, 4, 5]
    list2 = [2, 2, 4, 4]
    expected = [1, 3, 5]
    assert remove_elements(list1, list2) == expected