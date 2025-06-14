def max_path_sum(tri, m, n): 
	for i in range(m-1, -1, -1): 
		for j in range(i+1): 
			if (tri[i+1][j] > tri[i+1][j+1]): 
				tri[i][j] += tri[i+1][j] 
			else: 
				tri[i][j] += tri[i+1][j+1] 
	return tri[0][0]

import pytest

def test_max_path_sum_simple_triangle():
    tri = [[2], [3, 4], [6, 5, 7]]
    m = 2
    n = 2
    expected = 13
    assert max_path_sum(tri, m, n) == expected

def test_max_path_sum_four_row_triangle():
    tri = [[1], [2, 3], [4, 5, 6], [7, 8, 9, 10]]
    m = 3
    n = 3
    expected = 20
    assert max_path_sum(tri, m, n) == expected

def test_max_path_sum_triangle_with_negative_values():
    tri = [[2], [-1, 3], [4, -5, 6]]
    m = 2
    n = 2
    expected = 11
    assert max_path_sum(tri, m, n) == expected

def test_max_path_sum_single_element_triangle():
    tri = [[5]]
    m = 0
    n = 0
    expected = 5
    assert max_path_sum(tri, m, n) == expected

def test_max_path_sum_all_equal_values():
    tri = [[1], [1, 1], [1, 1, 1]]
    m = 2
    n = 2
    expected = 3
    assert max_path_sum(tri, m, n) == expected