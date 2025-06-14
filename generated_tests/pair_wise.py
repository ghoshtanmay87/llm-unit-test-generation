def pair_wise(l1):
    temp = []
    for i in range(len(l1) - 1):
        current_element, next_element = l1[i], l1[i + 1]
        x = (current_element, next_element)
        temp.append(x)
    return temp

import pytest

def test_pair_wise_multiple_integers():
    l1 = [1, 2, 3, 4]
    expected = [(1, 2), (2, 3), (3, 4)]
    assert pair_wise(l1) == expected

def test_pair_wise_two_elements():
    l1 = [10, 20]
    expected = [(10, 20)]
    assert pair_wise(l1) == expected

def test_pair_wise_one_element():
    l1 = [5]
    expected = []
    assert pair_wise(l1) == expected

def test_pair_wise_empty_list():
    l1 = []
    expected = []
    assert pair_wise(l1) == expected

def test_pair_wise_mixed_data_types():
    l1 = ['a', 'b', 'c']
    expected = [('a', 'b'), ('b', 'c')]
    assert pair_wise(l1) == expected

def test_pair_wise_repeated_elements():
    l1 = [7, 7, 7]
    expected = [(7, 7), (7, 7)]
    assert pair_wise(l1) == expected