import sys 
def min_coins(coins, m, V): 
    if (V == 0): 
        return 0
    res = sys.maxsize 
    for i in range(0, m): 
        if (coins[i] <= V): 
            sub_res = min_coins(coins, m, V-coins[i]) 
            if (sub_res != sys.maxsize and sub_res + 1 < res): 
                res = sub_res + 1  
    return res

import pytest
import sys

def test_min_coins_V11_coins_1_2_5():
    # Calculate minimum coins for V=11 with coins [1, 2, 5]
    coins = [1, 2, 5]
    m = 3
    V = 11
    expected = 3
    assert min_coins(coins, m, V) == expected

def test_min_coins_V3_coins_2_no_solution():
    # Calculate minimum coins for V=3 with coins [2]
    coins = [2]
    m = 1
    V = 3
    expected = 9223372036854775807
    assert min_coins(coins, m, V) == expected

def test_min_coins_V0_any_coins():
    # Calculate minimum coins for V=0 with any coins
    coins = [1, 2, 5]
    m = 3
    V = 0
    expected = 0
    assert min_coins(coins, m, V) == expected

def test_min_coins_V7_coins_1_3_4_5():
    # Calculate minimum coins for V=7 with coins [1, 3, 4, 5]
    coins = [1, 3, 4, 5]
    m = 4
    V = 7
    expected = 2
    assert min_coins(coins, m, V) == expected

def test_min_coins_V10_coins_2_5_3_6():
    # Calculate minimum coins for V=10 with coins [2, 5, 3, 6]
    coins = [2, 5, 3, 6]
    m = 4
    V = 10
    expected = 2
    assert min_coins(coins, m, V) == expected