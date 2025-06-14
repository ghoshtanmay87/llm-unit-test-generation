def minimum(a,b):   
    if a <= b: 
        return a 
    else: 
        return b

import pytest

def test_minimum_both_inputs_equal():
    # Both inputs are equal
    a = 5
    b = 5
    expected = 5
    assert minimum(a, b) == expected

def test_minimum_a_less_than_b():
    # a is less than b
    a = 3
    b = 7
    expected = 3
    assert minimum(a, b) == expected

def test_minimum_a_greater_than_b():
    # a is greater than b
    a = 10
    b = 2
    expected = 2
    assert minimum(a, b) == expected

def test_minimum_a_negative_less_than_b():
    # a is negative and less than b
    a = -4
    b = 0
    expected = -4
    assert minimum(a, b) == expected

def test_minimum_b_negative_less_than_a():
    # b is negative and less than a
    a = 1
    b = -1
    expected = -1
    assert minimum(a, b) == expected