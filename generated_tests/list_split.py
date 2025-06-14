def list_split(S, step):
    return [S[i::step] for i in range(step)]

import pytest

def test_split_list_of_integers_step_2():
    # Split a list of integers into 2 sublists by taking every 2nd element starting at index 0 and 1
    input_data = {'S': [1, 2, 3, 4, 5, 6], 'step': 2}
    expected = [[1, 3, 5], [2, 4, 6]]
    assert list_split(**input_data) == expected

def test_split_list_of_characters_step_3():
    # Split a list of characters into 3 sublists by taking every 3rd element starting at indices 0, 1, and 2
    input_data = {'S': ['a', 'b', 'c', 'd', 'e', 'f', 'g'], 'step': 3}
    expected = [['a', 'd', 'g'], ['b', 'e'], ['c', 'f']]
    assert list_split(**input_data) == expected

def test_split_empty_list_step_4():
    # Split an empty list with step 4 returns 4 empty sublists
    input_data = {'S': [], 'step': 4}
    expected = [[], [], [], []]
    assert list_split(**input_data) == expected

def test_split_list_fewer_elements_than_step():
    # Split a list with fewer elements than step size
    input_data = {'S': [10, 20], 'step': 5}
    expected = [[10], [20], [], [], []]
    assert list_split(**input_data) == expected

def test_split_list_of_floats_step_1():
    # Split a list of floats into 1 sublist (step=1) returns the original list
    input_data = {'S': [0.1, 0.2, 0.3], 'step': 1}
    expected = [[0.1, 0.2, 0.3]]
    assert list_split(**input_data) == expected