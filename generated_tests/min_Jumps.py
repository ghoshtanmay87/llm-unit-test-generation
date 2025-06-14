def min_Jumps(a, b, d): 
    temp = a 
    a = min(a, b) 
    b = max(temp, b) 
    if (d >= b): 
        return (d + b - 1) / b 
    if (d == 0): 
        return 0
    if (d == a): 
        return 1
    else:
        return 2

import pytest

def test_distance_greater_than_or_equal_max_of_a_b():
    # Distance greater than or equal to the maximum of a and b
    a = 2
    b = 5
    d = 10
    expected = 2.8
    assert min_Jumps(a, b, d) == expected

def test_distance_is_zero():
    # Distance is zero
    a = 3
    b = 7
    d = 0
    expected = 0
    assert min_Jumps(a, b, d) == expected

def test_distance_equals_min_of_a_b():
    # Distance equals the minimum of a and b
    a = 4
    b = 6
    d = 4
    expected = 1
    assert min_Jumps(a, b, d) == expected

def test_distance_less_than_min_and_not_zero():
    # Distance less than minimum of a and b and not zero
    a = 5
    b = 10
    d = 3
    expected = 2
    assert min_Jumps(a, b, d) == expected

def test_distance_between_min_and_max_of_a_b():
    # Distance between minimum and maximum of a and b
    a = 3
    b = 8
    d = 5
    expected = 2
    assert min_Jumps(a, b, d) == expected