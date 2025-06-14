def count_nums(arr):

    def digits_sum(n):
        neg = 1
        if n < 0:
            n, neg = (-1 * n, -1)
        n = [int(i) for i in str(n)]
        n[0] = n[0] * neg
        return sum(n)
    return len(list(filter(lambda x: x > 0, [digits_sum(i) for i in arr])))

import pytest

def test_all_positive_numbers_with_single_digit_sums():
    arr = [1, 2, 3, 4, 5]
    expected_output = 5
    assert count_nums(arr) == expected_output

def test_all_negative_numbers_with_single_digit_sums():
    arr = [-1, -2, -3, -4, -5]
    expected_output = 0
    assert count_nums(arr) == expected_output

def test_zero_and_positive_numbers():
    arr = [0, 10, 20]
    expected_output = 2
    assert count_nums(arr) == expected_output

def test_zero_and_negative_numbers():
    arr = [0, -10, -20]
    expected_output = 0
    assert count_nums(arr) == expected_output

def test_numbers_where_digits_sum_results_in_zero():
    arr = [0, 0]
    expected_output = 0
    assert count_nums(arr) == expected_output

def test_single_negative_number_with_digits_summing_to_zero():
    arr = [-11]
    expected_output = 0
    assert count_nums(arr) == expected_output

def test_single_positive_number_with_digits_summing_to_zero():
    arr = [0]
    expected_output = 0
    assert count_nums(arr) == expected_output

def test_numbers_with_multiple_digits_and_mixed_signs():
    arr = [123, -123, 456, -456]
    expected_output = 4
    assert count_nums(arr) == expected_output

def test_mixed_numbers_with_zero_and_positive_sums():
    arr = [101, -101, 202, -202, 0]
    expected_output = 2
    assert count_nums(arr) == expected_output

def test_mixed_positive_and_negative_numbers_with_multi_digit_sums():
    arr = [12, -12, 34, -34]
    expected_output = 4
    assert count_nums(arr) == expected_output