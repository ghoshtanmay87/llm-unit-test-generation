def count_upper(s):
    count = 0
    for i in range(0, len(s), 2):
        if s[i] in 'AEIOU':
            count += 1
    return count

import pytest

def test_count_upper_mixed_characters():
    # Count uppercase vowels at even indices in a string with mixed characters
    s = 'AbEcIdOfU'
    expected = 5
    assert count_upper(s) == expected

def test_count_upper_no_uppercase_vowels():
    # Count uppercase vowels at even indices in a string with no uppercase vowels
    s = 'bcdfghjklmnpqrstvwxyz'
    expected = 0
    assert count_upper(s) == expected

def test_count_upper_empty_string():
    # Count uppercase vowels at even indices in an empty string
    s = ''
    expected = 0
    assert count_upper(s) == expected

def test_count_upper_only_uppercase_vowels():
    # Count uppercase vowels at even indices in a string with only uppercase vowels
    s = 'AEIOUAEIOU'
    expected = 5
    assert count_upper(s) == expected

def test_count_upper_uppercase_consonants_and_vowels():
    # Count uppercase vowels at even indices in a string with uppercase consonants and vowels
    s = 'BACEGIKOMU'
    expected = 0
    assert count_upper(s) == expected