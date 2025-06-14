def is_valid_parenthese( str1):
        stack, pchar = [], {"(": ")", "{": "}", "[": "]"}
        for parenthese in str1:
            if parenthese in pchar:
                stack.append(parenthese)
            elif len(stack) == 0 or pchar[stack.pop()] != parenthese:
                return False
        return len(stack) == 0

import pytest

def test_empty_string_should_be_valid():
    # Empty string should be valid as there are no parentheses to match
    input_str = ''
    expected = True
    assert is_valid_parenthese(input_str) == expected

def test_string_with_only_opening_parentheses_is_invalid():
    # String with only opening parentheses is invalid
    input_str = '((('
    expected = False
    assert is_valid_parenthese(input_str) == expected

def test_string_with_only_closing_parentheses_is_invalid():
    # String with only closing parentheses is invalid
    input_str = ')))'
    expected = False
    assert is_valid_parenthese(input_str) == expected

def test_properly_nested_and_matched_parentheses():
    # Properly nested and matched parentheses
    input_str = '({[]})'
    expected = True
    assert is_valid_parenthese(input_str) == expected

def test_mismatched_parentheses_should_return_false():
    # Mismatched parentheses should return False
    input_str = '({[)]}'
    expected = False
    assert is_valid_parenthese(input_str) == expected

def test_single_pair_of_parentheses_is_valid():
    # Single pair of parentheses is valid
    input_str = '()'
    expected = True
    assert is_valid_parenthese(input_str) == expected

def test_interleaved_but_invalid_parentheses():
    # Interleaved but invalid parentheses
    input_str = '([)]'
    expected = False
    assert is_valid_parenthese(input_str) == expected

def test_long_valid_sequence_of_mixed_parentheses():
    # Long valid sequence of mixed parentheses
    input_str = '([]{})'
    expected = True
    assert is_valid_parenthese(input_str) == expected

def test_string_with_characters_other_than_parentheses_should_be_invalid():
    # String with characters other than parentheses should be invalid (not handled explicitly)
    input_str = '(a)'
    expected = False
    assert is_valid_parenthese(input_str) == expected