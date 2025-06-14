def get_maxgold(gold, m, n): 
    goldTable = [[0 for i in range(n)] 
                        for j in range(m)]   
    for col in range(n-1, -1, -1): 
        for row in range(m):  
            if (col == n-1): 
                right = 0
            else: 
                right = goldTable[row][col+1] 
            if (row == 0 or col == n-1): 
                right_up = 0
            else: 
                right_up = goldTable[row-1][col+1] 
            if (row == m-1 or col == n-1): 
                right_down = 0
            else: 
                right_down = goldTable[row+1][col+1] 
            goldTable[row][col] = gold[row][col] + max(right, right_up, right_down) 
    res = goldTable[0][0] 
    for i in range(1, m): 
        res = max(res, goldTable[i][0])  
    return res

import pytest

def test_single_cell_grid_with_one_gold_value():
    gold = [[5]]
    m = 1
    n = 1
    expected = 5
    assert get_maxgold(gold, m, n) == expected

def test_single_row_with_multiple_columns():
    gold = [[1, 3, 3]]
    m = 1
    n = 3
    expected = 7
    assert get_maxgold(gold, m, n) == expected

def test_two_rows_two_columns_with_varied_gold():
    gold = [[1, 3], [2, 1]]
    m = 2
    n = 2
    expected = 5
    assert get_maxgold(gold, m, n) == expected

def test_three_rows_three_columns_with_mixed_values():
    gold = [[1, 3, 1], [2, 1, 4], [0, 6, 4]]
    m = 3
    n = 3
    expected = 12
    assert get_maxgold(gold, m, n) == expected

def test_all_zero_gold_values_in_2x3_grid():
    gold = [[0, 0, 0], [0, 0, 0]]
    m = 2
    n = 3
    expected = 0
    assert get_maxgold(gold, m, n) == expected