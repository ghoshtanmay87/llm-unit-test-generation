def multiply_int(x, y):
    if y < 0:
        return -multiply_int(x, -y)
    elif y == 0:
        return 0
    elif y == 1:
        return x
    else:
        return x + multiply_int(x, y - 1)

import pytest

def test_multiplying_two_positive_integers():
    # Since y=4 > 1, the function recursively adds x=3 four times: 3 + 3 + 3 + 3 = 12.
    assert multiply_int(3, 4) == 12

def test_multiplying_by_zero():
    # When y=0, the function returns 0 immediately as per the base case.
    assert multiply_int(5, 0) == 0

def test_multiplying_by_one():
    # When y=1, the function returns x directly, so output is 7.
    assert multiply_int(7, 1) == 7

def test_multiplying_by_negative_integer():
    # Since y is negative, the function calls itself with y=3 and negates the result.
    # multiply_int(4, 3) = 12, so final output is -12.
    assert multiply_int(4, -3) == -12

def test_multiplying_zero_by_positive_integer():
    # Multiplying zero by any number results in zero.
    # The function adds zero five times, resulting in 0.
    assert multiply_int(0, 5) == 0

def test_multiplying_positive_integer_by_large_positive_integer():
    # The function adds 2 ten times: 2 * 10 = 20.
    assert multiply_int(2, 10) == 20

def test_multiplying_negative_integer_by_negative_integer():
    # Since y is negative, the function calls multiply_int(-3, 2) and negates the result.
    # multiply_int(-3, 2) = -6, negated is 6.
    assert multiply_int(-3, -2) == 6