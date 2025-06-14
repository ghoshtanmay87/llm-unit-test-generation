def encode(message):
    vowels = 'aeiouAEIOU'
    vowels_replace = dict([(i, chr(ord(i) + 2)) for i in vowels])
    message = message.swapcase()
    return ''.join([vowels_replace[i] if i in vowels else i for i in message])

import pytest

def test_encode_no_vowels():
    # Encoding a string with no vowels
    input_message = 'bcdfg'
    expected = 'BCDFG'
    assert encode(input_message) == expected

def test_encode_empty_string():
    # Encoding an empty string
    input_message = ''
    expected = ''
    assert encode(input_message) == expected

def test_encode_mixed_case_vowels_and_consonants():
    # Encoding a mixed case string with vowels and consonants
    input_message = 'Hello World'
    expected = 'hGLLQ wQRLD'
    assert encode(input_message) == expected

def test_encode_only_lowercase_vowels():
    # Encoding a string with only lowercase vowels
    input_message = 'aeiou'
    expected = 'CGKQW'
    assert encode(input_message) == expected

def test_encode_only_uppercase_vowels():
    # Encoding a string with only uppercase vowels
    input_message = 'AEIOU'
    expected = 'cgkqw'
    assert encode(input_message) == expected