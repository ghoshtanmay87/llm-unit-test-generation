def solve(s):
    flg = 0
    idx = 0
    new_str = list(s)
    for i in s:
        if i.isalpha():
            new_str[idx] = i.swapcase()
            flg = 1
        idx += 1
    s = ''
    for i in new_str:
        s += i
    if flg == 0:
        return s[len(s)::-1]
    return s

import pytest

def test_mixed_alphabetic_and_non_alphabetic_characters():
    # Input string with mixed alphabetic and non-alphabetic characters
    input_str = 'AbC123'
    expected = 'aBc123'
    assert solve(input_str) == expected

def test_only_digits_no_alphabetic_characters():
    # Input string with only digits (no alphabetic characters)
    input_str = '12345'
    expected = '54321'
    assert solve(input_str) == expected

def test_only_uppercase_letters():
    # Input string with only uppercase letters
    input_str = 'HELLO'
    expected = 'hello'
    assert solve(input_str) == expected

def test_only_lowercase_letters():
    # Input string with only lowercase letters
    input_str = 'world'
    expected = 'WORLD'
    assert solve(input_str) == expected

def test_no_alphabetic_characters_with_symbols():
    # Input string with no alphabetic characters but with symbols
    input_str = '!@#$%'
    expected = '%$#@!'
    assert solve(input_str) == expected

def test_empty_string_input():
    # Empty string input
    input_str = ''
    expected = ''
    assert solve(input_str) == expected

def test_alphabetic_and_whitespace_characters():
    # Input string with alphabetic and whitespace characters
    input_str = 'Hello World'
    expected = 'hELLO wORLD'
    assert solve(input_str) == expected

def test_alphabetic_characters_and_digits_mixed():
    # Input string with alphabetic characters and digits mixed
    input_str = 'a1B2c3'
    expected = 'A1b2C3'
    assert solve(input_str) == expected