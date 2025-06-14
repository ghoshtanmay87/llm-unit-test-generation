FIX = '\nAdd more test cases.\n'

def vowels_count(s):
    vowels = 'aeiouAEIOU'
    n_vowels = sum((c in vowels for c in s))
    if s[-1] == 'y' or s[-1] == 'Y':
        n_vowels += 1
    return n_vowels

import pytest

def test_count_vowels_simple_lowercase_no_trailing_y():
    # The string 'hello' contains two vowels: 'e' and 'o'.
    # The last character is 'o', not 'y' or 'Y', so no extra vowel is added.
    assert vowels_count('hello') == 2

def test_count_vowels_string_ending_with_lowercase_y():
    # The string 'happy' contains one vowel 'a'.
    # The last character is 'y', so one additional vowel is added, making the total 2.
    assert vowels_count('happy') == 2

def test_count_vowels_string_ending_with_uppercase_Y():
    # The string 'FUNNY' contains one vowel 'U'.
    # The last character is 'Y', so one additional vowel is added, making the total 2.
    assert vowels_count('FUNNY') == 2

def test_count_vowels_mixed_case_vowels_no_trailing_y():
    # All characters are vowels (both uppercase and lowercase), so the count is 5.
    # The last character is 'U', not 'y' or 'Y', so no extra vowel is added.
    assert vowels_count('AeIoU') == 5

def test_count_vowels_no_vowels_no_trailing_y():
    # The string 'rhythm' contains no vowels from 'aeiouAEIOU'.
    # The last character is 'm', not 'y' or 'Y', so no extra vowel is added.
    assert vowels_count('rhythm') == 0

def test_count_vowels_no_vowels_ending_with_y():
    # The string 'my' contains no vowels from 'aeiouAEIOU'.
    # The last character is 'y', so one additional vowel is added, making the total 1.
    assert vowels_count('my') == 1

def test_count_vowels_single_character_vowel():
    # The string 'a' is a vowel, so the count is 1.
    # The last character is 'a', not 'y' or 'Y', so no extra vowel is added.
    assert vowels_count('a') == 1

def test_count_vowels_single_character_y():
    # The string 'y' contains no vowels from 'aeiouAEIOU',
    # but the last character is 'y', so one additional vowel is added, making the total 1.
    assert vowels_count('y') == 1