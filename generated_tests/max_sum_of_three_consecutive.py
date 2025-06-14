def max_sum_of_three_consecutive(arr, n): 
	sum = [0 for k in range(n)] 
	if n >= 1: 
		sum[0] = arr[0] 
	if n >= 2: 
		sum[1] = arr[0] + arr[1] 
	if n > 2: 
		sum[2] = max(sum[1], max(arr[1] + arr[2], arr[0] + arr[2])) 
	for i in range(3, n): 
		sum[i] = max(max(sum[i-1], sum[i-2] + arr[i]), arr[i] + arr[i-1] + sum[i-3]) 
	return sum[n-1]

import pytest

def test_array_with_single_element():
    arr = [5]
    n = 1
    expected = 5
    assert max_sum_of_three_consecutive(arr, n) == expected

def test_array_with_two_elements():
    arr = [3, 7]
    n = 2
    expected = 10
    assert max_sum_of_three_consecutive(arr, n) == expected

def test_array_with_three_elements():
    arr = [1, 2, 3]
    n = 3
    expected = 5
    assert max_sum_of_three_consecutive(arr, n) == expected

def test_array_with_four_elements_corrected():
    arr = [1, 2, 3, 4]
    n = 4
    expected = 8
    assert max_sum_of_three_consecutive(arr, n) == expected

def test_array_with_five_elements_corrected():
    arr = [2, 1, 5, 1, 3]
    n = 5
    expected = 10
    assert max_sum_of_three_consecutive(arr, n) == expected

def test_array_with_six_elements_corrected():
    arr = [4, 2, 1, 7, 8, 1]
    n = 6
    expected = 21
    assert max_sum_of_three_consecutive(arr, n) == expected

def test_array_with_all_equal_elements():
    arr = [3, 3, 3, 3, 3]
    n = 5
    expected = 12
    assert max_sum_of_three_consecutive(arr, n) == expected