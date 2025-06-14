from typing import List, Optional

def longest(strings: List[str]) -> Optional[str]:
    if not strings:
        return None
    maxlen = max((len(x) for x in strings))
    for s in strings:
        if len(s) == maxlen:
            return s

import pytest

def test_empty_list_input_returns_none():
    # The input list is empty, so the function returns None immediately as per the first condition.
    assert longest([]) is None

def test_single_string_input_returns_that_string():
    # Only one string is present, so it is the longest by default and returned.
    assert longest(['hello']) == 'hello'

def test_multiple_strings_with_unique_longest_string():
    # The longest string length is 3 ('abc'), so the function returns 'abc' which is the first string with that length.
    assert longest(['a', 'ab', 'abc', 'ab']) == 'abc'

def test_multiple_strings_with_multiple_longest_strings_returns_first_longest():
    # Both 'abc' and 'def' have length 3, the longest length. The function returns the first occurrence, 'abc'.
    assert longest(['abc', 'def', 'gh']) == 'abc'

def test_all_strings_same_length_returns_first_string():
    # All strings have length 3, so the function returns the first string 'one'.
    assert longest(['one', 'two', 'six']) == 'one'

def test_strings_with_varying_lengths_and_special_characters():
    # The longest string length is 3 ('   ', 'abc'), so the function returns the first string with that length, which is '   '.
    assert longest(['', ' ', '  ', '   ', 'a', 'ab', 'abc']) == '   '