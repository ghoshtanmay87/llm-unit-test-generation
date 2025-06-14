def difference(n) :  
    S = (n*(n + 1))//2;  
    res = S*(S-1);  
    return res;

import pytest

def test_difference_n_1():
    # Calculate difference for n=1
    # For n=1, S = (1*2)//2 = 1. Then res = 1*(1-1) = 0.
    assert difference(1) == 0

def test_difference_n_2():
    # Calculate difference for n=2
    # For n=2, S = (2*3)//2 = 3. Then res = 3*(3-1) = 3*2 = 6.
    assert difference(2) == 6

def test_difference_n_3():
    # Calculate difference for n=3
    # For n=3, S = (3*4)//2 = 6. Then res = 6*(6-1) = 6*5 = 30.
    assert difference(3) == 30

def test_difference_n_5():
    # Calculate difference for n=5
    # For n=5, S = (5*6)//2 = 15. Then res = 15*(15-1) = 15*14 = 210.
    assert difference(5) == 210

def test_difference_n_10():
    # Calculate difference for n=10
    # For n=10, S = (10*11)//2 = 55. Then res = 55*(55-1) = 55*54 = 2970.
    assert difference(10) == 2970