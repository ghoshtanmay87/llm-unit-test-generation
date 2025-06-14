def no_of_subsequences(arr, k): 
	n = len(arr) 
	dp = [[0 for i in range(n + 1)] 
			for j in range(k + 1)] 
	for i in range(1, k + 1): 
		for j in range(1, n + 1): 
			dp[i][j] = dp[i][j - 1] 
			if arr[j - 1] <= i and arr[j - 1] > 0: 
				dp[i][j] += dp[i // arr[j - 1]][j - 1] + 1
	return dp[k][n]

import pytest

def test_empty_array_any_k():
    # Empty array input with any k
    arr = []
    k = 5
    expected = 0
    assert no_of_subsequences(arr, k) == expected

def test_single_element_equal_to_k():
    # Array with one element equal to k
    arr = [2]
    k = 2
    expected = 1
    assert no_of_subsequences(arr, k) == expected

def test_single_element_greater_than_k():
    # Array with one element greater than k
    arr = [3]
    k = 2
    expected = 0
    assert no_of_subsequences(arr, k) == expected

def test_all_elements_one_k_one():
    # Array with multiple elements all equal to 1 and k=1
    arr = [1, 1, 1]
    k = 1
    expected = 6
    assert no_of_subsequences(arr, k) == expected

def test_elements_1_2_3_k_6():
    # Array with elements [1, 2, 3] and k=6
    arr = [1, 2, 3]
    k = 6
    expected = 7
    assert no_of_subsequences(arr, k) == expected

def test_array_with_zero_and_positive_k_3():
    # Array with zero and positive elements, k=3
    arr = [0, 1, 3]
    k = 3
    expected = 3
    assert no_of_subsequences(arr, k) == expected

def test_elements_2_2_2_k_4():
    # Array with elements [2, 2, 2] and k=4
    arr = [2, 2, 2]
    k = 4
    expected = 5
    assert no_of_subsequences(arr, k) == expected