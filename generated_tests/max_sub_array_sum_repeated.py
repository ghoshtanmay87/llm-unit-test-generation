def max_sub_array_sum_repeated(a, n, k): 
	max_so_far = -2147483648
	max_ending_here = 0
	for i in range(n*k): 
		max_ending_here = max_ending_here + a[i%n] 
		if (max_so_far < max_ending_here): 
			max_so_far = max_ending_here 
		if (max_ending_here < 0): 
			max_ending_here = 0
	return max_so_far

import pytest

def test_single_element_array_repeated_once():
    a = [5]
    n = 1
    k = 1
    expected = 5
    assert max_sub_array_sum_repeated(a, n, k) == expected

def test_single_element_array_repeated_multiple_times():
    a = [5]
    n = 1
    k = 3
    expected = 15
    assert max_sub_array_sum_repeated(a, n, k) == expected

def test_all_negative_elements_repeated_once():
    a = [-2, -3, -1]
    n = 3
    k = 1
    expected = 0
    assert max_sub_array_sum_repeated(a, n, k) == expected

def test_mixed_positive_and_negative_elements_repeated_twice():
    a = [1, -2, 3]
    n = 3
    k = 2
    expected = 4
    assert max_sub_array_sum_repeated(a, n, k) == expected

def test_array_with_zero_and_positive_elements_repeated_thrice():
    a = [0, 2, -1, 2]
    n = 4
    k = 3
    expected = 7
    assert max_sub_array_sum_repeated(a, n, k) == expected

def test_array_with_all_positive_elements_repeated_twice():
    a = [1, 2, 3]
    n = 3
    k = 2
    expected = 12
    assert max_sub_array_sum_repeated(a, n, k) == expected

def test_array_with_negative_prefix_and_positive_suffix_repeated_twice_corrected():
    a = [-1, -2, 3, 4]
    n = 4
    k = 2
    expected = 11
    assert max_sub_array_sum_repeated(a, n, k) == expected

def test_array_with_zeros_only_repeated_multiple_times():
    a = [0, 0, 0]
    n = 3
    k = 5
    expected = 0
    assert max_sub_array_sum_repeated(a, n, k) == expected

def test_array_with_one_large_positive_and_rest_negative_repeated_once():
    a = [-1, 10, -2, -3]
    n = 4
    k = 1
    expected = 10
    assert max_sub_array_sum_repeated(a, n, k) == expected