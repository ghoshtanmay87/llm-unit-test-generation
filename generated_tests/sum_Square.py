def sum_Square(n) : 
    i = 1 
    while i*i <= n : 
        j = 1
        while (j*j <= n) : 
            if (i*i+j*j == n) : 
                return True
            j = j+1
        i = i+1     
    return False

import pytest

def test_sum_square_with_5():
    # Check if 5 can be expressed as the sum of squares of two integers
    n = 5
    expected = True
    assert sum_Square(n) == expected

def test_sum_square_with_3():
    # Check if 3 can be expressed as the sum of squares of two integers
    n = 3
    expected = False
    assert sum_Square(n) == expected

def test_sum_square_with_50():
    # Check if 50 can be expressed as the sum of squares of two integers
    n = 50
    expected = True
    assert sum_Square(n) == expected

def test_sum_square_with_1():
    # Check if 1 can be expressed as the sum of squares of two integers
    n = 1
    expected = False
    assert sum_Square(n) == expected

def test_sum_square_with_2():
    # Check if 2 can be expressed as the sum of squares of two integers
    n = 2
    expected = True
    assert sum_Square(n) == expected

def test_sum_square_with_0():
    # Check if 0 can be expressed as the sum of squares of two integers
    n = 0
    expected = False
    assert sum_Square(n) == expected