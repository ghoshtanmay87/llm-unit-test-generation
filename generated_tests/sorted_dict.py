def sorted_dict(dict1):
  sorted_dict = {x: sorted(y) for x, y in dict1.items()}
  return sorted_dict

import pytest

def test_sort_lists_of_integers_for_each_key():
    input_dict = {'a': [3, 1, 2], 'b': [5, 4]}
    expected = {'a': [1, 2, 3], 'b': [4, 5]}
    assert sorted_dict(input_dict) == expected

def test_sort_lists_of_strings_for_each_key():
    input_dict = {'fruits': ['banana', 'apple', 'cherry'], 'colors': ['red', 'blue']}
    expected = {'fruits': ['apple', 'banana', 'cherry'], 'colors': ['blue', 'red']}
    assert sorted_dict(input_dict) == expected

def test_empty_dictionary_input_returns_empty_dictionary():
    input_dict = {}
    expected = {}
    assert sorted_dict(input_dict) == expected

def test_lists_with_one_element_remain_unchanged():
    input_dict = {'single': [42], 'letters': ['z']}
    expected = {'single': [42], 'letters': ['z']}
    assert sorted_dict(input_dict) == expected

def test_lists_with_duplicate_elements_sorted_with_duplicates_preserved():
    input_dict = {'nums': [2, 3, 2, 1, 1]}
    expected = {'nums': [1, 1, 2, 2, 3]}
    assert sorted_dict(input_dict) == expected