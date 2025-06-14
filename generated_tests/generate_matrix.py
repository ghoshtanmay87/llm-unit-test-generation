def generate_matrix(n):
        if n<=0:
            return [] 
        matrix=[row[:] for row in [[0]*n]*n]        
        row_st=0
        row_ed=n-1        
        col_st=0
        col_ed=n-1
        current=1        
        while (True):
            if current>n*n:
                break
            for c in range (col_st, col_ed+1):
                matrix[row_st][c]=current
                current+=1
            row_st+=1
            for r in range (row_st, row_ed+1):
                matrix[r][col_ed]=current
                current+=1
            col_ed-=1
            for c in range (col_ed, col_st-1, -1):
                matrix[row_ed][c]=current
                current+=1
            row_ed-=1
            for r in range (row_ed, row_st-1, -1):
                matrix[r][col_st]=current
                current+=1
            col_st+=1
        return matrix

import pytest

def test_generate_matrix_zero_size():
    # Generate a 0x0 matrix (edge case with n=0)
    n = 0
    expected = []
    assert generate_matrix(n) == expected

def test_generate_matrix_one_by_one():
    # Generate a 1x1 matrix
    n = 1
    expected = [[1]]
    assert generate_matrix(n) == expected

def test_generate_matrix_two_by_two():
    # Generate a 2x2 matrix
    n = 2
    expected = [[1, 2], [4, 3]]
    assert generate_matrix(n) == expected

def test_generate_matrix_three_by_three():
    # Generate a 3x3 matrix
    n = 3
    expected = [[1, 2, 3], [8, 9, 4], [7, 6, 5]]
    assert generate_matrix(n) == expected

def test_generate_matrix_four_by_four():
    # Generate a 4x4 matrix
    n = 4
    expected = [[1, 2, 3, 4], [12, 13, 14, 5], [11, 16, 15, 6], [10, 9, 8, 7]]
    assert generate_matrix(n) == expected