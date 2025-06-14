def check_last (arr,n,p): 
    _sum = 0
    for i in range(n): 
        _sum = _sum + arr[i] 
    if p == 1: 
        if _sum % 2 == 0: 
            return "ODD"
        else: 
            return "EVEN"
    return "EVEN"

import pytest

def test_sum_even_p_is_1_returns_ODD():
    # Sum of first 3 elements is 6 (even), p=1, expect "ODD"
    arr = [1, 2, 3, 4]
    n = 3
    p = 1
    assert check_last(arr, n, p) == "ODD"

def test_sum_odd_p_is_1_returns_EVEN():
    # Sum of first 2 elements is 3 (odd), p=1, expect "EVEN"
    arr = [1, 2, 3, 4]
    n = 2
    p = 1
    assert check_last(arr, n, p) == "EVEN"

def test_p_not_1_sum_even_returns_EVEN():
    # Sum of first 3 elements is 12 (even), p=0, expect "EVEN"
    arr = [2, 4, 6]
    n = 3
    p = 0
    assert check_last(arr, n, p) == "EVEN"

def test_p_not_1_sum_odd_returns_EVEN():
    # Sum of first 3 elements is 9 (odd), p=2, expect "EVEN"
    arr = [1, 3, 5]
    n = 3
    p = 2
    assert check_last(arr, n, p) == "EVEN"

def test_empty_array_n_0_p_1_returns_ODD():
    # Sum of first 0 elements is 0 (even), p=1, expect "ODD"
    arr = []
    n = 0
    p = 1
    assert check_last(arr, n, p) == "ODD"