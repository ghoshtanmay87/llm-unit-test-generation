def pairs_sum_to_zero(l):
    for i, l1 in enumerate(l):
        for j in range(i + 1, len(l)):
            if l1 + l[j] == 0:
                return True
    return False

import pytest

def test_pairs_sum_to_zero_with_pair_summing_to_zero():
    # List contains a pair of numbers that sum to zero
    input_list = [1, 2, -1, 4]
    expected = True
    assert pairs_sum_to_zero(input_list) == expected

def test_pairs_sum_to_zero_with_no_pairs_summing_to_zero():
    # List contains no pairs that sum to zero
    input_list = [1, 2, 3, 4]
    expected = False
    assert pairs_sum_to_zero(input_list) == expected

def test_pairs_sum_to_zero_with_zero_twice():
    # List contains zero twice, which sums to zero
    input_list = [0, 0, 1]
    expected = True
    assert pairs_sum_to_zero(input_list) == expected

def test_pairs_sum_to_zero_with_single_zero_element():
    # List contains a single zero element only
    input_list = [0]
    expected = False
    assert pairs_sum_to_zero(input_list) == expected

def test_pairs_sum_to_zero_with_empty_list():
    # Empty list input
    input_list = []
    expected = False
    assert pairs_sum_to_zero(input_list) == expected

def test_pairs_sum_to_zero_with_multiple_pairs_summing_to_zero():
    # List with multiple pairs summing to zero, returns True on first found
    input_list = [3, -3, 2, -2]
    expected = True
    assert pairs_sum_to_zero(input_list) == expected

def test_pairs_sum_to_zero_with_positive_and_negative_no_zero_sum_pairs():
    # List with positive and negative numbers but no zero-sum pairs
    input_list = [5, -4, 3, -2]
    expected = False
    assert pairs_sum_to_zero(input_list) == expected