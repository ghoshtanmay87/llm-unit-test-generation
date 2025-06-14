from operator import eq
def count_same_pair(nums1, nums2):
    result = sum(map(eq, nums1, nums2))
    return result

import pytest

def test_count_pairs_all_elements_equal():
    nums1 = [1, 2, 3]
    nums2 = [1, 2, 3]
    expected = 3
    assert count_same_pair(nums1, nums2) == expected

def test_count_pairs_no_matching_elements():
    nums1 = [1, 2, 3]
    nums2 = [4, 5, 6]
    expected = 0
    assert count_same_pair(nums1, nums2) == expected

def test_count_pairs_some_matching_elements():
    nums1 = [1, 2, 3, 4]
    nums2 = [1, 3, 3, 5]
    expected = 2
    assert count_same_pair(nums1, nums2) == expected

def test_count_pairs_empty_lists():
    nums1 = []
    nums2 = []
    expected = 0
    assert count_same_pair(nums1, nums2) == expected

def test_count_pairs_different_lengths_shorter_second_list():
    nums1 = [1, 2, 3, 4]
    nums2 = [1, 2]
    expected = 2
    assert count_same_pair(nums1, nums2) == expected

def test_count_pairs_different_lengths_shorter_first_list():
    nums1 = [1, 2]
    nums2 = [1, 2, 3, 4]
    expected = 2
    assert count_same_pair(nums1, nums2) == expected

def test_count_pairs_repeated_elements():
    nums1 = [5, 5, 5]
    nums2 = [5, 6, 5]
    expected = 2
    assert count_same_pair(nums1, nums2) == expected