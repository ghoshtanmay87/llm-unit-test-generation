def find_triplet_array(A, arr_size, sum): 
	for i in range( 0, arr_size-2): 
		for j in range(i + 1, arr_size-1): 
			for k in range(j + 1, arr_size): 
				if A[i] + A[j] + A[k] == sum: 
					return  A[i],A[j],A[k] 
					return True
	return False

import pytest

def test_find_triplet_small_array():
    A = [1, 2, 3, 4, 5]
    arr_size = 5
    sum_value = 9
    expected = (1, 3, 5)
    assert find_triplet_array(A, arr_size, sum_value) == expected

def test_no_triplet_sums_to_target():
    A = [1, 2, 4, 5]
    arr_size = 4
    sum_value = 50
    expected = False
    assert find_triplet_array(A, arr_size, sum_value) == expected

def test_triplet_with_negative_numbers():
    A = [-1, 0, 1, 2]
    arr_size = 4
    sum_value = 0
    expected = (-1, 0, 1)
    assert find_triplet_array(A, arr_size, sum_value) == expected

def test_array_exactly_three_elements():
    A = [3, 3, 3]
    arr_size = 3
    sum_value = 9
    expected = (3, 3, 3)
    assert find_triplet_array(A, arr_size, sum_value) == expected

def test_multiple_triplets_returns_first_found():
    A = [1, 2, 3, 4, 5, 6]
    arr_size = 6
    sum_value = 12
    expected = (1, 5, 6)
    assert find_triplet_array(A, arr_size, sum_value) == expected

def test_array_with_no_elements():
    A = []
    arr_size = 0
    sum_value = 0
    expected = False
    assert find_triplet_array(A, arr_size, sum_value) == expected

def test_array_with_less_than_three_elements():
    A = [1, 2]
    arr_size = 2
    sum_value = 3
    expected = False
    assert find_triplet_array(A, arr_size, sum_value) == expected