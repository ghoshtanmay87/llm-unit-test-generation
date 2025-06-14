def max_subarray_product(arr):
	n = len(arr)
	max_ending_here = 1
	min_ending_here = 1
	max_so_far = 0
	flag = 0
	for i in range(0, n):
		if arr[i] > 0:
			max_ending_here = max_ending_here * arr[i]
			min_ending_here = min (min_ending_here * arr[i], 1)
			flag = 1
		elif arr[i] == 0:
			max_ending_here = 1
			min_ending_here = 1
		else:
			temp = max_ending_here
			max_ending_here = max (min_ending_here * arr[i], 1)
			min_ending_here = temp * arr[i]
		if (max_so_far < max_ending_here):
			max_so_far = max_ending_here
	if flag == 0 and max_so_far == 0:
		return 0
	return max_so_far

import pytest

def test_all_positive_numbers():
    arr = [1, 2, 3, 4]
    expected = 24
    assert max_subarray_product(arr) == expected

def test_array_with_zero_resetting_product():
    arr = [1, 0, 3, 4]
    expected = 12
    assert max_subarray_product(arr) == expected

def test_array_with_negative_numbers_and_even_count():
    arr = [-1, -2, -3, -4]
    expected = 24
    assert max_subarray_product(arr) == expected

def test_array_with_negative_numbers_and_odd_count():
    arr = [-1, -2, -3]
    expected = 6
    assert max_subarray_product(arr) == expected

def test_array_with_single_zero():
    arr = [0]
    expected = 0
    assert max_subarray_product(arr) == expected

def test_array_with_single_negative_number():
    arr = [-5]
    expected = 0
    assert max_subarray_product(arr) == expected

def test_array_with_positive_negative_and_zero():
    arr = [2, -3, 0, 4, -1]
    expected = 4
    assert max_subarray_product(arr) == expected

def test_array_with_multiple_zeros():
    arr = [0, -1, 0, -2, 0]
    expected = 0
    assert max_subarray_product(arr) == expected

def test_array_with_one_positive_number_among_negatives():
    arr = [-1, 2, -3, 4]
    expected = 24
    assert max_subarray_product(arr) == expected

def test_array_with_all_ones():
    arr = [1, 1, 1, 1]
    expected = 1
    assert max_subarray_product(arr) == expected