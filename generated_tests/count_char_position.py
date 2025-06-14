def count_char_position(str1): 
    count_chars = 0
    for i in range(len(str1)):
        if ((i == ord(str1[i]) - ord('A')) or 
            (i == ord(str1[i]) - ord('a'))): 
            count_chars += 1
    return count_chars

import pytest

def test_all_characters_match_uppercase_positions():
    # All characters match their zero-based index positions (uppercase)
    result = count_char_position('ABCDEF')
    assert result == 6

def test_all_characters_match_lowercase_positions():
    # All characters match their zero-based index positions (lowercase)
    result = count_char_position('abcdef')
    assert result == 6

def test_mixed_case_some_characters_match_positions():
    # Mixed case with some characters matching their positions
    result = count_char_position('aBcDeF')
    assert result == 6

def test_characters_do_not_match_positions():
    # Characters do not match their positions
    result = count_char_position('XYZ')
    assert result == 0

def test_empty_string_input():
    # Empty string input
    result = count_char_position('')
    assert result == 0

def test_string_with_non_alphabetic_characters():
    # String with non-alphabetic characters
    result = count_char_position('A1b2C3')
    assert result == 2

def test_long_string_with_partial_matches():
    # Long string with partial matches
    result = count_char_position('aAbBcCdDeEfFgG')
    assert result == 14