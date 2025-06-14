def min_sum_path(A): 
	memo = [None] * len(A) 
	n = len(A) - 1
	for i in range(len(A[n])): 
		memo[i] = A[n][i] 
	for i in range(len(A) - 2, -1,-1): 
		for j in range( len(A[i])): 
			memo[j] = A[i][j] + min(memo[j], 
									memo[j + 1]) 
	return memo[0]

import pytest

def test_min_sum_path_simple_triangle_three_rows():
    A = [[2], [3, 4], [6, 5, 7]]
    expected = 10
    assert min_sum_path(A) == expected

def test_min_sum_path_triangle_four_rows():
    A = [[1], [2, 3], [3, 6, 7], [4, 1, 8, 3]]
    expected = 7
    assert min_sum_path(A) == expected

def test_min_sum_path_single_row():
    A = [[5]]
    expected = 5
    assert min_sum_path(A) == expected

def test_min_sum_path_two_rows():
    A = [[1], [2, 3]]
    expected = 3
    assert min_sum_path(A) == expected

def test_min_sum_path_with_negative_numbers():
    A = [[-1], [2, 3], [1, -1, -3]]
    expected = -1
    assert min_sum_path(A) == expected

def test_min_sum_path_all_zeros():
    A = [[0], [0, 0], [0, 0, 0]]
    expected = 0
    assert min_sum_path(A) == expected