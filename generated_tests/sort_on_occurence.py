def sort_on_occurence(lst): 
	dct = {} 
	for i, j in lst: 
		dct.setdefault(i, []).append(j) 
	return ([(i, *dict.fromkeys(j), len(j)) 
				for i, j in dct.items()])

import pytest

def test_sort_on_occurence_multiple_pairs_repeated_first_and_second_elements():
    lst = [(1, 2), (1, 3), (1, 2), (2, 4), (2, 4), (3, 5)]
    expected_output = [(1, 2, 3, 2, 3), (2, 4, 2), (3, 5, 1)]
    assert sort_on_occurence(lst) == expected_output

def test_sort_on_occurence_unique_first_and_second_elements():
    lst = [(10, 100), (20, 200), (30, 300)]
    expected_output = [(10, 100, 1), (20, 200, 1), (30, 300, 1)]
    assert sort_on_occurence(lst) == expected_output

def test_sort_on_occurence_repeated_first_elements_identical_second_elements():
    lst = [(5, 7), (5, 7), (5, 7)]
    expected_output = [(5, 7, 3)]
    assert sort_on_occurence(lst) == expected_output

def test_sort_on_occurence_empty_list():
    lst = []
    expected_output = []
    assert sort_on_occurence(lst) == expected_output

def test_sort_on_occurence_multiple_first_elements_mixed_repeated_second_elements():
    lst = [(1, 1), (1, 2), (1, 1), (2, 3), (2, 3), (2, 4), (3, 5), (3, 5), (3, 5)]
    expected_output = [(1, 1, 2, 3), (2, 3, 4, 3), (3, 5, 3)]
    assert sort_on_occurence(lst) == expected_output