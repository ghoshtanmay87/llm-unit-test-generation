def concatenate_elements(list):
  ans = ' '
  for i in list:
    ans = ans+ ' '+i
  return (ans)

import pytest

def test_concatenate_multiple_strings():
    # Concatenate a list of multiple strings
    input_list = ['hello', 'world']
    expected = '  hello world'
    assert concatenate_elements(input_list) == expected

def test_concatenate_single_string():
    # Concatenate a list with a single string
    input_list = ['test']
    expected = '  test'
    assert concatenate_elements(input_list) == expected

def test_concatenate_empty_list():
    # Concatenate an empty list
    input_list = []
    expected = ' '
    assert concatenate_elements(input_list) == expected

def test_concatenate_three_strings():
    # Concatenate a list of three strings
    input_list = ['a', 'b', 'c']
    expected = '  a b c'
    assert concatenate_elements(input_list) == expected

def test_concatenate_empty_strings():
    # Concatenate a list with empty strings
    input_list = ['', '']
    expected = '   '
    assert concatenate_elements(input_list) == expected