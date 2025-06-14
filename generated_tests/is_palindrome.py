def is_palindrome(text: str):
    for i in range(len(text)):
        if text[i] != text[len(text) - 1 - i]:
            return False
    return True

import pytest

def test_empty_string_is_palindrome():
    # An empty string has no characters to compare and is trivially a palindrome.
    assert is_palindrome(text='') is True

def test_single_character_is_palindrome():
    # A single character string reads the same forwards and backwards, so it is a palindrome.
    assert is_palindrome(text='a') is True

def test_even_length_palindrome():
    # Characters at symmetric positions match: 'a' == 'a' and 'b' == 'b', so it is a palindrome.
    assert is_palindrome(text='abba') is True

def test_odd_length_palindrome():
    # Characters at symmetric positions match: 'r' == 'r', 'a' == 'a', 'c' == 'c', and the middle 'e' is the same, so it is a palindrome.
    assert is_palindrome(text='racecar') is True

def test_non_palindrome_string():
    # Characters at symmetric positions differ: 'h' != 'o', so the function returns False.
    assert is_palindrome(text='hello') is False

def test_mixed_case_case_sensitive():
    # The function is case sensitive, so 'A' != 'a', resulting in False.
    assert is_palindrome(text='Aa') is False

def test_spaces_and_punctuation_not_palindrome():
    # Spaces and characters at symmetric positions do not match exactly, so the function returns False.
    assert is_palindrome(text='a man a plan a canal panama') is False

def test_numeric_characters_palindrome():
    # Numeric characters at symmetric positions match: '1' == '1', '2' == '2', and the middle '3' is the same, so it is a palindrome.
    assert is_palindrome(text='12321') is True