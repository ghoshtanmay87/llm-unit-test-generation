def unique_Characters(str):
    for i in range(len(str)):
        for j in range(i + 1,len(str)): 
            if (str[i] == str[j]):
                return False;
    return True;

import pytest

def test_unique_characters_all_unique():
    # Check string with all unique characters
    input_str = 'abcdef'
    expected = True
    assert unique_Characters(input_str) == expected

def test_unique_characters_repeated_chars():
    # Check string with repeated characters
    input_str = 'hello'
    expected = False
    assert unique_Characters(input_str) == expected

def test_unique_characters_empty_string():
    # Check empty string
    input_str = ''
    expected = True
    assert unique_Characters(input_str) == expected

def test_unique_characters_single_char():
    # Check string with one character
    input_str = 'x'
    expected = True
    assert unique_Characters(input_str) == expected

def test_unique_characters_all_identical():
    # Check string with all identical characters
    input_str = 'aaaaaa'
    expected = False
    assert unique_Characters(input_str) == expected

def test_unique_characters_mixed_case_unique():
    # Check string with mixed case unique characters
    input_str = 'AbCdEf'
    expected = True
    assert unique_Characters(input_str) == expected

def test_unique_characters_mixed_case_repeated():
    # Check string with mixed case repeated characters
    input_str = 'AbCa'
    expected = False
    assert unique_Characters(input_str) == expected