def intersection_array(array_nums1,array_nums2):
 result = list(filter(lambda x: x in array_nums1, array_nums2)) 
 return result

import pytest

def test_intersection_with_common_elements():
    # Find intersection when both arrays have common elements
    array_nums1 = [1, 2, 3, 4]
    array_nums2 = [3, 4, 5, 6]
    expected_output = [3, 4]
    assert intersection_array(array_nums1, array_nums2) == expected_output

def test_intersection_with_no_common_elements():
    # Find intersection when no elements are common
    array_nums1 = [1, 2, 3]
    array_nums2 = [4, 5, 6]
    expected_output = []
    assert intersection_array(array_nums1, array_nums2) == expected_output

def test_intersection_with_empty_array_nums2():
    # Find intersection when array_nums2 is empty
    array_nums1 = [1, 2, 3]
    array_nums2 = []
    expected_output = []
    assert intersection_array(array_nums1, array_nums2) == expected_output

def test_intersection_with_empty_array_nums1():
    # Find intersection when array_nums1 is empty
    array_nums1 = []
    array_nums2 = [1, 2, 3]
    expected_output = []
    assert intersection_array(array_nums1, array_nums2) == expected_output

def test_intersection_with_duplicates_in_array_nums2():
    # Find intersection with duplicate elements in array_nums2
    array_nums1 = [1, 2, 3]
    array_nums2 = [2, 2, 3, 4]
    expected_output = [2, 2, 3]
    assert intersection_array(array_nums1, array_nums2) == expected_output

def test_intersection_with_duplicates_in_array_nums1():
    # Find intersection with duplicate elements in array_nums1
    array_nums1 = [1, 2, 2, 3]
    array_nums2 = [2, 3, 4]
    expected_output = [2, 3]
    assert intersection_array(array_nums1, array_nums2) == expected_output

def test_intersection_with_identical_arrays():
    # Find intersection when both arrays are identical
    array_nums1 = [1, 2, 3]
    array_nums2 = [1, 2, 3]
    expected_output = [1, 2, 3]
    assert intersection_array(array_nums1, array_nums2) == expected_output

def test_intersection_with_extra_elements_in_array_nums2():
    # Find intersection when array_nums2 has elements not in array_nums1
    array_nums1 = [5, 6, 7]
    array_nums2 = [4, 5, 6, 8]
    expected_output = [5, 6]
    assert intersection_array(array_nums1, array_nums2) == expected_output