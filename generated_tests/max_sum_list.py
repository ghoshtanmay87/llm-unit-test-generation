def max_sum_list(lists):
 return max(lists, key=sum)

import pytest

def test_single_list_input():
    # Only one list is present, so it is returned as the maximum sum list by default.
    input_lists = [[1, 2, 3]]
    expected = [1, 2, 3]
    assert max_sum_list(input_lists) == expected

def test_multiple_lists_with_distinct_sums():
    # Sum of [1, 2, 3] is 6, sum of [4, 5] is 9, sum of [0, 0, 0, 10] is 10.
    # The list with the maximum sum is [0, 0, 0, 10].
    input_lists = [[1, 2, 3], [4, 5], [0, 0, 0, 10]]
    expected = [0, 0, 0, 10]
    assert max_sum_list(input_lists) == expected

def test_multiple_lists_with_one_having_maximum_sum():
    # Sum of [-1, -2, -3] is -6, sum of [0] is 0, sum of [1, 1, 1] is 3.
    # The list with the maximum sum is [1, 1, 1].
    input_lists = [[-1, -2, -3], [0], [1, 1, 1]]
    expected = [1, 1, 1]
    assert max_sum_list(input_lists) == expected

def test_multiple_lists_with_equal_maximum_sums():
    # Sum of [1, 2] is 3, sum of [3] is 3, sum of [0, 3] is 3.
    # Since all sums are equal, max returns the first list with the maximum sum, which is [1, 2].
    input_lists = [[1, 2], [3], [0, 3]]
    expected = [1, 2]
    assert max_sum_list(input_lists) == expected

def test_lists_with_negative_and_positive_numbers():
    # Sum of [-10, 20] is 10, sum of [5, 5] is 10, sum of [15, -5] is 10.
    # All sums are equal, so the first list with the max sum is returned, which is [-10, 20].
    input_lists = [[-10, 20], [5, 5], [15, -5]]
    expected = [-10, 20]
    assert max_sum_list(input_lists) == expected

def test_empty_lists_included():
    # Sum of [] is 0, sum of [0] is 0, sum of [-1, 1] is 0.
    # All sums are equal, so the first list with the max sum is returned, which is [].
    input_lists = [[], [0], [-1, 1]]
    expected = []
    assert max_sum_list(input_lists) == expected