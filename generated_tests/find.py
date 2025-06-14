def find(n,m):  
    q = n//m 
    return (q)

import pytest

def test_divide_10_by_3_integer_division():
    # 10 divided by 3 is 3.333..., integer division truncates the decimal part, so the result is 3.
    assert find(10, 3) == 3

def test_divide_20_by_5_integer_division():
    # 20 divided by 5 is exactly 4, so integer division returns 4.
    assert find(20, 5) == 4

def test_divide_7_by_2_integer_division():
    # 7 divided by 2 is 3.5, integer division truncates the decimal part, so the result is 3.
    assert find(7, 2) == 3

def test_divide_0_by_1_integer_division():
    # 0 divided by any non-zero number is 0, so integer division returns 0.
    assert find(0, 1) == 0

def test_divide_15_by_4_integer_division():
    # 15 divided by 4 is 3.75, integer division truncates the decimal part, so the result is 3.
    assert find(15, 4) == 3