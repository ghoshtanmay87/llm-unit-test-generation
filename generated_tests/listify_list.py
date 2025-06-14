def listify_list(list1):
  result = list(map(list,list1)) 
  return result

import pytest

def test_listify_list_with_list_of_tuples():
    # Input is a list of tuples
    input_data = [(1, 2), (3, 4)]
    expected = [[1, 2], [3, 4]]
    assert listify_list(input_data) == expected

def test_listify_list_with_list_of_lists():
    # Input is a list of lists
    input_data = [[5, 6], [7, 8]]
    expected = [[5, 6], [7, 8]]
    assert listify_list(input_data) == expected

def test_listify_list_with_list_of_strings():
    # Input is a list of strings
    input_data = ['ab', 'cd']
    expected = [['a', 'b'], ['c', 'd']]
    assert listify_list(input_data) == expected

def test_listify_list_with_list_of_empty_tuples():
    # Input is a list of empty tuples
    input_data = [(), ()]
    expected = [[], []]
    assert listify_list(input_data) == expected

def test_listify_list_with_empty_list():
    # Input is an empty list
    input_data = []
    expected = []
    assert listify_list(input_data) == expected