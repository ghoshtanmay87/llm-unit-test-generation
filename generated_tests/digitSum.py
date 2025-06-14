def digitSum(s):
    if s == '':
        return 0
    return sum((ord(char) if char.isupper() else 0 for char in s))

import pytest

def test_empty_string_input_returns_0():
    assert digitSum('') == 0

def test_string_with_all_lowercase_letters_returns_0():
    assert digitSum('abcxyz') == 0

def test_string_with_all_uppercase_letters_returns_sum_of_their_ascii_codes():
    assert digitSum('ABC') == 198

def test_string_with_mixed_uppercase_and_lowercase_letters_sums_only_uppercase_ascii_codes():
    assert digitSum('aAbBcC') == 198

def test_string_with_digits_and_uppercase_letters_sums_only_uppercase_ascii_codes():
    assert digitSum('123ABC456') == 198

def test_string_with_special_characters_and_uppercase_letters_sums_only_uppercase_ascii_codes():
    assert digitSum('!@#XyZ$%^') == 178

def test_string_with_uppercase_letters_and_non_alphabetic_characters_sums_only_uppercase_ascii_codes():
    assert digitSum('Hello, World!') == 159