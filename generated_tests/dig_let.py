def dig_let(s):
 d=l=0
 for c in s:
    if c.isdigit():
        d=d+1
    elif c.isalpha():
        l=l+1
    else:
        pass
 return (l,d)

import pytest

def test_input_string_with_only_digits():
    s = '1234567890'
    expected = (0, 10)
    assert dig_let(s) == expected

def test_input_string_with_only_letters():
    s = 'abcdefXYZ'
    expected = (9, 0)
    assert dig_let(s) == expected

def test_input_string_with_letters_and_digits():
    s = 'a1b2c3'
    expected = (3, 3)
    assert dig_let(s) == expected

def test_input_string_with_letters_digits_and_special_characters():
    s = 'a1!b2@c3#'
    expected = (3, 3)
    assert dig_let(s) == expected

def test_empty_input_string():
    s = ''
    expected = (0, 0)
    assert dig_let(s) == expected

def test_input_string_with_spaces_and_punctuation_only():
    s = ' !@#$%^&*() '
    expected = (0, 0)
    assert dig_let(s) == expected

def test_input_string_with_mixed_case_letters_and_digits():
    s = 'AbC123xYz'
    expected = (6, 3)
    assert dig_let(s) == expected

def test_input_string_with_unicode_letters_and_digits():
    s = 'a1ß2ç3'
    expected = (4, 3)
    assert dig_let(s) == expected