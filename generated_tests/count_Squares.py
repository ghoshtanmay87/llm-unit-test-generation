def count_Squares(m,n):
    if(n < m):
        temp = m
        m = n
        n = temp
    return ((m * (m + 1) * (2 * m + 1) / 6 + (n - m) * m * (m + 1) / 2))

import pytest

def test_count_squares_1x1_grid():
    # Counting squares in a 1x1 grid
    m = 1
    n = 1
    expected = 1.0
    assert count_Squares(m, n) == expected

def test_count_squares_2x2_grid():
    # Counting squares in a 2x2 grid
    m = 2
    n = 2
    expected = 5.0
    assert count_Squares(m, n) == expected

def test_count_squares_2x3_grid():
    # Counting squares in a 2x3 grid
    m = 2
    n = 3
    expected = 8.0
    assert count_Squares(m, n) == expected

def test_count_squares_3x2_grid_input_order_swapped():
    # Counting squares in a 3x2 grid (input order swapped)
    m = 3
    n = 2
    expected = 8.0
    assert count_Squares(m, n) == expected

def test_count_squares_3x3_grid():
    # Counting squares in a 3x3 grid
    m = 3
    n = 3
    expected = 14.0
    assert count_Squares(m, n) == expected

def test_count_squares_1x4_grid():
    # Counting squares in a 1x4 grid
    m = 1
    n = 4
    expected = 4.0
    assert count_Squares(m, n) == expected

def test_count_squares_4x1_grid_input_order_swapped():
    # Counting squares in a 4x1 grid (input order swapped)
    m = 4
    n = 1
    expected = 4.0
    assert count_Squares(m, n) == expected