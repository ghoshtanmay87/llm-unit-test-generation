def lbs(arr): 
	n = len(arr) 
	lis = [1 for i in range(n+1)] 
	for i in range(1 , n): 
		for j in range(0 , i): 
			if ((arr[i] > arr[j]) and (lis[i] < lis[j] +1)): 
				lis[i] = lis[j] + 1
	lds = [1 for i in range(n+1)] 
	for i in reversed(range(n-1)): 
		for j in reversed(range(i-1 ,n)): 
			if(arr[i] > arr[j] and lds[i] < lds[j] + 1): 
				lds[i] = lds[j] + 1
	maximum = lis[0] + lds[0] - 1
	for i in range(1 , n): 
		maximum = max((lis[i] + lds[i]-1), maximum) 
	return maximum

import pytest

def test_lbs_simple_increasing_then_decreasing():
    # The entire array is strictly increasing up to 4 and then strictly decreasing,
    # so the longest bitonic subsequence is the whole array with length 7.
    arr = [1, 2, 3, 4, 3, 2, 1]
    expected = 7
    assert lbs(arr) == expected

def test_lbs_strictly_increasing_sequence():
    # The longest increasing subsequence is the entire array (length 5),
    # and the longest decreasing subsequence from any point is 1,
    # so the bitonic subsequence length is 5.
    arr = [1, 2, 3, 4, 5]
    expected = 5
    assert lbs(arr) == expected

def test_lbs_strictly_decreasing_sequence():
    # The longest decreasing subsequence is the entire array (length 5),
    # and the longest increasing subsequence from any point is 1,
    # so the bitonic subsequence length is 5.
    arr = [5, 4, 3, 2, 1]
    expected = 5
    assert lbs(arr) == expected

def test_lbs_sequence_with_multiple_peaks():
    # The longest bitonic subsequence is [1, 2, 10, 5, 2, 1] or [1, 2, 4, 5, 2, 1], length 6.
    arr = [1, 11, 2, 10, 4, 5, 2, 1]
    expected = 6
    assert lbs(arr) == expected

def test_lbs_all_equal_elements():
    # No strictly increasing or decreasing subsequence longer than 1 exists because all elements are equal,
    # so the longest bitonic subsequence length is 1.
    arr = [3, 3, 3, 3, 3]
    expected = 1
    assert lbs(arr) == expected

def test_lbs_empty_array():
    # Empty array has no subsequences, so the longest bitonic subsequence length is 0.
    arr = []
    expected = 0
    assert lbs(arr) == expected

def test_lbs_single_element_array():
    # Single element array has longest bitonic subsequence length 1.
    arr = [10]
    expected = 1
    assert lbs(arr) == expected