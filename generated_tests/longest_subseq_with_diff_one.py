def longest_subseq_with_diff_one(arr, n): 
	dp = [1 for i in range(n)] 
	for i in range(n): 
		for j in range(i): 
			if ((arr[i] == arr[j]+1) or (arr[i] == arr[j]-1)): 
				dp[i] = max(dp[i], dp[j]+1) 
	result = 1
	for i in range(n): 
		if (result < dp[i]): 
			result = dp[i] 
	return result

import pytest

def test_single_element_array():
    arr = [5]
    n = 1
    expected = 1
    assert longest_subseq_with_diff_one(arr, n) == expected

def test_all_elements_equal():
    arr = [3, 3, 3, 3]
    n = 4
    expected = 1
    assert longest_subseq_with_diff_one(arr, n) == expected

def test_strictly_increasing_consecutive_numbers():
    arr = [1, 2, 3, 4, 5]
    n = 5
    expected = 5
    assert longest_subseq_with_diff_one(arr, n) == expected

def test_strictly_decreasing_consecutive_numbers():
    arr = [5, 4, 3, 2, 1]
    n = 5
    expected = 5
    assert longest_subseq_with_diff_one(arr, n) == expected

def test_mixed_array_with_multiple_subsequences():
    arr = [10, 9, 4, 5, 4, 8, 6]
    n = 7
    expected = 3
    assert longest_subseq_with_diff_one(arr, n) == expected

def test_array_with_gaps_and_repeated_elements():
    arr = [1, 2, 2, 3, 4, 2, 3]
    n = 7
    expected = 5
    assert longest_subseq_with_diff_one(arr, n) == expected

def test_array_with_no_adjacent_elements_differing_by_one():
    arr = [1, 3, 5, 7, 9]
    n = 5
    expected = 1
    assert longest_subseq_with_diff_one(arr, n) == expected

def test_array_with_multiple_subsequences_of_same_max_length():
    arr = [1, 2, 3, 2, 3, 4, 5]
    n = 7
    expected = 5
    assert longest_subseq_with_diff_one(arr, n) == expected