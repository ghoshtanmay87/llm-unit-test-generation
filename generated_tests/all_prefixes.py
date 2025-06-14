from typing import List

def all_prefixes(string: str) -> List[str]:
    result = []
    for i in range(len(string)):
        result.append(string[:i + 1])
    return result

import pytest

def test_empty_string_input_returns_empty_list():
    # The input string is empty, so the loop does not execute and the result list remains empty.
    input_string = ''
    expected = []
    assert all_prefixes(input_string) == expected

def test_single_character_string_returns_list_with_one_prefix():
    # The string length is 1, so the loop runs once, appending string[:1] which is 'a'.
    input_string = 'a'
    expected = ['a']
    assert all_prefixes(input_string) == expected

def test_two_character_string_returns_two_prefixes():
    # The loop runs twice: first appends string[:1] = 'a', then string[:2] = 'ab'.
    input_string = 'ab'
    expected = ['a', 'ab']
    assert all_prefixes(input_string) == expected

def test_string_with_repeated_characters_returns_all_prefixes():
    # The loop runs three times, each time appending the prefix up to index i+1, resulting in 'a', 'aa', and 'aaa'.
    input_string = 'aaa'
    expected = ['a', 'aa', 'aaa']
    assert all_prefixes(input_string) == expected

def test_longer_string_returns_all_incremental_prefixes():
    # The loop runs 5 times, appending prefixes of increasing length from 1 to 5 characters.
    input_string = 'hello'
    expected = ['h', 'he', 'hel', 'hell', 'hello']
    assert all_prefixes(input_string) == expected