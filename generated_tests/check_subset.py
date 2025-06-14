def check_subset(list1,list2): 
    return all(map(list1.__contains__,list2))

import pytest

def test_all_elements_of_list2_present_in_list1():
    list1 = [1, 2, 3, 4, 5]
    list2 = [2, 3]
    expected = True
    assert check_subset(list1, list2) == expected

def test_some_elements_of_list2_not_present_in_list1():
    list1 = [1, 2, 3]
    list2 = [2, 4]
    expected = False
    assert check_subset(list1, list2) == expected

def test_list2_is_empty():
    list1 = [1, 2, 3]
    list2 = []
    expected = True
    assert check_subset(list1, list2) == expected

def test_list1_is_empty_but_list2_is_not():
    list1 = []
    list2 = [1]
    expected = False
    assert check_subset(list1, list2) == expected

def test_both_list1_and_list2_are_empty():
    list1 = []
    list2 = []
    expected = True
    assert check_subset(list1, list2) == expected

def test_list2_has_duplicate_elements_all_present_in_list1():
    list1 = [1, 2, 3]
    list2 = [2, 2]
    expected = True
    assert check_subset(list1, list2) == expected

def test_list2_has_elements_not_in_list1_with_duplicates():
    list1 = [1, 2, 3]
    list2 = [2, 4, 4]
    expected = False
    assert check_subset(list1, list2) == expected