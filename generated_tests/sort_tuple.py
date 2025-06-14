def sort_tuple(tup): 
	lst = len(tup) 
	for i in range(0, lst): 
		for j in range(0, lst-i-1): 
			if (tup[j][-1] > tup[j + 1][-1]): 
				temp = tup[j] 
				tup[j]= tup[j + 1] 
				tup[j + 1]= temp 
	return tup

import pytest

def test_sort_tuple_by_last_element_ascending():
    # Sort a tuple of tuples by the last element in ascending order
    input_tup = ((3, 4), (1, 2), (5, 0))
    expected = ((5, 0), (1, 2), (3, 4))
    assert sort_tuple(input_tup) == expected

def test_sort_tuple_all_last_elements_equal():
    # Sort a tuple of tuples where all last elements are equal
    input_tup = ((1, 5), (2, 5), (3, 5))
    expected = ((1, 5), (2, 5), (3, 5))
    assert sort_tuple(input_tup) == expected

def test_sort_tuple_with_negative_and_positive_last_elements():
    # Sort a tuple of tuples with negative and positive last elements
    input_tup = ((10, -1), (4, 3), (7, 0))
    expected = ((10, -1), (7, 0), (4, 3))
    assert sort_tuple(input_tup) == expected

def test_sort_tuple_single_element_tuples():
    # Sort a tuple of single-element tuples
    input_tup = ((3,), (1,), (2,))
    expected = ((1,), (2,), (3,))
    assert sort_tuple(input_tup) == expected

def test_sort_tuple_empty_tuple():
    # Sort an empty tuple
    input_tup = ()
    expected = ()
    assert sort_tuple(input_tup) == expected