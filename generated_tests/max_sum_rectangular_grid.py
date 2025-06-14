def max_sum_rectangular_grid(grid, n) : 
	incl = max(grid[0][0], grid[1][0]) 
	excl = 0
	for i in range(1, n) : 
		excl_new = max(excl, incl) 
		incl = excl + max(grid[0][i], grid[1][i]) 
		excl = excl_new 
	return max(excl, incl)

import pytest

def test_two_columns_with_positive_values():
    grid = [[1, 2], [3, 4]]
    n = 2
    expected = 7
    result = max_sum_rectangular_grid(grid, n)
    assert result == expected, f"Expected {expected} but got {result}"

def test_single_column_with_positive_values():
    grid = [[5], [10]]
    n = 1
    expected = 10
    result = max_sum_rectangular_grid(grid, n)
    assert result == expected, f"Expected {expected} but got {result}"

def test_three_columns_with_mixed_values():
    grid = [[1, 2, 9], [3, 4, 1]]
    n = 3
    expected = 12
    result = max_sum_rectangular_grid(grid, n)
    assert result == expected, f"Expected {expected} but got {result}"

def test_all_negative_values():
    grid = [[-1, -2, -3], [-4, -5, -6]]
    n = 3
    expected = -1
    result = max_sum_rectangular_grid(grid, n)
    assert result == expected, f"Expected {expected} but got {result}"

def test_four_columns_with_alternating_high_values():
    grid = [[10, 1, 10, 1], [1, 10, 1, 10]]
    n = 4
    expected = 30
    result = max_sum_rectangular_grid(grid, n)
    assert result == expected, f"Expected {expected} but got {result}"