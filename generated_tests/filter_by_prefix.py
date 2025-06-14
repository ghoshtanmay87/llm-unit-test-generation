from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [x for x in strings if x.startswith(prefix)]

import pytest

def test_filter_multiple_strings_some_start_with_prefix():
    strings = ['apple', 'banana', 'apricot', 'cherry']
    prefix = 'ap'
    expected = ['apple', 'apricot']
    assert filter_by_prefix(strings, prefix) == expected

def test_filter_no_strings_start_with_prefix():
    strings = ['dog', 'cat', 'mouse']
    prefix = 'z'
    expected = []
    assert filter_by_prefix(strings, prefix) == expected

def test_filter_all_strings_start_with_prefix():
    strings = ['test', 'testing', 'tester']
    prefix = 'test'
    expected = ['test', 'testing', 'tester']
    assert filter_by_prefix(strings, prefix) == expected

def test_filter_empty_list_with_any_prefix():
    strings = []
    prefix = 'any'
    expected = []
    assert filter_by_prefix(strings, prefix) == expected

def test_filter_list_with_empty_prefix_returns_all_strings():
    strings = ['one', 'two', 'three']
    prefix = ''
    expected = ['one', 'two', 'three']
    assert filter_by_prefix(strings, prefix) == expected

def test_filter_prefix_longer_than_any_string():
    strings = ['a', 'ab', 'abc']
    prefix = 'abcd'
    expected = []
    assert filter_by_prefix(strings, prefix) == expected

def test_filter_prefix_matching_multiple_strings():
    strings = ['hello', 'world', 'help', 'held']
    prefix = 'hel'
    expected = ['hello', 'help', 'held']
    assert filter_by_prefix(strings, prefix) == expected