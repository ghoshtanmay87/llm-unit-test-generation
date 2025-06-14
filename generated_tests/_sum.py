def _sum(arr):  
    sum=0
    for i in arr: 
        sum = sum + i      
    return(sum)

import pytest

def test_sum_empty_list():
    # Sum of an empty list
    arr = []
    expected = 0
    assert _sum(arr) == expected

def test_sum_positive_integers():
    # Sum of a list with positive integers
    arr = [1, 2, 3, 4, 5]
    expected = 15
    assert _sum(arr) == expected

def test_sum_negative_and_positive_integers():
    # Sum of a list with negative and positive integers
    arr = [-1, 2, -3, 4]
    expected = 2
    assert _sum(arr) == expected

def test_sum_floating_point_numbers():
    # Sum of a list with floating point numbers
    arr = [1.5, 2.5, 3.0]
    expected = 7.0
    assert _sum(arr) == expected

def test_sum_single_element():
    # Sum of a list with a single element
    arr = [42]
    expected = 42
    assert _sum(arr) == expected