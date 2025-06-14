def add_list(nums1,nums2):
  result = map(lambda x, y: x + y, nums1, nums2)
  return list(result)

import pytest

def test_add_list_equal_length_positive_integers():
    nums1 = [1, 2, 3]
    nums2 = [4, 5, 6]
    expected = [5, 7, 9]
    assert add_list(nums1, nums2) == expected

def test_add_list_equal_length_negative_and_positive_integers():
    nums1 = [-1, 0, 3]
    nums2 = [1, -2, 4]
    expected = [0, -2, 7]
    assert add_list(nums1, nums2) == expected

def test_add_list_two_empty_lists():
    nums1 = []
    nums2 = []
    expected = []
    assert add_list(nums1, nums2) == expected

def test_add_list_lists_with_floats():
    nums1 = [1.5, 2.5]
    nums2 = [2.5, 3.5]
    expected = [4.0, 6.0]
    assert add_list(nums1, nums2) == expected

def test_add_list_different_lengths_shorter_second_list():
    nums1 = [1, 2, 3, 4]
    nums2 = [10, 20]
    expected = [11, 22]
    assert add_list(nums1, nums2) == expected

def test_add_list_different_lengths_shorter_first_list():
    nums1 = [5, 6]
    nums2 = [1, 2, 3]
    expected = [6, 8]
    assert add_list(nums1, nums2) == expected