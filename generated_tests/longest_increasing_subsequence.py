def longest_increasing_subsequence(arr): 
	n = len(arr) 
	longest_increasing_subsequence = [1]*n 
	for i in range (1 , n): 
		for j in range(0 , i): 
			if arr[i] > arr[j] and longest_increasing_subsequence[i]< longest_increasing_subsequence[j] + 1 : 
				longest_increasing_subsequence[i] = longest_increasing_subsequence[j]+1
	maximum = 0
	for i in range(n): 
		maximum = max(maximum , longest_increasing_subsequence[i]) 
	return maximum

import pytest

def test_empty_list_input():
    arr = []
    expected = 0
    assert longest_increasing_subsequence(arr) == expected

def test_single_element_list():
    arr = [10]
    expected = 1
    assert longest_increasing_subsequence(arr) == expected

def test_strictly_increasing_list():
    arr = [1, 2, 3, 4, 5]
    expected = 5
    assert longest_increasing_subsequence(arr) == expected

def test_strictly_decreasing_list():
    arr = [5, 4, 3, 2, 1]
    expected = 1
    assert longest_increasing_subsequence(arr) == expected

def test_list_with_repeated_elements():
    arr = [2, 2, 2, 2]
    expected = 1
    assert longest_increasing_subsequence(arr) == expected

def test_mixed_increasing_and_decreasing_elements():
    arr = [10, 22, 9, 33, 21, 50, 41, 60]
    expected = 5
    assert longest_increasing_subsequence(arr) == expected

def test_list_with_multiple_increasing_subsequences():
    arr = [3, 10, 2, 1, 20]
    expected = 3
    assert longest_increasing_subsequence(arr) == expected

def test_list_with_negative_and_positive_numbers():
    arr = [-1, 0, 1, 2, -1, 3]
    expected = 5
    assert longest_increasing_subsequence(arr) == expected

def test_list_with_alternating_increase_and_decrease():
    arr = [1, 3, 2, 4, 3, 5]
    expected = 4
    assert longest_increasing_subsequence(arr) == expected