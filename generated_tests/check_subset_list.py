def check_subset_list(list1, list2): 
    l1, l2 = list1[0], list2[0] 
    exist = True
    for i in list2: 
        if i not in list1: 
            exist = False
    return exist

import pytest

def test_all_elements_of_list2_present_in_list1():
    list1 = [1, 2, 3, 4]
    list2 = [2, 3]
    expected = True
    assert check_subset_list(list1, list2) == expected

def test_some_elements_of_list2_not_present_in_list1():
    list1 = [1, 2, 3]
    list2 = [2, 4]
    expected = False
    assert check_subset_list(list1, list2) == expected

def test_list2_is_empty():
    list1 = [1, 2, 3]
    list2 = []
    expected = True
    assert check_subset_list(list1, list2) == expected

def test_list1_empty_but_list2_not():
    list1 = []
    list2 = [1]
    expected = False
    assert check_subset_list(list1, list2) == expected

def test_list1_and_list2_identical():
    list1 = [5, 6, 7]
    list2 = [5, 6, 7]
    expected = True
    assert check_subset_list(list1, list2) == expected

def test_list2_has_duplicate_elements_all_present_in_list1():
    list1 = [1, 2, 3]
    list2 = [2, 2]
    expected = True
    assert check_subset_list(list1, list2) == expected

def test_list2_has_duplicate_elements_with_one_missing_in_list1():
    list1 = [1, 2, 3]
    list2 = [2, 4, 4]
    expected = False
    assert check_subset_list(list1, list2) == expected