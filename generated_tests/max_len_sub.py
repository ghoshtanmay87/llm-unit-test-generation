def max_len_sub( arr, n): 
	mls=[] 
	max = 0
	for i in range(n): 
		mls.append(1) 
	for i in range(n): 
		for j in range(i): 
			if (abs(arr[i] - arr[j]) <= 1 and mls[i] < mls[j] + 1): 
				mls[i] = mls[j] + 1
	for i in range(n): 
		if (max < mls[i]): 
			max = mls[i] 
	return max

import pytest

def test_all_elements_are_the_same():
    arr = [5, 5, 5, 5]
    n = 4
    expected = 4
    assert max_len_sub(arr, n) == expected

def test_elements_differ_by_more_than_one_no_longer_subsequence():
    arr = [1, 4, 7, 10]
    n = 4
    expected = 1
    assert max_len_sub(arr, n) == expected

def test_mixed_elements_with_differences_leq_one_forming_subsequence():
    arr = [1, 2, 2, 3, 4]
    n = 5
    expected = 4
    assert max_len_sub(arr, n) == expected

def test_strictly_increasing_consecutive_integers():
    arr = [1, 2, 3, 4, 5]
    n = 5
    expected = 5
    assert max_len_sub(arr, n) == expected

def test_array_with_negative_and_positive_integers():
    arr = [-1, 0, 1, 2, 3]
    n = 5
    expected = 5
    assert max_len_sub(arr, n) == expected

def test_array_with_repeated_elements_and_gaps():
    arr = [4, 5, 5, 6, 8, 9]
    n = 6
    expected = 4
    assert max_len_sub(arr, n) == expected

def test_single_element_array():
    arr = [10]
    n = 1
    expected = 1
    assert max_len_sub(arr, n) == expected

def test_empty_array():
    arr = []
    n = 0
    expected = 0
    assert max_len_sub(arr, n) == expected