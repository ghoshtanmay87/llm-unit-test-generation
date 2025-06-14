def sub_list(nums1,nums2):
  result = map(lambda x, y: x - y, nums1, nums2)
  return list(result)

import pytest

def test_subtract_equal_length_positive_integers():
    nums1 = [5, 10, 15]
    nums2 = [1, 2, 3]
    expected_output = [4, 8, 12]
    assert sub_list(nums1, nums2) == expected_output

def test_subtract_negative_and_positive_integers():
    nums1 = [0, -5, 10]
    nums2 = [5, -5, 5]
    expected_output = [-5, 0, 5]
    assert sub_list(nums1, nums2) == expected_output

def test_subtract_lists_with_zeros():
    nums1 = [0, 0, 0]
    nums2 = [0, 0, 0]
    expected_output = [0, 0, 0]
    assert sub_list(nums1, nums2) == expected_output

def test_subtract_nums2_larger_values():
    nums1 = [1, 2, 3]
    nums2 = [4, 5, 6]
    expected_output = [-3, -3, -3]
    assert sub_list(nums1, nums2) == expected_output

def test_subtract_floating_point_numbers():
    nums1 = [1.5, 2.5, 3.5]
    nums2 = [0.5, 1.5, 2.5]
    expected_output = [1.0, 1.0, 1.0]
    assert sub_list(nums1, nums2) == expected_output