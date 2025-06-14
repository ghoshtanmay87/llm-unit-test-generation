def max_fill(grid, capacity):
    import math
    '\n    You are given a rectangular grid of wells. Each row represents a single well,\n    and each 1 in a row represents a single unit of water.\n    Each well has a corresponding bucket that can be used to extract water from it, \n    and all buckets have the same capacity.\n    Your task is to use the buckets to empty the wells.\n    Output the number of times you need to lower the buckets.\n\n    Example 1:\n        Input: \n            grid : [[0,0,1,0], [0,1,0,0], [1,1,1,1]]\n            bucket_capacity : 1\n        Output: 6\n\n    Example 2:\n        Input: \n            grid : [[0,0,1,1], [0,0,0,0], [1,1,1,1], [0,1,1,1]]\n            bucket_capacity : 2\n        Output: 5\n    \n    Example 3:\n        Input: \n            grid : [[0,0,0], [0,0,0]]\n            bucket_capacity : 5\n        Output: 0\n\n    Constraints:\n        * all wells have the same length\n        * 1 <= grid.length <= 10^2\n        * 1 <= grid[:,1].length <= 10^2\n        * grid[i][j] -> 0 | 1\n        * 1 <= capacity <= 10\n    '
    return sum([math.ceil(sum(arr) / capacity) for arr in grid])

import pytest

def test_single_well_with_one_unit_and_capacity_1():
    """Test with a single well having one unit of water and bucket capacity 1"""
    grid = [[1]]
    capacity = 1
    expected_output = 1
    assert max_fill(grid, capacity) == expected_output

def test_multiple_wells_with_varying_water_and_capacity_2():
    """Test with multiple wells, some empty and some with water, and bucket capacity 2"""
    grid = [[0, 0, 1, 1], [0, 0, 0, 0], [1, 1, 1, 1], [0, 1, 1, 1]]
    capacity = 2
    expected_output = 5
    assert max_fill(grid, capacity) == expected_output

def test_all_wells_empty_and_capacity_5():
    """Test with all wells empty and bucket capacity 5"""
    grid = [[0, 0, 0], [0, 0, 0]]
    capacity = 5
    expected_output = 0
    assert max_fill(grid, capacity) == expected_output

def test_wells_with_varying_water_and_capacity_3():
    """Test with wells having varying amounts of water and bucket capacity 3"""
    grid = [[1, 1, 1], [1, 1, 0], [0, 0, 0], [1, 1, 1]]
    capacity = 3
    expected_output = 3
    assert max_fill(grid, capacity) == expected_output

def test_single_well_with_more_water_than_bucket_capacity():
    """Test with a single well having more water than the bucket capacity"""
    grid = [[1, 1, 1, 1, 1]]
    capacity = 2
    expected_output = 3
    assert max_fill(grid, capacity) == expected_output