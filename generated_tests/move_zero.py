def move_zero(num_list):
    a = [0 for i in range(num_list.count(0))]
    x = [ i for i in num_list if i != 0]
    x.extend(a)
    return (x)

import pytest

def test_move_zero_mixed_zeros_and_nonzero_integers():
    num_list = [1, 0, 2, 0, 3]
    expected_output = [1, 2, 3, 0, 0]
    assert move_zero(num_list) == expected_output

def test_move_zero_no_zeros():
    num_list = [4, 5, 6]
    expected_output = [4, 5, 6]
    assert move_zero(num_list) == expected_output

def test_move_zero_all_zeros():
    num_list = [0, 0, 0]
    expected_output = [0, 0, 0]
    assert move_zero(num_list) == expected_output

def test_move_zero_empty_list():
    num_list = []
    expected_output = []
    assert move_zero(num_list) == expected_output

def test_move_zero_zeros_and_negative_numbers():
    num_list = [0, -1, 0, -2, 3]
    expected_output = [-1, -2, 3, 0, 0]
    assert move_zero(num_list) == expected_output

def test_move_zero_zeros_and_floats():
    num_list = [0.0, 1.5, 0.0, 2.5]
    expected_output = [1.5, 2.5, 0.0, 0.0]
    assert move_zero(num_list) == expected_output