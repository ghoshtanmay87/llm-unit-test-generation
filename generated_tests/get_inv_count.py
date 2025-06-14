def get_inv_count(arr, n): 
	inv_count = 0
	for i in range(n): 
		for j in range(i + 1, n): 
			if (arr[i] > arr[j]): 
				inv_count += 1
	return inv_count

import pytest

def test_count_inversions_empty_array():
    # An empty array has no elements, so there are no pairs to compare and no inversions.
    arr = []
    n = 0
    expected = 0
    assert get_inv_count(arr, n) == expected

def test_count_inversions_sorted_ascending_array():
    # The array is sorted in ascending order, so no element is greater than any element that comes after it, resulting in zero inversions.
    arr = [1, 2, 3, 4, 5]
    n = 5
    expected = 0
    assert get_inv_count(arr, n) == expected

def test_count_inversions_sorted_descending_array():
    # Every pair (i, j) with i < j is an inversion because each earlier element is greater than all elements after it. For 5 elements, total pairs are 5*4/2 = 10.
    arr = [5, 4, 3, 2, 1]
    n = 5
    expected = 10
    assert get_inv_count(arr, n) == expected

def test_count_inversions_some_inversions():
    # Inversions are (21), (41), and (43). Total 3 inversions.
    arr = [2, 4, 1, 3, 5]
    n = 5
    expected = 3
    assert get_inv_count(arr, n) == expected

def test_count_inversions_with_duplicates():
    # Inversions are (32), (31), (31), and (21). Total 4 inversions.
    arr = [1, 3, 2, 3, 1]
    n = 5
    expected = 4
    assert get_inv_count(arr, n) == expected

def test_count_inversions_single_element_array():
    # With only one element, there are no pairs to compare, so zero inversions.
    arr = [42]
    n = 1
    expected = 0
    assert get_inv_count(arr, n) == expected