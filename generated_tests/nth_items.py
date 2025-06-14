def nth_items(list,n):
 return list[::n]

import pytest

def test_selecting_every_2nd_item_from_list_of_integers():
    input_list = [1, 2, 3, 4, 5, 6]
    n = 2
    expected_output = [1, 3, 5]
    assert nth_items(input_list, n) == expected_output

def test_selecting_every_3rd_item_from_list_of_strings():
    input_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
    n = 3
    expected_output = ['a', 'd', 'g']
    assert nth_items(input_list, n) == expected_output

def test_selecting_every_1st_item_all_items_from_list():
    input_list = [10, 20, 30]
    n = 1
    expected_output = [10, 20, 30]
    assert nth_items(input_list, n) == expected_output

def test_selecting_every_4th_item_from_short_list():
    input_list = [5, 10, 15]
    n = 4
    expected_output = [5]
    assert nth_items(input_list, n) == expected_output

def test_selecting_every_2nd_item_from_empty_list():
    input_list = []
    n = 2
    expected_output = []
    assert nth_items(input_list, n) == expected_output