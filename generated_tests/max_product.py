def max_product(arr, n ): 
	mpis =[0] * (n) 
	for i in range(n): 
		mpis[i] = arr[i] 
	for i in range(1, n): 
		for j in range(i): 
			if (arr[i] > arr[j] and
					mpis[i] < (mpis[j] * arr[i])): 
						mpis[i] = mpis[j] * arr[i] 
	return max(mpis)

import pytest

def test_all_positive_increasing_numbers():
    arr = [1, 2, 3, 4]
    n = 4
    expected = 24
    assert max_product(arr, n) == expected

def test_array_with_decreasing_numbers():
    arr = [4, 3, 2, 1]
    n = 4
    expected = 4
    assert max_product(arr, n) == expected

def test_array_with_mixed_positive_numbers():
    arr = [3, 100, 4, 5, 150, 6]
    n = 6
    expected = 45000
    assert max_product(arr, n) == expected

def test_array_with_negative_and_positive_numbers():
    arr = [-1, -2, -3, 4, 5]
    n = 5
    expected = 20
    assert max_product(arr, n) == expected

def test_array_with_zeros_and_positives():
    arr = [0, 2, 0, 3, 4]
    n = 5
    expected = 24
    assert max_product(arr, n) == expected

def test_single_element_array():
    arr = [10]
    n = 1
    expected = 10
    assert max_product(arr, n) == expected

def test_array_with_repeated_elements():
    arr = [2, 2, 2, 2]
    n = 4
    expected = 2
    assert max_product(arr, n) == expected