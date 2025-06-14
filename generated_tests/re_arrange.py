def right_rotate(arr, n, out_of_place, cur):
	temp = arr[cur]
	for i in range(cur, out_of_place, -1):
		arr[i] = arr[i - 1]
	arr[out_of_place] = temp
	return arr
def re_arrange(arr, n):
	out_of_place = -1
	for index in range(n):
		if (out_of_place >= 0):
			if ((arr[index] >= 0 and arr[out_of_place] < 0) or
			(arr[index] < 0 and arr[out_of_place] >= 0)):
				arr = right_rotate(arr, n, out_of_place, index)
				if (index-out_of_place > 2):
					out_of_place += 2
				else:
					out_of_place = - 1
		if (out_of_place == -1):
			if ((arr[index] >= 0 and index % 2 == 0) or
			 (arr[index] < 0 and index % 2 == 1)):
				out_of_place = index
	return arr

import pytest

def test_rearrange_alternating_pos_neg_starting_positive():
    arr = [1, -2, 3, -4, 5, -6]
    n = 6
    expected = [1, -2, 3, -4, 5, -6]
    assert re_arrange(arr, n) == expected

def test_rearrange_all_positives_followed_by_negatives():
    arr = [1, 2, 3, -4, -5, -6]
    n = 6
    expected = [1, -4, 2, -5, 3, -6]
    assert re_arrange(arr, n) == expected

def test_rearrange_all_negatives_followed_by_positives():
    arr = [-1, -2, -3, 4, 5, 6]
    n = 6
    expected = [-1, 4, -2, 5, -3, 6]
    assert re_arrange(arr, n) == expected

def test_rearrange_mixed_not_alternating():
    arr = [2, 3, -4, -1, 6, -5]
    n = 6
    expected = [2, -4, 3, -1, 6, -5]
    assert re_arrange(arr, n) == expected

def test_rearrange_single_element_positive():
    arr = [10]
    n = 1
    expected = [10]
    assert re_arrange(arr, n) == expected

def test_rearrange_single_element_negative():
    arr = [-10]
    n = 1
    expected = [-10]
    assert re_arrange(arr, n) == expected

def test_rearrange_zeros_and_negatives():
    arr = [0, -1, 2, -3, 4, -5]
    n = 6
    expected = [0, -1, 2, -3, 4, -5]
    assert re_arrange(arr, n) == expected

def test_rearrange_zeros_and_positives_only():
    arr = [0, 1, 2, 3, 4, 5]
    n = 6
    expected = [0, 1, 2, 3, 4, 5]
    assert re_arrange(arr, n) == expected

def test_rearrange_negatives_even_positives_odd():
    arr = [-1, 2, -3, 4, -5, 6]
    n = 6
    expected = [-1, 2, -3, 4, -5, 6]
    assert re_arrange(arr, n) == expected

def test_rearrange_alternating_starting_negative_index_0():
    arr = [-1, 2, -3, 4, -5, 6]
    n = 6
    expected = [-1, 2, -3, 4, -5, 6]
    assert re_arrange(arr, n) == expected