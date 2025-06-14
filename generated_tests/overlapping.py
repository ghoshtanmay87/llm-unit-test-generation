def overlapping(list1,list2):  
    c=0
    d=0
    for i in list1: 
        c+=1
    for i in list2: 
        d+=1
    for i in range(0,c): 
        for j in range(0,d): 
            if(list1[i]==list2[j]): 
                return 1
    return 0

import pytest

def test_no_common_elements_between_two_non_empty_lists():
    list1 = [1, 2, 3]
    list2 = [4, 5, 6]
    expected = 0
    assert overlapping(list1, list2) == expected

def test_one_common_element_between_two_lists():
    list1 = [1, 2, 3]
    list2 = [3, 4, 5]
    expected = 1
    assert overlapping(list1, list2) == expected

def test_both_lists_empty():
    list1 = []
    list2 = []
    expected = 0
    assert overlapping(list1, list2) == expected

def test_first_list_empty_second_non_empty():
    list1 = []
    list2 = [1, 2, 3]
    expected = 0
    assert overlapping(list1, list2) == expected

def test_second_list_empty_first_non_empty():
    list1 = [1, 2, 3]
    list2 = []
    expected = 0
    assert overlapping(list1, list2) == expected

def test_multiple_common_elements_returns_on_first_found():
    list1 = [7, 8, 9]
    list2 = [9, 7, 10]
    expected = 1
    assert overlapping(list1, list2) == expected

def test_lists_with_duplicate_elements_common_element_present():
    list1 = [1, 1, 2]
    list2 = [2, 2, 3]
    expected = 1
    assert overlapping(list1, list2) == expected

def test_lists_with_duplicate_elements_no_common_element():
    list1 = [1, 1, 2]
    list2 = [3, 3, 4]
    expected = 0
    assert overlapping(list1, list2) == expected