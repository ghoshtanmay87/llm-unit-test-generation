def babylonian_squareroot(number):
    if(number == 0):
        return 0;
    g = number/2.0;
    g2 = g + 1;
    while(g != g2):
        n = number/ g;
        g2 = g;
        g = (g + n)/2;
    return g;

import pytest

def test_square_root_of_zero():
    # Calculate square root of zero
    result = babylonian_squareroot(0)
    assert result == 0

def test_square_root_of_four():
    # Calculate square root of 4
    result = babylonian_squareroot(4)
    assert result == 2.0

def test_square_root_of_nine():
    # Calculate square root of 9
    result = babylonian_squareroot(9)
    assert result == 3.0

def test_square_root_of_two():
    # Calculate square root of 2
    result = babylonian_squareroot(2)
    assert result == 1.4142135623746899

def test_square_root_of_point_two_five():
    # Calculate square root of 0.25
    result = babylonian_squareroot(0.25)
    assert result == 0.5

def test_square_root_of_one():
    # Calculate square root of 1
    result = babylonian_squareroot(1)
    assert result == 1.0