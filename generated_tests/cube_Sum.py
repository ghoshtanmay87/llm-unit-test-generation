def cube_Sum(n): 
    sum = 0
    for i in range(1,n + 1): 
        sum += (2*i)*(2*i)*(2*i) 
    return sum

import pytest

def test_cube_sum_n_1():
    # For n=1, the loop runs once with i=1. The term is (2*1)^3 = 2^3 = 8. Sum is 8.
    assert cube_Sum(1) == 8

def test_cube_sum_n_2():
    # For n=2, terms are (2*1)^3 = 8 and (2*2)^3 = 64. Sum is 8 + 64 = 72.
    assert cube_Sum(2) == 72

def test_cube_sum_n_3():
    # For n=3, terms are 8, 64, and (2*3)^3 = 6^3 = 216. Sum is 8 + 64 + 216 = 288.
    assert cube_Sum(3) == 216

def test_cube_sum_n_0():
    # For n=0, the loop does not run, so sum remains 0.
    assert cube_Sum(0) == 0

def test_cube_sum_n_4():
    # For n=4, terms are 8, 64, 216, and (2*4)^3 = 8^3 = 512. Sum is 8 + 64 + 216 + 512 = 800.
    assert cube_Sum(4) == 512