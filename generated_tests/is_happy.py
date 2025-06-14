def is_happy(s):
    if len(s) < 3:
        return False
    for i in range(len(s) - 2):
        if s[i] == s[i + 1] or s[i + 1] == s[i + 2] or s[i] == s[i + 2]:
            return False
    return True

import pytest

def test_input_string_shorter_than_3_characters():
    s = 'ab'
    expected = False
    assert is_happy(s) == expected

def test_string_with_no_three_character_substrings_having_any_two_equal_characters():
    s = 'abcde'
    expected = True
    assert is_happy(s) == expected

def test_string_with_three_consecutive_characters_where_first_two_are_equal():
    s = 'aabbc'
    expected = False
    assert is_happy(s) == expected

def test_string_with_three_consecutive_characters_where_last_two_are_equal():
    s = 'abbcd'
    expected = False
    assert is_happy(s) == expected

def test_string_with_three_consecutive_characters_where_first_and_last_are_equal():
    s = 'aba'
    expected = False
    assert is_happy(s) == expected

def test_string_with_multiple_substrings_one_substring_violates_the_condition():
    s = 'abcdefgg'
    expected = False
    assert is_happy(s) == expected

def test_string_with_multiple_substrings_all_satisfy_the_condition():
    s = 'abcdefg'
    expected = True
    assert is_happy(s) == expected

def test_string_with_exactly_3_characters_all_distinct():
    s = 'xyz'
    expected = True
    assert is_happy(s) == expected

def test_string_with_exactly_3_characters_with_two_equal_characters():
    s = 'xxy'
    expected = False
    assert is_happy(s) == expected