def swap_List(newList): 
    size = len(newList) 
    temp = newList[0] 
    newList[0] = newList[size - 1] 
    newList[size - 1] = temp   
    return newList

import pytest

def test_swap_first_and_last_integers():
    input_data = [1, 2, 3, 4, 5]
    expected = [5, 2, 3, 4, 1]
    assert swap_List(input_data) == expected

def test_swap_first_and_last_strings():
    input_data = ['a', 'b', 'c', 'd']
    expected = ['d', 'b', 'c', 'a']
    assert swap_List(input_data) == expected

def test_swap_first_and_last_two_elements():
    input_data = [10, 20]
    expected = [20, 10]
    assert swap_List(input_data) == expected

def test_swap_first_and_last_single_element():
    input_data = [42]
    expected = [42]
    assert swap_List(input_data) == expected

def test_swap_first_and_last_mixed_types():
    input_data = [True, 'middle', 3.14, None]
    expected = [None, 'middle', 3.14, True]
    assert swap_List(input_data) == expected