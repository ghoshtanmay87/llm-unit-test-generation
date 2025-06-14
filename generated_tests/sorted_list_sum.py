def sorted_list_sum(lst):
    lst.sort()
    new_lst = []
    for i in lst:
        if len(i) % 2 == 0:
            new_lst.append(i)
    return sorted(new_lst, key=len)

import pytest

def test_all_odd_length_sublists():
    # List with all odd length sublists
    input_lst = [[1], [2, 3, 4], [5, 6, 7]]
    expected = []
    assert sorted_list_sum(input_lst) == expected

def test_all_even_length_sublists():
    # List with all even length sublists
    input_lst = [[2, 1], [4, 3, 6, 5], [8, 7]]
    expected = [[2, 1], [8, 7], [4, 3, 6, 5]]
    assert sorted_list_sum(input_lst) == expected

def test_empty_list_input():
    # Empty list input
    input_lst = []
    expected = []
    assert sorted_list_sum(input_lst) == expected

def test_list_with_empty_sublists():
    # List with empty sublists
    input_lst = [[], [], [1], [2, 3]]
    expected = [[], [], [2, 3]]
    assert sorted_list_sum(input_lst) == expected

def test_mixed_even_and_odd_length_sublists():
    # List with mixed even and odd length sublists
    input_lst = [[3, 1, 2], [4, 5], [6, 7, 8, 9], [10]]
    expected = [[4, 5], [6, 7, 8, 9]]
    assert sorted_list_sum(input_lst) == expected