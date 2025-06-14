def string_length(str1):
    count = 0
    for char in str1:
        count += 1
    return count

import pytest

def test_length_of_empty_string():
    assert string_length('') == 0

def test_length_of_single_character_string():
    assert string_length('a') == 1

def test_length_of_short_string():
    assert string_length('hello') == 5

def test_length_of_string_with_spaces():
    assert string_length('a b c') == 5

def test_length_of_string_with_special_characters():
    assert string_length('!@#$$%^&*()') == 10

def test_length_of_string_with_unicode_characters():
    assert string_length('你好') == 2