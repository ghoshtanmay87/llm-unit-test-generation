def is_subset(arr1, m, arr2, n): 
	hashset = set() 
	for i in range(0, m): 
		hashset.add(arr1[i]) 
	for i in range(0, n): 
		if arr2[i] in hashset: 
			continue
		else: 
			return False
	return True

import pytest

def test_all_elements_of_arr2_present_in_arr1():
    arr1 = [1, 2, 3, 4, 5]
    m = 5
    arr2 = [2, 3, 5]
    n = 3
    assert is_subset(arr1, m, arr2, n) is True

def test_arr2_contains_element_not_in_arr1():
    arr1 = [10, 20, 30]
    m = 3
    arr2 = [20, 40]
    n = 2
    assert is_subset(arr1, m, arr2, n) is False

def test_arr2_empty_arr1_non_empty():
    arr1 = [7, 8, 9]
    m = 3
    arr2 = []
    n = 0
    assert is_subset(arr1, m, arr2, n) is True

def test_both_arr1_and_arr2_empty():
    arr1 = []
    m = 0
    arr2 = []
    n = 0
    assert is_subset(arr1, m, arr2, n) is True

def test_arr2_has_duplicate_elements_all_present_in_arr1():
    arr1 = [1, 2, 3]
    m = 3
    arr2 = [2, 2, 3]
    n = 3
    assert is_subset(arr1, m, arr2, n) is True

def test_arr1_has_duplicates_arr2_subset_without_duplicates():
    arr1 = [4, 4, 5, 6]
    m = 4
    arr2 = [4, 6]
    n = 2
    assert is_subset(arr1, m, arr2, n) is True

def test_arr2_has_elements_not_in_arr1_arr1_has_duplicates():
    arr1 = [1, 1, 2, 3]
    m = 4
    arr2 = [1, 4]
    n = 2
    assert is_subset(arr1, m, arr2, n) is False