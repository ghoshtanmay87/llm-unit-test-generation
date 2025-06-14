def remove_odd(str1):
 str2 = ''
 for i in range(1, len(str1) + 1):
    if(i % 2 == 0):
        str2 = str2 + str1[i - 1]
 return str2

import pytest

def test_remove_odd_simple_string():
    # Remove characters at odd positions from a simple string
    input_str = 'abcdef'
    expected = 'bdf'
    assert remove_odd(input_str) == expected

def test_remove_odd_string_with_spaces():
    # Remove characters at odd positions from a string with spaces
    input_str = 'hello world'
    expected = 'el ol'
    assert remove_odd(input_str) == expected

def test_remove_odd_single_character_string():
    # Remove characters at odd positions from a single character string
    input_str = 'x'
    expected = ''
    assert remove_odd(input_str) == expected

def test_remove_odd_empty_string():
    # Remove characters at odd positions from an empty string
    input_str = ''
    expected = ''
    assert remove_odd(input_str) == expected

def test_remove_odd_numeric_string():
    # Remove characters at odd positions from a numeric string
    input_str = '1234567890'
    expected = '24680'
    assert remove_odd(input_str) == expected

def test_remove_odd_string_with_special_characters():
    # Remove characters at odd positions from a string with special characters
    input_str = '!@#$%^&*()'
    expected = '@$^&()'
    assert remove_odd(input_str) == expected