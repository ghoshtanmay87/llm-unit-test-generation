def same_chars(s0: str, s1: str):
    return set(s0) == set(s1)

import pytest

def test_same_chars_identical_strings():
    # Both strings have exactly the same characters in the same quantity
    s0 = 'abc'
    s1 = 'abc'
    expected = True
    assert same_chars(s0, s1) == expected

def test_same_chars_same_characters_different_order():
    # Both strings have the same characters but in different order
    s0 = 'abc'
    s1 = 'cba'
    expected = True
    assert same_chars(s0, s1) == expected

def test_same_chars_different_characters():
    # Strings have different characters
    s0 = 'abc'
    s1 = 'abd'
    expected = False
    assert same_chars(s0, s1) == expected

def test_same_chars_one_empty_one_nonempty():
    # One string is empty, the other is not
    s0 = ''
    s1 = 'a'
    expected = False
    assert same_chars(s0, s1) == expected

def test_same_chars_both_empty():
    # Both strings are empty
    s0 = ''
    s1 = ''
    expected = True
    assert same_chars(s0, s1) == expected

def test_same_chars_same_characters_different_counts():
    # Strings have same characters but different counts
    s0 = 'aabbcc'
    s1 = 'abc'
    expected = True
    assert same_chars(s0, s1) == expected

def test_same_chars_overlapping_not_identical_sets():
    # Strings have overlapping but not identical character sets
    s0 = 'abc'
    s1 = 'ab'
    expected = False
    assert same_chars(s0, s1) == expected

def test_same_chars_special_characters_and_spaces():
    # Strings with special characters and spaces
    s0 = 'a b!'
    s1 = '!ba '
    expected = True
    assert same_chars(s0, s1) == expected

def test_same_chars_unicode_characters():
    # Strings with unicode characters
    s0 = 'ñáç'
    s1 = 'çáñ'
    expected = True
    assert same_chars(s0, s1) == expected

def test_same_chars_different_unicode_characters():
    # Strings with different unicode characters
    s0 = 'ñáç'
    s1 = 'ñáé'
    expected = False
    assert same_chars(s0, s1) == expected