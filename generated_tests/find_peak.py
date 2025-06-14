def find_peak_util(arr, low, high, n): 
	mid = low + (high - low)/2
	mid = int(mid) 
	if ((mid == 0 or arr[mid - 1] <= arr[mid]) and
		(mid == n - 1 or arr[mid + 1] <= arr[mid])): 
		return mid 
	elif (mid > 0 and arr[mid - 1] > arr[mid]): 
		return find_peak_util(arr, low, (mid - 1), n) 
	else: 
		return find_peak_util(arr, (mid + 1), high, n) 
def find_peak(arr, n): 
	return find_peak_util(arr, 0, n - 1, n)

import pytest

def test_find_peak_single_element_array():
    arr = [5]
    n = 1
    expected_output = 0
    assert find_peak(arr, n) == expected_output

def test_find_peak_ascending_array():
    arr = [1, 2, 3, 4, 5]
    n = 5
    expected_output = 4
    assert find_peak(arr, n) == expected_output

def test_find_peak_descending_array():
    arr = [5, 4, 3, 2, 1]
    n = 5
    expected_output = 0
    assert find_peak(arr, n) == expected_output

def test_find_peak_multiple_peaks():
    arr = [1, 3, 2, 4, 3]
    n = 5
    expected_output = 1
    assert find_peak(arr, n) == expected_output

def test_find_peak_middle_peak():
    arr = [1, 2, 5, 3, 1]
    n = 5
    expected_output = 2
    assert find_peak(arr, n) == expected_output

def test_find_peak_plateau_peak():
    arr = [1, 2, 2, 2, 1]
    n = 5
    expected_output = 3
    assert find_peak(arr, n) == expected_output

def test_find_peak_all_equal_elements():
    arr = [2, 2, 2, 2, 2]
    n = 5
    expected_output = 2
    assert find_peak(arr, n) == expected_output