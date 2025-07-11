from sys import maxsize 
def max_sub_array_sum(a,size): 
	max_so_far = -maxsize - 1
	max_ending_here = 0
	start = 0
	end = 0
	s = 0
	for i in range(0,size): 
		max_ending_here += a[i] 
		if max_so_far < max_ending_here: 
			max_so_far = max_ending_here 
			start = s 
			end = i 
		if max_ending_here < 0: 
			max_ending_here = 0
			s = i+1
	return (end - start + 1)

import pytest

def test_all_positive_numbers():
    a = [1, 2, 3, 4, 5]
    size = 5
    expected = 5
    assert max_sub_array_sum(a, size) == expected

def test_all_negative_numbers():
    a = [-1, -2, -3, -4, -5]
    size = 5
    expected = 1
    assert max_sub_array_sum(a, size) == expected

def test_mixed_numbers_max_subarray_in_middle():
    a = [-2, -3, 4, -1, -2, 1, 5, -3]
    size = 8
    expected = 5
    assert max_sub_array_sum(a, size) == expected

def test_single_element_array():
    a = [10]
    size = 1
    expected = 1
    assert max_sub_array_sum(a, size) == expected

def test_zeros_and_positive_numbers():
    a = [0, 0, 0, 0]
    size = 4
    expected = 1
    assert max_sub_array_sum(a, size) == expected

def test_zeros_and_negative_numbers():
    a = [0, -1, 0, -2]
    size = 4
    expected = 1
    assert max_sub_array_sum(a, size) == expected

def test_one_large_positive_surrounded_by_negatives():
    a = [-1, -2, 10, -1, -2]
    size = 5
    expected = 1
    assert max_sub_array_sum(a, size) == expected