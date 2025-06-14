def moddiv_list(nums1,nums2):
  result = map(lambda x, y: x % y, nums1, nums2)
  return list(result)

import pytest

def test_moddiv_equal_length_positive_integers():
    nums1 = [10, 20, 30]
    nums2 = [3, 7, 4]
    expected = [1, 6, 2]
    assert moddiv_list(nums1, nums2) == expected

def test_moddiv_zeros_in_nums1():
    nums1 = [0, 0, 0]
    nums2 = [1, 2, 3]
    expected = [0, 0, 0]
    assert moddiv_list(nums1, nums2) == expected

def test_moddiv_nums1_smaller_than_nums2():
    nums1 = [1, 2, 3]
    nums2 = [5, 6, 7]
    expected = [1, 2, 3]
    assert moddiv_list(nums1, nums2) == expected

def test_moddiv_negative_nums1():
    nums1 = [-10, -20, -30]
    nums2 = [3, 7, 4]
    expected = [2, 1, 2]
    assert moddiv_list(nums1, nums2) == expected

def test_moddiv_negative_nums2():
    nums1 = [10, 20, 30]
    nums2 = [-3, -7, -4]
    expected = [-2, -1, -2]
    assert moddiv_list(nums1, nums2) == expected

def test_moddiv_mixed_positive_negative():
    nums1 = [10, -20, 30]
    nums2 = [3, -7, 4]
    expected = [1, -6, 2]
    assert moddiv_list(nums1, nums2) == expected

def test_moddiv_single_element_lists():
    nums1 = [5]
    nums2 = [2]
    expected = [1]
    assert moddiv_list(nums1, nums2) == expected

def test_moddiv_empty_lists():
    nums1 = []
    nums2 = []
    expected = []
    assert moddiv_list(nums1, nums2) == expected