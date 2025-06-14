def split_two_parts(list1, L):
    return list1[:L], list1[L:]

import pytest

def test_split_list_L_less_than_length():
    # Split list into two parts where L is less than the length of the list
    result = split_two_parts([1, 2, 3, 4, 5], 3)
    assert result == ([1, 2, 3], [4, 5])

def test_split_list_L_zero():
    # Split list into two parts where L is zero
    result = split_two_parts([10, 20, 30], 0)
    assert result == ([], [10, 20, 30])

def test_split_list_L_equals_length():
    # Split list into two parts where L equals the length of the list
    result = split_two_parts([7, 8, 9], 3)
    assert result == ([7, 8, 9], [])

def test_split_list_L_greater_than_length():
    # Split list into two parts where L is greater than the length of the list
    result = split_two_parts([1, 2], 5)
    assert result == ([1, 2], [])

def test_split_empty_list_L_zero():
    # Split an empty list with L=0
    result = split_two_parts([], 0)
    assert result == ([], [])