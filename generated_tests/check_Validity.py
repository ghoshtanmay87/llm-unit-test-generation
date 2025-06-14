def check_Validity(a,b,c):  
    if (a + b <= c) or (a + c <= b) or (b + c <= a) : 
        return False
    else: 
        return True

import pytest

def test_all_sides_satisfy_triangle_inequality():
    # All sides satisfy triangle inequality (3, 4, 5)
    a, b, c = 3, 4, 5
    expected = True
    assert check_Validity(a, b, c) == expected

def test_sum_of_two_sides_equals_third_side():
    # Sum of two sides equals the third side (1, 2, 3)
    a, b, c = 1, 2, 3
    expected = False
    assert check_Validity(a, b, c) == expected

def test_sum_of_two_sides_less_than_third_side():
    # Sum of two sides less than the third side (2, 2, 5)
    a, b, c = 2, 2, 5
    expected = False
    assert check_Validity(a, b, c) == expected

def test_all_sides_equal_and_positive():
    # All sides equal and positive (5, 5, 5)
    a, b, c = 5, 5, 5
    expected = True
    assert check_Validity(a, b, c) == expected

def test_one_side_zero():
    # One side zero (0, 4, 5)
    a, b, c = 0, 4, 5
    expected = False
    assert check_Validity(a, b, c) == expected