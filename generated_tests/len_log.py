def len_log(list1):
    min=len(list1[0])
    for i in list1:
        if len(i)<min:
            min=len(i)
    return min

import pytest

def test_len_log_list_of_strings_with_varying_lengths():
    input_data = ['apple', 'banana', 'pear', 'kiwi']
    expected = 4
    assert len_log(input_data) == expected

def test_len_log_list_of_empty_and_non_empty_strings():
    input_data = ['', 'a', 'ab', 'abc']
    expected = 0
    assert len_log(input_data) == expected

def test_len_log_list_of_lists_with_different_lengths():
    input_data = [[1, 2, 3], [4, 5], [6], [7, 8, 9, 10]]
    expected = 1
    assert len_log(input_data) == expected

def test_len_log_list_with_one_element():
    input_data = ['single']
    expected = 6
    assert len_log(input_data) == expected

def test_len_log_list_of_tuples_with_varying_lengths():
    input_data = [(1, 2), (3, 4, 5), (6,)]
    expected = 1
    assert len_log(input_data) == expected