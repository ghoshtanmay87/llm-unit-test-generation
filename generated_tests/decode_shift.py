def encode_shift(s: str):
    return ''.join([chr((ord(ch) + 5 - ord('a')) % 26 + ord('a')) for ch in s])

def decode_shift(s: str):
    return ''.join([chr((ord(ch) - 5 - ord('a')) % 26 + ord('a')) for ch in s])

import pytest

def test_decode_shift_simple_lowercase_fghij():
    # Decoding a simple lowercase string 'fghij' shifted by 5
    input_str = 'fghij'
    expected = 'abcde'
    assert decode_shift(input_str) == expected

def test_decode_shift_wrap_around_abcde():
    # Decoding the string 'abcde' which was originally 'vwxyz' shifted by 5
    input_str = 'abcde'
    expected = 'vwxyz'
    assert decode_shift(input_str) == expected

def test_decode_shift_wrap_around_zabcd():
    # Decoding the string 'zabcd' which was originally 'uvwxy' shifted by 5
    input_str = 'zabcd'
    expected = 'uvwxy'
    assert decode_shift(input_str) == expected

def test_decode_shift_empty_string():
    # Decoding an empty string returns an empty string
    input_str = ''
    expected = ''
    assert decode_shift(input_str) == expected

def test_decode_shift_klmno_to_fghij():
    # Decoding the string 'klmno' which was originally 'fghij' shifted by 5
    input_str = 'klmno'
    expected = 'fghij'
    assert decode_shift(input_str) == expected