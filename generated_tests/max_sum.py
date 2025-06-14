def max_sum(arr, n): 
	MSIBS = arr[:] 
	for i in range(n): 
		for j in range(0, i): 
			if arr[i] > arr[j] and MSIBS[i] < MSIBS[j] + arr[i]: 
				MSIBS[i] = MSIBS[j] + arr[i] 
	MSDBS = arr[:] 
	for i in range(1, n + 1): 
		for j in range(1, i): 
			if arr[-i] > arr[-j] and MSDBS[-i] < MSDBS[-j] + arr[-i]: 
				MSDBS[-i] = MSDBS[-j] + arr[-i] 
	max_sum = float("-Inf") 
	for i, j, k in zip(MSIBS, MSDBS, arr): 
		max_sum = max(max_sum, i + j - k) 
	return max_sum

import pytest

def test_single_element_array():
    arr = [5]
    n = 1
    expected = 5
    assert max_sum(arr, n) == expected

def test_strictly_increasing_array():
    arr = [1, 2, 3, 4, 5]
    n = 5
    expected = 15
    assert max_sum(arr, n) == expected

def test_strictly_decreasing_array():
    arr = [5, 4, 3, 2, 1]
    n = 5
    expected = 15
    assert max_sum(arr, n) == expected

def test_bitonic_sequence_with_peak_in_the_middle():
    arr = [1, 3, 5, 4, 2]
    n = 5
    expected = 12
    assert max_sum(arr, n) == expected

def test_array_with_all_equal_elements():
    arr = [2, 2, 2, 2]
    n = 4
    expected = 2
    assert max_sum(arr, n) == expected

def test_array_with_mixed_increasing_and_decreasing_parts():
    arr = [10, 5, 4, 3, 6, 8, 7]
    n = 7
    expected = 24
    assert max_sum(arr, n) == expected