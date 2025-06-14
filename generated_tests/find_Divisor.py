def find_Divisor(x,y):  
    if (x==y): 
        return y 
    return 2

import pytest

def test_find_Divisor_equal_positive_integers():
    # When both inputs are equal positive integers
    x = 5
    y = 5
    expected = 5
    assert find_Divisor(x, y) == expected

def test_find_Divisor_equal_negative_integers():
    # When both inputs are equal negative integers
    x = -3
    y = -3
    expected = -3
    assert find_Divisor(x, y) == expected

def test_find_Divisor_different_positive_integers():
    # When inputs are different positive integers
    x = 4
    y = 7
    expected = 2
    assert find_Divisor(x, y) == expected

def test_find_Divisor_different_negative_integers():
    # When inputs are different negative integers
    x = -2
    y = -5
    expected = 2
    assert find_Divisor(x, y) == expected

def test_find_Divisor_zero_and_positive_integer():
    # When inputs are zero and a positive integer
    x = 0
    y = 3
    expected = 2
    assert find_Divisor(x, y) == expected

def test_find_Divisor_zero_and_zero():
    # When inputs are zero and zero
    x = 0
    y = 0
    expected = 0
    assert find_Divisor(x, y) == expected