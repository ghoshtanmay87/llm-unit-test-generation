import sys 
def tuple_size(tuple_list):
  return (sys.getsizeof(tuple_list))

import pytest

def test_size_of_empty_tuple_list():
    # Calculate size of an empty tuple list
    input_data = []
    expected = 56
    assert tuple_size(input_data) == expected

def test_size_of_list_with_one_empty_tuple():
    # Calculate size of a list with one empty tuple
    input_data = [()]
    expected = 64
    assert tuple_size(input_data) == expected

def test_size_of_list_with_two_empty_tuples():
    # Calculate size of a list with two empty tuples
    input_data = [(), ()]
    expected = 72
    assert tuple_size(input_data) == expected

def test_size_of_list_with_one_tuple_containing_one_integer():
    # Calculate size of a list with one tuple containing one integer
    input_data = [(1,)]
    expected = 64
    assert tuple_size(input_data) == expected

def test_size_of_list_with_three_empty_tuples():
    # Calculate size of a list with three empty tuples
    input_data = [(), (), ()]
    expected = 80
    assert tuple_size(input_data) == expected