from typing import List, Any

def filter_integers(values: List[Any]) -> List[int]:
    return [x for x in values if isinstance(x, int)]

import pytest

def test_filter_only_integers():
    # Filter a list containing only integers
    values = [1, 2, 3, 4, 5]
    expected_output = [1, 2, 3, 4, 5]
    assert filter_integers(values) == expected_output

def test_filter_integers_and_strings():
    # Filter a list containing integers and strings
    values = [1, '2', 3, 'four', 5]
    expected_output = [1, 3, 5]
    assert filter_integers(values) == expected_output

def test_filter_integers_floats_booleans():
    # Filter a list containing integers, floats, and booleans
    values = [0, 1.0, True, 2, False, 3.5]
    expected_output = [0, True, 2, False]
    assert filter_integers(values) == expected_output

def test_filter_no_integers():
    # Filter a list containing no integers
    values = ['a', 2.5, None, [], {}]
    expected_output = []
    assert filter_integers(values) == expected_output

def test_filter_empty_list():
    # Filter an empty list
    values = []
    expected_output = []
    assert filter_integers(values) == expected_output

def test_filter_nested_lists_and_integers():
    # Filter a list with nested lists and integers
    values = [1, [2], 3, [4, 5], 6]
    expected_output = [1, 3, 6]
    assert filter_integers(values) == expected_output