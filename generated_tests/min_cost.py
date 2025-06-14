R = 3
C = 3
def min_cost(cost, m, n): 
	tc = [[0 for x in range(C)] for x in range(R)] 
	tc[0][0] = cost[0][0] 
	for i in range(1, m+1): 
		tc[i][0] = tc[i-1][0] + cost[i][0] 
	for j in range(1, n+1): 
		tc[0][j] = tc[0][j-1] + cost[0][j] 
	for i in range(1, m+1): 
		for j in range(1, n+1): 
			tc[i][j] = min(tc[i-1][j-1], tc[i-1][j], tc[i][j-1]) + cost[i][j] 
	return tc[m][n]

import pytest

def test_min_cost_path_to_bottom_right_corner_3x3():
    cost = [[1, 2, 3], [4, 8, 2], [1, 5, 3]]
    m = 2
    n = 2
    expected = 8
    assert min_cost(cost, m, n) == expected

def test_min_cost_path_to_middle_cell_11_3x3():
    cost = [[1, 2, 3], [4, 8, 2], [1, 5, 3]]
    m = 1
    n = 1
    expected = 9
    assert min_cost(cost, m, n) == expected

def test_min_cost_path_to_cell_02_top_row_3x3():
    cost = [[1, 2, 3], [4, 8, 2], [1, 5, 3]]
    m = 0
    n = 2
    expected = 6
    assert min_cost(cost, m, n) == expected

def test_min_cost_path_to_cell_20_left_column_3x3():
    cost = [[1, 2, 3], [4, 8, 2], [1, 5, 3]]
    m = 2
    n = 0
    expected = 6
    assert min_cost(cost, m, n) == expected

def test_min_cost_path_2x2_uniform_costs():
    cost = [[1, 1], [1, 1]]
    m = 1
    n = 1
    expected = 2
    assert min_cost(cost, m, n) == expected

def test_min_cost_path_1x1_single_cell():
    cost = [[5]]
    m = 0
    n = 0
    expected = 5
    assert min_cost(cost, m, n) == expected