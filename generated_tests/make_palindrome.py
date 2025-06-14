def is_palindrome(string: str) -> bool:
    return string == string[::-1]

def make_palindrome(string: str) -> str:
    if not string:
        return ''
    beginning_of_suffix = 0
    while not is_palindrome(string[beginning_of_suffix:]):
        beginning_of_suffix += 1
    return string + string[:beginning_of_suffix][::-1]

import pytest

def test_empty_string_input_returns_empty_string():
    input_string = ''
    expected = ''
    assert make_palindrome(input_string) == expected

def test_input_string_already_palindrome_returns_same_string():
    input_string = 'racecar'
    expected = 'racecar'
    assert make_palindrome(input_string) == expected

def test_input_abc_returns_abcba_by_appending_reversed_prefix():
    input_string = 'abc'
    expected = 'abcba'
    assert make_palindrome(input_string) == expected

def test_input_aabb_returns_aabbaa_by_appending_reversed_prefix():
    input_string = 'aabb'
    expected = 'aabbaa'
    assert make_palindrome(input_string) == expected

def test_input_abcd_returns_abcdcba_by_appending_reversed_prefix():
    input_string = 'abcd'
    expected = 'abcdcba'
    assert make_palindrome(input_string) == expected

def test_input_a_returns_a_since_it_is_already_palindrome():
    input_string = 'a'
    expected = 'a'
    assert make_palindrome(input_string) == expected

def test_input_aa_returns_aa_since_it_is_already_palindrome():
    input_string = 'aa'
    expected = 'aa'
    assert make_palindrome(input_string) == expected

def test_input_abcba_returns_abcba_since_it_is_already_palindrome():
    input_string = 'abcba'
    expected = 'abcba'
    assert make_palindrome(input_string) == expected

def test_input_ab_returns_aba_by_appending_reversed_prefix():
    input_string = 'ab'
    expected = 'aba'
    assert make_palindrome(input_string) == expected

def test_input_abca_returns_abcacba_by_appending_reversed_prefix():
    input_string = 'abca'
    expected = 'abcacba'
    assert make_palindrome(input_string) == expected