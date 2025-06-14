def find_ind(key, i, n, 
			k, arr):
	ind = -1
	start = i + 1
	end = n - 1;
	while (start < end):
		mid = int(start +
				(end - start) / 2)
		if (arr[mid] - key <= k):
			ind = mid
			start = mid + 1
		else:
			end = mid
	return ind
def removals(arr, n, k):
	ans = n - 1
	arr.sort()
	for i in range(0, n):
		j = find_ind(arr[i], i, 
					n, k, arr)
		if (j != -1):
			ans = min(ans, n -
						(j - i + 1))
	return ans

import pytest

def test_all_elements_same_k_zero_no_removals():
    arr = [5, 5, 5, 5]
    n = 4
    k = 0
    expected = 0
    assert removals(arr, n, k) == expected

def test_increasing_elements_k_two_some_removals():
    arr = [1, 3, 6, 10]
    n = 4
    k = 2
    expected = 2
    assert removals(arr, n, k) == expected

def test_all_elements_within_k_no_removals():
    arr = [2, 4, 5, 6]
    n = 4
    k = 4
    expected = 0
    assert removals(arr, n, k) == expected

def test_large_gaps_k_one_many_removals():
    arr = [1, 10, 20, 30]
    n = 4
    k = 1
    expected = 3
    assert removals(arr, n, k) == expected

def test_single_element_array_no_removals():
    arr = [100]
    n = 1
    k = 0
    expected = 0
    assert removals(arr, n, k) == expected