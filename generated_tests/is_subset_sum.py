def is_subset_sum(set, n, sum):
	if (sum == 0):
		return True
	if (n == 0):
		return False
	if (set[n - 1] > sum):
		return is_subset_sum(set, n - 1, sum)
	return is_subset_sum(set, n-1, sum) or is_subset_sum(set, n-1, sum-set[n-1])

import pytest

def test_sum_zero_should_return_true():
    # Sum is zero, should return True regardless of set contents
    input_set = [1, 2, 3]
    n = 3
    sum_value = 0
    expected = True
    assert is_subset_sum(input_set, n, sum_value) == expected

def test_empty_set_nonzero_sum_should_return_false():
    # Empty set with non-zero sum, should return False
    input_set = []
    n = 0
    sum_value = 5
    expected = False
    assert is_subset_sum(input_set, n, sum_value) == expected

def test_single_element_equal_to_sum_should_return_true():
    # Single element equal to sum, should return True
    input_set = [5]
    n = 1
    sum_value = 5
    expected = True
    assert is_subset_sum(input_set, n, sum_value) == expected

def test_single_element_less_than_sum_should_return_false():
    # Single element less than sum, no subset sums to sum, should return False
    input_set = [3]
    n = 1
    sum_value = 5
    expected = False
    assert is_subset_sum(input_set, n, sum_value) == expected

def test_multiple_elements_subset_sums_to_sum_should_return_true():
    # Multiple elements with subset summing to sum, should return True
    input_set = [3, 34, 4, 12, 5, 2]
    n = 6
    sum_value = 9
    expected = True
    assert is_subset_sum(input_set, n, sum_value) == expected

def test_multiple_elements_no_subset_sums_to_sum_should_return_false():
    # Multiple elements with no subset summing to sum, should return False
    input_set = [3, 34, 4, 12, 5, 2]
    n = 6
    sum_value = 30
    expected = False
    assert is_subset_sum(input_set, n, sum_value) == expected

def test_element_larger_than_sum_ignored_subset_sums_should_return_true():
    # Element larger than sum is ignored, subset sums to sum, should return True
    input_set = [10, 2, 3]
    n = 3
    sum_value = 5
    expected = True
    assert is_subset_sum(input_set, n, sum_value) == expected

def test_all_elements_larger_than_sum_should_return_false():
    # All elements larger than sum, should return False
    input_set = [6, 7, 8]
    n = 3
    sum_value = 5
    expected = False
    assert is_subset_sum(input_set, n, sum_value) == expected

def test_sum_equals_sum_of_all_elements_should_return_true():
    # Sum equals sum of all elements, should return True
    input_set = [1, 2, 3, 4]
    n = 4
    sum_value = 10
    expected = True
    assert is_subset_sum(input_set, n, sum_value) == expected

def test_sum_less_than_smallest_element_should_return_false():
    # Sum is less than smallest element, should return False
    input_set = [5, 6, 7]
    n = 3
    sum_value = 4
    expected = False
    assert is_subset_sum(input_set, n, sum_value) == expected