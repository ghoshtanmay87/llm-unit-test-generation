def coin_change(S, m, n): 
    table = [[0 for x in range(m)] for x in range(n+1)] 
    for i in range(m): 
        table[0][i] = 1
    for i in range(1, n+1): 
        for j in range(m): 
            x = table[i - S[j]][j] if i-S[j] >= 0 else 0
            y = table[i][j-1] if j >= 1 else 0 
            table[i][j] = x + y   
    return table[n][m-1]

import pytest

def test_ways_to_make_zero_with_any_coins():
    S = [1, 2, 3]
    m = 3
    n = 0
    expected = 1
    assert coin_change(S, m, n) == expected

def test_ways_to_make_4_with_coins_1_2_3():
    S = [1, 2, 3]
    m = 3
    n = 4
    expected = 4
    assert coin_change(S, m, n) == expected

def test_ways_to_make_5_with_coins_1_2_5():
    S = [1, 2, 5]
    m = 3
    n = 5
    expected = 4
    assert coin_change(S, m, n) == expected

def test_ways_to_make_3_with_coin_2_only():
    S = [2]
    m = 1
    n = 3
    expected = 0
    assert coin_change(S, m, n) == expected

def test_ways_to_make_10_with_coins_2_5_3_6():
    S = [2, 5, 3, 6]
    m = 4
    n = 10
    expected = 5
    assert coin_change(S, m, n) == expected