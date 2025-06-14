from itertools import combinations
def sub_lists(my_list):
	subs = []
	for i in range(0, len(my_list)+1):
	  temp = [list(x) for x in combinations(my_list, i)]
	  if len(temp)>0:
	    subs.extend(temp)
	return subs

import pytest

def test_empty_list_returns_only_empty_sublist():
    input_data = []
    expected = [[]]
    assert sub_lists(input_data) == expected

def test_single_element_list_returns_empty_and_single_element():
    input_data = [5]
    expected = [[], [5]]
    assert sub_lists(input_data) == expected

def test_two_element_list_returns_all_subsets():
    input_data = [1, 2]
    expected = [[], [1], [2], [1, 2]]
    assert sub_lists(input_data) == expected

def test_three_element_list_returns_all_subsets():
    input_data = [1, 2, 3]
    expected = [[], [1], [2], [3], [1, 2], [1, 3], [2, 3], [1, 2, 3]]
    assert sub_lists(input_data) == expected

def test_list_with_duplicates_returns_subsets_including_duplicates():
    input_data = [1, 1]
    expected = [[], [1], [1], [1, 1]]
    assert sub_lists(input_data) == expected