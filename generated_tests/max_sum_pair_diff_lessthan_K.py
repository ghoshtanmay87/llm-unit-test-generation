def max_sum_pair_diff_lessthan_K(arr, N, K): 
	arr.sort() 
	dp = [0] * N 
	dp[0] = 0
	for i in range(1, N): 
		dp[i] = dp[i-1] 
		if (arr[i] - arr[i-1] < K): 
			if (i >= 2): 
				dp[i] = max(dp[i], dp[i-2] + arr[i] + arr[i-1]); 
			else: 
				dp[i] = max(dp[i], arr[i] + arr[i-1]); 
	return dp[N - 1]

import pytest

def test_no_pairs_with_difference_less_than_K():
    # Array with no pairs having difference less than K
    arr = [1, 10, 20, 30]
    N = 4
    K = 5
    expected = 0
    assert max_sum_pair_diff_lessthan_K(arr, N, K) == expected

def test_one_valid_pair_difference_less_than_K():
    # Array with one valid pair difference less than K
    arr = [1, 3, 10, 20]
    N = 4
    K = 3
    expected = 4
    assert max_sum_pair_diff_lessthan_K(arr, N, K) == expected

def test_multiple_valid_pairs_non_overlapping_maximize_sum():
    # Array with multiple valid pairs, non-overlapping pairs maximize sum
    arr = [3, 5, 10, 15, 17, 20]
    N = 6
    K = 5
    expected = 40
    assert max_sum_pair_diff_lessthan_K(arr, N, K) == expected

def test_all_elements_equal_and_K_greater_than_zero():
    # Array with all elements equal and K > 0
    arr = [4, 4, 4, 4]
    N = 4
    K = 1
    expected = 16
    assert max_sum_pair_diff_lessthan_K(arr, N, K) == expected

def test_pairs_overlapping_function_chooses_optimal_non_overlapping():
    # Array with pairs overlapping, function chooses optimal non-overlapping pairs
    arr = [1, 2, 3, 4, 5]
    N = 5
    K = 3
    expected = 12
    assert max_sum_pair_diff_lessthan_K(arr, N, K) == expected

def test_empty_array():
    # Array with no elements
    arr = []
    N = 0
    K = 10
    expected = 0
    assert max_sum_pair_diff_lessthan_K(arr, N, K) == expected

def test_single_element_array():
    # Array with single element
    arr = [10]
    N = 1
    K = 5
    expected = 0
    assert max_sum_pair_diff_lessthan_K(arr, N, K) == expected

def test_all_pairs_valid_maximum_sum_is_sum_of_all_pairs():
    # Array with all pairs valid and maximum sum is sum of all pairs
    arr = [1, 2, 3, 4]
    N = 4
    K = 5
    expected = 10
    assert max_sum_pair_diff_lessthan_K(arr, N, K) == expected