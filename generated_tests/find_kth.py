def find_kth(arr1, arr2, m, n, k):
	sorted1 = [0] * (m + n)
	i = 0
	j = 0
	d = 0
	while (i < m and j < n):
		if (arr1[i] < arr2[j]):
			sorted1[d] = arr1[i]
			i += 1
		else:
			sorted1[d] = arr2[j]
			j += 1
		d += 1
	while (i < m):
		sorted1[d] = arr1[i]
		d += 1
		i += 1
	while (j < n):
		sorted1[d] = arr2[j]
		d += 1
		j += 1
	return sorted1[k - 1]

import pytest

def test_find_3rd_smallest_element_equal_length_arrays():
    arr1 = [1, 3, 5]
    arr2 = [2, 4, 6]
    m = 3
    n = 3
    k = 3
    expected = 3
    assert find_kth(arr1, arr2, m, n, k) == expected

def test_find_1st_smallest_element_different_length_arrays():
    arr1 = [10, 20, 30]
    arr2 = [5, 15]
    m = 3
    n = 2
    k = 1
    expected = 5
    assert find_kth(arr1, arr2, m, n, k) == expected

def test_find_5th_smallest_element_k_equals_total_length():
    arr1 = [1, 2, 3]
    arr2 = [4, 5]
    m = 3
    n = 2
    k = 5
    expected = 5
    assert find_kth(arr1, arr2, m, n, k) == expected

def test_find_4th_smallest_element_overlapping_values():
    arr1 = [1, 4, 7]
    arr2 = [2, 4, 6]
    m = 3
    n = 3
    k = 4
    expected = 4
    assert find_kth(arr1, arr2, m, n, k) == expected

def test_find_2nd_smallest_element_one_array_empty():
    arr1 = []
    arr2 = [1, 2, 3]
    m = 0
    n = 3
    k = 2
    expected = 2
    assert find_kth(arr1, arr2, m, n, k) == expected

def test_find_6th_smallest_element_arrays_with_duplicates():
    arr1 = [1, 2, 2, 3]
    arr2 = [2, 2, 4]
    m = 4
    n = 3
    k = 6
    expected = 3
    assert find_kth(arr1, arr2, m, n, k) == expected