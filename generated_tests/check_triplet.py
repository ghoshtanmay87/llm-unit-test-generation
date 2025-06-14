def check_triplet(A, n, sum, count):
    if count == 3 and sum == 0:
        return True
    if count == 3 or n == 0 or sum < 0:
        return False
    return check_triplet(A, n - 1, sum - A[n - 1], count + 1) or\
           check_triplet(A, n - 1, sum, count)

import pytest

def test_triplet_exists_with_exact_zero_sum():
    A = [1, 2, -3, 4]
    n = 4
    sum_val = 0
    count = 0
    assert check_triplet(A, n, sum_val, count) is True

def test_triplet_does_not_exist_when_sum_cannot_be_zero():
    A = [1, 2, 3, 4]
    n = 4
    sum_val = 0
    count = 0
    assert check_triplet(A, n, sum_val, count) is False

def test_triplet_with_negative_sum_early_termination():
    A = [5, 6, 7]
    n = 3
    sum_val = 0
    count = 0
    assert check_triplet(A, n, sum_val, count) is False

def test_triplet_with_sum_zero_and_exactly_three_elements_chosen():
    A = [0, 0, 0]
    n = 3
    sum_val = 0
    count = 0
    assert check_triplet(A, n, sum_val, count) is True

def test_triplet_with_sum_zero_and_more_than_three_elements_in_list():
    A = [1, -1, 0, 0]
    n = 4
    sum_val = 0
    count = 0
    assert check_triplet(A, n, sum_val, count) is True