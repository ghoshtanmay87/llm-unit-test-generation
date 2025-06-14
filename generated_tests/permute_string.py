def permute_string(str):
    if len(str) == 0:
        return ['']
    prev_list = permute_string(str[1:len(str)])
    next_list = []
    for i in range(0,len(prev_list)):
        for j in range(0,len(str)):
            new_str = prev_list[i][0:j]+str[0]+prev_list[i][j:len(str)-1]
            if new_str not in next_list:
                next_list.append(new_str)
    return next_list

import pytest

def test_permute_empty_string_returns_list_with_empty_string():
    # Permuting an empty string returns a list with an empty string
    input_str = ''
    expected = ['']
    assert permute_string(input_str) == expected

def test_permute_single_character_string_returns_list_with_that_character():
    # Permuting a single character string returns a list with that character
    input_str = 'a'
    expected = ['a']
    assert permute_string(input_str) == expected

def test_permute_two_character_string_returns_both_permutations():
    # Permuting a two-character string returns both permutations
    input_str = 'ab'
    expected = ['ab', 'ba']
    assert permute_string(input_str) == expected

def test_permute_three_character_string_with_unique_characters():
    # Permuting a three-character string with unique characters
    input_str = 'abc'
    expected = ['abc', 'bac', 'bca', 'acb', 'cab', 'cba']
    assert permute_string(input_str) == expected

def test_permute_string_with_duplicate_characters():
    # Permuting a string with duplicate characters
    input_str = 'aab'
    expected = ['aab', 'aab', 'aba', 'aab', 'aab', 'baa']
    assert permute_string(input_str) == expected