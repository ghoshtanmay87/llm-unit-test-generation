def sort_String(str) : 
    str = ''.join(sorted(str)) 
    return (str)

import pytest

def test_sort_string_mixed_characters():
    # Sorting a string with mixed characters
    input_str = 'dcba'
    expected = 'abcd'
    assert sort_String(input_str) == expected

def test_sort_string_repeated_characters():
    # Sorting a string with repeated characters
    input_str = 'banana'
    expected = 'aaabnn'
    assert sort_String(input_str) == expected

def test_sort_string_already_sorted():
    # Sorting an already sorted string
    input_str = 'abc'
    expected = 'abc'
    assert sort_String(input_str) == expected

def test_sort_string_uppercase_lowercase():
    # Sorting a string with uppercase and lowercase letters
    input_str = 'bAcD'
    expected = 'ADbc'
    assert sort_String(input_str) == expected

def test_sort_string_empty():
    # Sorting an empty string
    input_str = ''
    expected = ''
    assert sort_String(input_str) == expected