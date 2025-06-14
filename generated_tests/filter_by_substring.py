from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [x for x in strings if substring in x]

import pytest

def test_filter_list_with_substring_present_in_some_elements():
    strings = ['apple', 'banana', 'apricot', 'cherry']
    substring = 'ap'
    expected_output = ['apple', 'apricot']
    assert filter_by_substring(strings, substring) == expected_output

def test_filter_list_with_substring_not_present_in_any_element():
    strings = ['dog', 'cat', 'mouse']
    substring = 'z'
    expected_output = []
    assert filter_by_substring(strings, substring) == expected_output

def test_filter_list_with_empty_substring_should_return_all_elements():
    strings = ['one', 'two', 'three']
    substring = ''
    expected_output = ['one', 'two', 'three']
    assert filter_by_substring(strings, substring) == expected_output

def test_filter_empty_list_with_any_substring():
    strings = []
    substring = 'any'
    expected_output = []
    assert filter_by_substring(strings, substring) == expected_output

def test_filter_list_with_substring_present_in_all_elements():
    strings = ['test', 'testing', 'contest']
    substring = 'test'
    expected_output = ['test', 'testing', 'contest']
    assert filter_by_substring(strings, substring) == expected_output

def test_filter_list_with_substring_present_in_some_elements_with_overlapping_substrings():
    strings = ['hello', 'world', 'hold', 'cold']
    substring = 'ol'
    expected_output = ['hold', 'cold']
    assert filter_by_substring(strings, substring) == expected_output