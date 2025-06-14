def Check_Solution(a,b,c) : 
    if ((b*b) - (4*a*c)) > 0 : 
        return ("2 solutions") 
    elif ((b*b) - (4*a*c)) == 0 : 
        return ("1 solution") 
    else : 
        return ("No solutions")

import pytest

def test_two_distinct_real_roots():
    # Quadratic equation with two distinct real roots
    a = 1
    b = 5
    c = 6
    expected = "2 solutions"
    assert Check_Solution(a, b, c) == expected

def test_one_real_repeated_root():
    # Quadratic equation with one real root (repeated root)
    a = 1
    b = 2
    c = 1
    expected = "1 solution"
    assert Check_Solution(a, b, c) == expected

def test_no_real_roots():
    # Quadratic equation with no real roots
    a = 1
    b = 0
    c = 1
    expected = "No solutions"
    assert Check_Solution(a, b, c) == expected

def test_zero_coefficient_b_positive_discriminant():
    # Quadratic equation with zero coefficient b and positive discriminant
    a = 1
    b = 4
    c = 3
    expected = "2 solutions"
    assert Check_Solution(a, b, c) == expected

def test_zero_coefficient_a_not_quadratic():
    # Quadratic equation with zero coefficient a (not a quadratic)
    a = 0
    b = 2
    c = 1
    expected = "2 solutions"
    assert Check_Solution(a, b, c) == expected