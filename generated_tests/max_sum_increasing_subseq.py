def max_sum_increasing_subseq(a, n, index, k):
	dp = [[0 for i in range(n)] 
			for i in range(n)]
	for i in range(n):
		if a[i] > a[0]:
			dp[0][i] = a[i] + a[0]
		else:
			dp[0][i] = a[i]
	for i in range(1, n):
		for j in range(n):
			if a[j] > a[i] and j > i:
				if dp[i - 1][i] + a[j] > dp[i - 1][j]:
					dp[i][j] = dp[i - 1][i] + a[j]
				else:
					dp[i][j] = dp[i - 1][j]
			else:
				dp[i][j] = dp[i - 1][j]
	return dp[index][k]

import pytest

def test_max_sum_increasing_subseq_small_array_index0_k1():
    # Scenario: Calculate max sum increasing subsequence for a small array with index=0 and k=1
    a = [1, 2, 3]
    n = 3
    index = 0
    k = 1
    expected_output = 3
    assert max_sum_increasing_subseq(a, n, index, k) == expected_output

def test_max_sum_increasing_subseq_small_array_index1_k2():
    # Scenario: Calculate max sum increasing subsequence for a small array with index=1 and k=2
    a = [1, 2, 3]
    n = 3
    index = 1
    k = 2
    expected_output = 6
    assert max_sum_increasing_subseq(a, n, index, k) == expected_output

def test_max_sum_increasing_subseq_no_increasing_pairs_index0_k0():
    # Scenario: Calculate max sum increasing subsequence for array with no increasing pairs at index=0 and k=0
    a = [5, 4, 3]
    n = 3
    index = 0
    k = 0
    expected_output = 5
    assert max_sum_increasing_subseq(a, n, index, k) == expected_output

def test_max_sum_increasing_subseq_repeated_elements_index0_k1():
    # Scenario: Calculate max sum increasing subsequence for array with repeated elements at index=0 and k=1
    a = [2, 2, 3]
    n = 3
    index = 0
    k = 1
    expected_output = 2
    assert max_sum_increasing_subseq(a, n, index, k) == expected_output

def test_max_sum_increasing_subseq_mixed_values_index2_k3():
    # Scenario: Calculate max sum increasing subsequence for array with mixed values at index=2 and k=3
    a = [1, 101, 2, 3, 100]
    n = 5
    index = 2
    k = 3
    expected_output = 106
    assert max_sum_increasing_subseq(a, n, index, k) == expected_output