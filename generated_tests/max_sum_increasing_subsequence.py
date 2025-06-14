def max_sum_increasing_subsequence(arr, n): 
	max = 0
	msis = [0 for x in range(n)] 
	for i in range(n): 
		msis[i] = arr[i] 
	for i in range(1, n): 
		for j in range(i): 
			if (arr[i] > arr[j] and
				msis[i] < msis[j] + arr[i]): 
				msis[i] = msis[j] + arr[i] 
	for i in range(n): 
		if max < msis[i]: 
			max = msis[i] 
	return max

import pytest

def test_single_element_array():
    arr = [10]
    n = 1
    expected = 10
    assert max_sum_increasing_subsequence(arr, n) == expected

def test_strictly_increasing_array():
    arr = [1, 2, 3, 4, 5]
    n = 5
    expected = 15
    assert max_sum_increasing_subsequence(arr, n) == expected

def test_strictly_decreasing_array():
    arr = [5, 4, 3, 2, 1]
    n = 5
    expected = 5
    assert max_sum_increasing_subsequence(arr, n) == expected

def test_mixed_increasing_and_decreasing_elements():
    arr = [1, 101, 2, 3, 100, 4, 5]
    n = 7
    expected = 106
    assert max_sum_increasing_subsequence(arr, n) == expected

def test_array_with_repeated_elements():
    arr = [3, 4, 5, 3, 7]
    n = 5
    expected = 19
    assert max_sum_increasing_subsequence(arr, n) == expected

def test_array_with_all_elements_equal():
    arr = [7, 7, 7, 7]
    n = 4
    expected = 7
    assert max_sum_increasing_subsequence(arr, n) == expected

def test_array_with_negative_and_positive_numbers():
    arr = [-1, 2, 3, -2, 5]
    n = 5
    expected = 10
    assert max_sum_increasing_subsequence(arr, n) == expected

def test_array_with_zeros_and_positive_numbers():
    arr = [0, 1, 0, 3, 2, 3]
    n = 6
    expected = 7
    assert max_sum_increasing_subsequence(arr, n) == expected

def test_empty_array():
    arr = []
    n = 0
    expected = 0
    assert max_sum_increasing_subsequence(arr, n) == expected