def binary_search(item_list,item):
	first = 0
	last = len(item_list)-1
	found = False
	while( first<=last and not found):
		mid = (first + last)//2
		if item_list[mid] == item :
			found = True
		else:
			if item < item_list[mid]:
				last = mid - 1
			else:
				first = mid + 1	
	return found

import pytest

def test_search_item_in_middle_of_list():
    item_list = [1, 3, 5, 7, 9]
    item = 5
    expected_output = True
    assert binary_search(item_list, item) == expected_output

def test_search_item_at_beginning_of_list():
    item_list = [2, 4, 6, 8, 10]
    item = 2
    expected_output = True
    assert binary_search(item_list, item) == expected_output

def test_search_item_at_end_of_list():
    item_list = [10, 20, 30, 40, 50]
    item = 50
    expected_output = True
    assert binary_search(item_list, item) == expected_output

def test_search_item_not_present_in_list():
    item_list = [1, 2, 3, 4, 5]
    item = 6
    expected_output = False
    assert binary_search(item_list, item) == expected_output

def test_search_in_empty_list():
    item_list = []
    item = 1
    expected_output = False
    assert binary_search(item_list, item) == expected_output

def test_search_item_smaller_than_all_elements():
    item_list = [10, 20, 30, 40]
    item = 5
    expected_output = False
    assert binary_search(item_list, item) == expected_output

def test_search_item_in_single_element_list_present():
    item_list = [7]
    item = 7
    expected_output = True
    assert binary_search(item_list, item) == expected_output

def test_search_item_in_single_element_list_absent():
    item_list = [7]
    item = 8
    expected_output = False
    assert binary_search(item_list, item) == expected_output