def maximum_product(nums):
    import heapq
    a, b = heapq.nlargest(3, nums), heapq.nsmallest(2, nums)
    return max(a[0] * a[1] * a[2], a[0] * b[0] * b[1])

import pytest

def test_all_positive_numbers():
    nums = [1, 2, 3, 4]
    expected = 24
    assert maximum_product(nums) == expected

def test_includes_negative_numbers_product_of_two_negatives_and_one_positive_is_largest():
    nums = [-10, -10, 5, 2]
    expected = 500
    assert maximum_product(nums) == expected

def test_all_negative_numbers():
    nums = [-5, -4, -3, -2]
    expected = -24
    assert maximum_product(nums) == expected

def test_mixed_positive_and_negative_with_zero():
    nums = [-1, 0, 1, 2, 3]
    expected = 6
    assert maximum_product(nums) == expected

def test_exactly_three_numbers():
    nums = [1, 2, 3]
    expected = 6
    assert maximum_product(nums) == expected

def test_two_large_negatives_and_one_large_positive():
    nums = [-100, -98, 1, 2, 3]
    expected = 29400
    assert maximum_product(nums) == expected