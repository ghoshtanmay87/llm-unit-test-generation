def largest_subset(a, n):
	dp = [0 for i in range(n)]
	dp[n - 1] = 1; 
	for i in range(n - 2, -1, -1):
		mxm = 0;
		for j in range(i + 1, n):
			if a[j] % a[i] == 0 or a[i] % a[j] == 0:
				mxm = max(mxm, dp[j])
		dp[i] = 1 + mxm
	return max(dp)

import pytest

def test_single_element_list_returns_1():
    a = [7]
    n = 1
    expected = 1
    assert largest_subset(a, n) == expected

def test_all_elements_powers_of_2_largest_subset_includes_all():
    a = [1, 2, 4, 8]
    n = 4
    expected = 4
    assert largest_subset(a, n) == expected

def test_no_elements_divide_each_other_except_themselves():
    a = [2, 3, 5, 7]
    n = 4
    expected = 1
    assert largest_subset(a, n) == expected

def test_mixed_divisibility_with_some_chains():
    a = [3, 6, 7, 12]
    n = 4
    expected = 3
    assert largest_subset(a, n) == expected

def test_list_with_repeated_elements():
    a = [2, 2, 4, 8]
    n = 4
    expected = 4
    assert largest_subset(a, n) == expected

def test_elements_with_multiple_divisibility_options():
    a = [1, 3, 6, 24]
    n = 4
    expected = 4
    assert largest_subset(a, n) == expected

def test_elements_with_no_divisibility_except_self_unordered():
    a = [10, 5, 3, 7]
    n = 4
    expected = 1
    assert largest_subset(a, n) == expected

def test_descending_order_with_divisibility():
    a = [8, 4, 2, 1]
    n = 4
    expected = 4
    assert largest_subset(a, n) == expected

def test_list_with_prime_and_composite_numbers():
    a = [5, 10, 20, 25]
    n = 4
    expected = 3
    assert largest_subset(a, n) == expected

def test_empty_list_returns_0():
    a = []
    n = 0
    expected = 0
    assert largest_subset(a, n) == expected