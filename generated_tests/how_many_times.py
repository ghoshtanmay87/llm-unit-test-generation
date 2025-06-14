def how_many_times(string: str, substring: str) -> int:
    times = 0
    for i in range(len(string) - len(substring) + 1):
        if string[i:i + len(substring)] == substring:
            times += 1
    return times

import pytest

def test_count_multiple_non_overlapping_occurrences():
    # The substring 'ab' appears at indices 0, 2, and 4 in 'ababab', so it occurs 3 times.
    result = how_many_times(string='ababab', substring='ab')
    assert result == 3

def test_count_single_occurrence():
    # The substring 'world' appears exactly once starting at index 6 in 'hello world'.
    result = how_many_times(string='hello world', substring='world')
    assert result == 1

def test_count_no_occurrences():
    # The substring 'gh' does not appear anywhere in 'abcdef', so the count is 0.
    result = how_many_times(string='abcdef', substring='gh')
    assert result == 0

def test_count_overlapping_substrings():
    # The substring 'aa' appears at indices 0, 1, 2, and 3 in 'aaaaa', counting overlapping occurrences, so total is 4.
    result = how_many_times(string='aaaaa', substring='aa')
    assert result == 4

def test_count_substring_equals_string():
    # The substring 'test' is exactly the entire string, so it appears once.
    result = how_many_times(string='test', substring='test')
    assert result == 1

def test_count_empty_substring():
    # An empty substring is considered to appear at every position including the end, so for string length 3, it appears 4 times.
    result = how_many_times(string='abc', substring='')
    assert result == 4

def test_count_empty_string_nonempty_substring():
    # A non-empty substring cannot appear in an empty string, so the count is 0.
    result = how_many_times(string='', substring='a')
    assert result == 0

def test_count_empty_string_and_empty_substring():
    # An empty substring appears once in an empty string at position 0.
    result = how_many_times(string='', substring='')
    assert result == 1