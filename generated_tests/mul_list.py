def mul_list(nums1,nums2):
  result = map(lambda x, y: x * y, nums1, nums2)
  return list(result)

import pytest

def test_multiply_two_lists_of_equal_length_with_positive_integers():
    nums1 = [1, 2, 3]
    nums2 = [4, 5, 6]
    expected_output = [4, 10, 18]
    assert mul_list(nums1, nums2) == expected_output

def test_multiply_two_lists_where_one_list_contains_zeroes():
    nums1 = [0, 2, 0]
    nums2 = [4, 0, 6]
    expected_output = [0, 0, 0]
    assert mul_list(nums1, nums2) == expected_output

def test_multiply_two_lists_with_negative_and_positive_integers():
    nums1 = [-1, 2, -3]
    nums2 = [4, -5, 6]
    expected_output = [-4, -10, -18]
    assert mul_list(nums1, nums2) == expected_output

def test_multiply_two_empty_lists():
    nums1 = []
    nums2 = []
    expected_output = []
    assert mul_list(nums1, nums2) == expected_output

def test_multiply_two_lists_of_different_lengths():
    nums1 = [1, 2, 3, 4]
    nums2 = [10, 20]
    expected_output = [10, 40]
    assert mul_list(nums1, nums2) == expected_output