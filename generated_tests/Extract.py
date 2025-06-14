def Extract(lst): 
    return [item[0] for item in lst]

import pytest

def test_extract_first_elements_from_list_of_tuples():
    lst = [(1, 2), (3, 4), (5, 6)]
    expected = [1, 3, 5]
    assert Extract(lst) == expected

def test_extract_first_elements_from_list_of_lists():
    lst = [[10, 20], [30, 40], [50, 60]]
    expected = [10, 30, 50]
    assert Extract(lst) == expected

def test_extract_first_elements_from_list_of_single_element_lists():
    lst = [[7], [8], [9]]
    expected = [7, 8, 9]
    assert Extract(lst) == expected

def test_extract_first_elements_from_list_of_strings():
    lst = ['abc', 'def', 'ghi']
    expected = ['a', 'd', 'g']
    assert Extract(lst) == expected

def test_extract_first_elements_from_empty_list():
    lst = []
    expected = []
    assert Extract(lst) == expected