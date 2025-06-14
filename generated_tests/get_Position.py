import math as mt 
def get_Position(a,n,m): 
    for i in range(n): 
        a[i] = (a[i] // m + (a[i] % m != 0))  
    result,maxx = -1,-1
    for i in range(n - 1,-1,-1): 
        if (maxx < a[i]): 
            maxx = a[i] 
            result = i 
    return result + 1

import pytest

def test_single_element_exactly_divisible_by_m():
    a = [10]
    n = 1
    m = 5
    assert get_Position(a, n, m) == 1

def test_single_element_not_exactly_divisible_by_m():
    a = [11]
    n = 1
    m = 5
    assert get_Position(a, n, m) == 1

def test_multiple_elements_with_distinct_ceil_divisions():
    a = [10, 11, 12]
    n = 3
    m = 5
    assert get_Position(a, n, m) == 3

def test_multiple_elements_with_same_ceil_division_values():
    a = [5, 5, 5]
    n = 3
    m = 5
    assert get_Position(a, n, m) == 3

def test_elements_with_zero_values():
    a = [0, 0, 0]
    n = 3
    m = 5
    assert get_Position(a, n, m) == 3

def test_mixed_values_with_some_zero_and_some_positive():
    a = [0, 5, 10]
    n = 3
    m = 5
    assert get_Position(a, n, m) == 3

def test_large_values_with_remainder():
    a = [1000, 1001, 999]
    n = 3
    m = 1000
    assert get_Position(a, n, m) == 2

def test_all_elements_zero_with_m_1():
    a = [0, 0, 0]
    n = 3
    m = 1
    assert get_Position(a, n, m) == 3

def test_single_element_less_than_m():
    a = [3]
    n = 1
    m = 5
    assert get_Position(a, n, m) == 1

def test_multiple_elements_with_decreasing_values():
    a = [15, 10, 5]
    n = 3
    m = 5
    assert get_Position(a, n, m) == 1