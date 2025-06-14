def count(s,c) : 
    res = 0 
    for i in range(len(s)) : 
        if (s[i] == c): 
            res = res + 1
    return res

import pytest

def test_count_multiple_occurrences():
    # Count occurrences of a character present multiple times in the string
    result = count(s='hello world', c='l')
    assert result == 3

def test_count_single_occurrence():
    # Count occurrences of a character present once in the string
    result = count(s='hello world', c='h')
    assert result == 1

def test_count_character_not_present():
    # Count occurrences of a character not present in the string
    result = count(s='hello world', c='z')
    assert result == 0

def test_count_space_character():
    # Count occurrences of a space character in the string
    result = count(s='hello world', c=' ')
    assert result == 1

def test_count_in_empty_string():
    # Count occurrences of a character in an empty string
    result = count(s='', c='a')
    assert result == 0

def test_count_digit_character():
    # Count occurrences of a digit character in a string with digits
    result = count(s='123123123', c='1')
    assert result == 3

def test_count_uppercase_character():
    # Count occurrences of uppercase character in a mixed case string
    result = count(s='AbcABCabc', c='A')
    assert result == 2

def test_count_lowercase_character():
    # Count occurrences of lowercase character in a mixed case string
    result = count(s='AbcABCabc', c='a')
    assert result == 1