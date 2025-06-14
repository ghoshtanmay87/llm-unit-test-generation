def large_product(nums1, nums2, N):
    result = sorted([x*y for x in nums1 for y in nums2], reverse=True)[:N]
    return result

import pytest

def test_top_3_largest_products_from_two_small_lists():
    nums1 = [1, 2]
    nums2 = [3, 4]
    N = 3
    expected = [8, 6, 4]
    assert large_product(nums1, nums2, N) == expected

def test_request_more_products_than_possible_combinations():
    nums1 = [5]
    nums2 = [10]
    N = 5
    expected = [50]
    assert large_product(nums1, nums2, N) == expected

def test_include_zero_and_negative_numbers_in_inputs():
    nums1 = [-1, 0, 2]
    nums2 = [3, -4]
    N = 4
    expected = [6, 4, 0, 0]
    assert large_product(nums1, nums2, N) == expected

def test_all_negative_numbers_in_inputs():
    nums1 = [-2, -3]
    nums2 = [-4, -5]
    N = 2
    expected = [15, 12]
    assert large_product(nums1, nums2, N) == expected

def test_n_is_zero_expect_empty_list():
    nums1 = [1, 2, 3]
    nums2 = [4, 5, 6]
    N = 0
    expected = []
    assert large_product(nums1, nums2, N) == expected

def test_large_n_with_multiple_duplicates():
    nums1 = [2, 2]
    nums2 = [3, 3]
    N = 5
    expected = [6, 6, 6, 6]
    assert large_product(nums1, nums2, N) == expected