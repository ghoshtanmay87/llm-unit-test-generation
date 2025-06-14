def div_list(nums1,nums2):
  result = map(lambda x, y: x / y, nums1, nums2)
  return list(result)

import pytest

def test_divide_equal_length_positive_integers():
    nums1 = [10, 20, 30]
    nums2 = [2, 4, 5]
    expected = [5.0, 5.0, 6.0]
    assert div_list(nums1, nums2) == expected

def test_divide_lists_with_floats():
    nums1 = [5.5, 7.2, 9.0]
    nums2 = [2.0, 3.6, 3.0]
    expected = [2.75, 2.0, 3.0]
    assert div_list(nums1, nums2) == expected

def test_divide_lists_nums1_contains_zeros():
    nums1 = [0, 10, 0]
    nums2 = [1, 2, 3]
    expected = [0.0, 5.0, 0.0]
    assert div_list(nums1, nums2) == expected

def test_divide_lists_with_negative_numbers():
    nums1 = [-10, 20, -30]
    nums2 = [2, -4, 5]
    expected = [-5.0, -5.0, -6.0]
    assert div_list(nums1, nums2) == expected

def test_divide_lists_nums2_all_ones():
    nums1 = [1, 2, 3]
    nums2 = [1, 1, 1]
    expected = [1.0, 2.0, 3.0]
    assert div_list(nums1, nums2) == expected

def test_divide_lists_mixed_int_float():
    nums1 = [4, 9.0, 16]
    nums2 = [2.0, 3, 4.0]
    expected = [2.0, 3.0, 4.0]
    assert div_list(nums1, nums2) == expected

def test_divide_two_empty_lists():
    nums1 = []
    nums2 = []
    expected = []
    assert div_list(nums1, nums2) == expected

def test_divide_lists_nums2_contains_zero_raises():
    nums1 = [1, 2, 3]
    nums2 = [1, 0, 3]
    with pytest.raises(ZeroDivisionError):
        div_list(nums1, nums2)