def count_distinct_characters(string: str) -> int:
    return len(set(string.lower()))

import pytest

def test_count_distinct_characters_lowercase_string():
    # Count distinct characters in a lowercase string
    input_string = 'hello'
    expected = 4
    assert count_distinct_characters(input_string) == expected

def test_count_distinct_characters_mixed_case_string():
    # Count distinct characters in a mixed case string
    input_string = 'HeLLo'
    expected = 4
    assert count_distinct_characters(input_string) == expected

def test_count_distinct_characters_empty_string():
    # Count distinct characters in an empty string
    input_string = ''
    expected = 0
    assert count_distinct_characters(input_string) == expected

def test_count_distinct_characters_all_identical_characters():
    # Count distinct characters in a string with all identical characters
    input_string = 'aaaaaa'
    expected = 1
    assert count_distinct_characters(input_string) == expected

def test_count_distinct_characters_spaces_and_punctuation():
    # Count distinct characters in a string with spaces and punctuation
    input_string = 'Hi! Hi!'
    expected = 4
    assert count_distinct_characters(input_string) == expected

def test_count_distinct_characters_digits_and_letters():
    # Count distinct characters in a string with digits and letters
    input_string = 'abc123ABC'
    expected = 6
    assert count_distinct_characters(input_string) == expected