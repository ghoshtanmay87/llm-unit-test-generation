def count_charac(str1):
 total = 0
 for i in str1:
    total = total + 1
 return total

import pytest

def test_count_charac_empty_string():
    # Count characters in an empty string
    result = count_charac('')
    assert result == 0

def test_count_charac_single_character():
    # Count characters in a string with one character
    result = count_charac('a')
    assert result == 1

def test_count_charac_multiple_characters():
    # Count characters in a string with multiple characters
    result = count_charac('hello')
    assert result == 5

def test_count_charac_spaces_and_punctuation():
    # Count characters in a string with spaces and punctuation
    result = count_charac('Hi, there!')
    assert result == 9

def test_count_charac_unicode_characters():
    # Count characters in a string with unicode characters
    result = count_charac('café')
    assert result == 4