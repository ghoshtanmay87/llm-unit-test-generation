def add_str(test_tup, K):
  res = [ele for sub in test_tup for ele in (sub, K)]
  return (res)

import pytest

def test_add_integer_K_after_each_element_in_tuple_of_integers():
    test_tup = (1, 2, 3)
    K = 5
    expected_output = [1, 5, 2, 5, 3, 5]
    assert add_str(test_tup, K) == expected_output

def test_add_string_K_after_each_element_in_tuple_of_strings():
    test_tup = ('a', 'b')
    K = 'x'
    expected_output = ['a', 'x', 'b', 'x']
    assert add_str(test_tup, K) == expected_output

def test_add_float_K_after_each_element_in_tuple_of_mixed_types():
    test_tup = (10, 'hello')
    K = 3.14
    expected_output = [10, 3.14, 'hello', 3.14]
    assert add_str(test_tup, K) == expected_output

def test_add_None_K_after_each_element_in_tuple_of_integers():
    test_tup = (7, 8)
    K = None
    expected_output = [7, None, 8, None]
    assert add_str(test_tup, K) == expected_output

def test_add_empty_string_K_after_each_element_in_tuple_of_single_character_strings():
    test_tup = ('x', 'y', 'z')
    K = ''
    expected_output = ['x', '', 'y', '', 'z', '']
    assert add_str(test_tup, K) == expected_output