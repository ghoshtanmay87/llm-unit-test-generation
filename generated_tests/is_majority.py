def is_majority(arr, n, x):
	i = binary_search(arr, 0, n-1, x)
	if i == -1:
		return False
	if ((i + n//2) <= (n -1)) and arr[i + n//2] == x:
		return True
	else:
		return False
def binary_search(arr, low, high, x):
	if high >= low:
		mid = (low + high)//2 
		if (mid == 0 or x > arr[mid-1]) and (arr[mid] == x):
			return mid
		elif x > arr[mid]:
			return binary_search(arr, (mid + 1), high, x)
		else:
			return binary_search(arr, low, (mid -1), x)
	return -1

import pytest

def test_element_not_present_in_array():
    arr = [1, 2, 3, 4, 5]
    n = 5
    x = 6
    assert is_majority(arr, n, x) is False

def test_element_appears_exactly_half_not_majority():
    arr = [1, 2, 2, 3, 4]
    n = 5
    x = 2
    assert is_majority(arr, n, x) is False

def test_element_appears_more_than_half_is_majority():
    arr = [1, 2, 2, 2, 3]
    n = 5
    x = 2
    assert is_majority(arr, n, x) is True

def test_element_appears_once_in_single_element_array():
    arr = [7]
    n = 1
    x = 7
    assert is_majority(arr, n, x) is True

def test_element_multiple_times_not_majority_even_length():
    arr = [1, 1, 2, 2, 3, 3]
    n = 6
    x = 2
    assert is_majority(arr, n, x) is False

def test_element_majority_even_length_array():
    arr = [1, 2, 2, 2, 2, 3]
    n = 6
    x = 2
    assert is_majority(arr, n, x) is True

def test_element_at_end_is_majority():
    arr = [1, 1, 1, 2, 2, 2, 2, 2]
    n = 8
    x = 2
    assert is_majority(arr, n, x) is True

def test_element_at_start_is_majority():
    arr = [3, 3, 3, 3, 4, 5, 6]
    n = 7
    x = 3
    assert is_majority(arr, n, x) is True

def test_element_appears_less_than_half():
    arr = [1, 1, 2, 3, 4, 5, 6]
    n = 7
    x = 1
    assert is_majority(arr, n, x) is False

def test_empty_array_input():
    arr = []
    n = 0
    x = 1
    assert is_majority(arr, n, x) is False