def prod_Square(n):
    for i in range(2,(n) + 1):
        if (i*i < (n+1)):
            for j in range(2,n + 1):
                if ((i*i*j*j) == n):
                    return True;
    return False;

import pytest

def test_prod_square_36_true():
    # Check if 36 can be expressed as the product of squares of two integers >= 2
    n = 36
    expected = True
    assert prod_Square(n) == expected

def test_prod_square_18_false():
    # Check if 18 can be expressed as the product of squares of two integers >= 2
    n = 18
    expected = False
    assert prod_Square(n) == expected

def test_prod_square_100_true():
    # Check if 100 can be expressed as the product of squares of two integers >= 2
    n = 100
    expected = True
    assert prod_Square(n) == expected

def test_prod_square_1_false():
    # Check if 1 can be expressed as the product of squares of two integers >= 2
    n = 1
    expected = False
    assert prod_Square(n) == expected

def test_prod_square_16_true():
    # Check if 16 can be expressed as the product of squares of two integers >= 2
    n = 16
    expected = True
    assert prod_Square(n) == expected

def test_prod_square_50_false():
    # Check if 50 can be expressed as the product of squares of two integers >= 2
    n = 50
    expected = False
    assert prod_Square(n) == expected