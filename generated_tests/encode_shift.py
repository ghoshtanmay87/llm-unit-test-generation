def encode_shift(s: str):
    return ''.join([chr((ord(ch) + 5 - ord('a')) % 26 + ord('a')) for ch in s])

def decode_shift(s: str):
    return ''.join([chr((ord(ch) - 5 - ord('a')) % 26 + ord('a')) for ch in s])

import pytest

def test_encode_shift_simple_lowercase_string_abc():
    # Encoding a simple lowercase string 'abc'
    input_str = 'abc'
    expected = 'fgh'
    assert encode_shift(input_str) == expected

def test_encode_shift_wrap_around_xyz():
    # Encoding a string with wrap-around from 'z' to 'e'
    input_str = 'xyz'
    expected = 'cde'
    assert encode_shift(input_str) == expected

def test_encode_shift_single_character_m():
    # Encoding a single character 'm'
    input_str = 'm'
    expected = 'r'
    assert encode_shift(input_str) == expected

def test_encode_shift_empty_string():
    # Encoding an empty string
    input_str = ''
    expected = ''
    assert encode_shift(input_str) == expected

def test_encode_shift_full_alphabet():
    # Encoding a full alphabet string
    input_str = 'abcdefghijklmnopqrstuvwxyz'
    expected = 'fghijklmnopqrstuvwxyzabcde'
    assert encode_shift(input_str) == expected