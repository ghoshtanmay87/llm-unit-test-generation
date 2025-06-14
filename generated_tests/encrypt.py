def encrypt(s):
    d = 'abcdefghijklmnopqrstuvwxyz'
    out = ''
    for c in s:
        if c in d:
            out += d[(d.index(c) + 2 * 2) % 26]
        else:
            out += c
    return out

import pytest

def test_encrypt_lowercase_letters_only():
    # Encrypt a lowercase string with letters only
    input_str = 'abc'
    expected = 'efg'
    assert encrypt(input_str) == expected

def test_encrypt_mixed_lowercase_and_spaces():
    # Encrypt a string with mixed lowercase letters and spaces
    input_str = 'hello world'
    expected = 'lipps asvph'
    assert encrypt(input_str) == expected

def test_encrypt_letters_and_punctuation():
    # Encrypt a string with letters and punctuation
    input_str = 'abc! xyz.'
    expected = 'efg! bcd.'
    assert encrypt(input_str) == expected

def test_encrypt_empty_string():
    # Encrypt an empty string
    input_str = ''
    expected = ''
    assert encrypt(input_str) == expected

def test_encrypt_no_lowercase_letters():
    # Encrypt a string with no lowercase letters
    input_str = '1234!@#'
    expected = '1234!@#'
    assert encrypt(input_str) == expected

def test_encrypt_all_alphabet_letters():
    # Encrypt a string with all letters of the alphabet
    input_str = 'abcdefghijklmnopqrstuvwxyz'
    expected = 'efghijklmnopqrstuvwxyzabcd'
    assert encrypt(input_str) == expected