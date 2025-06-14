def all_Characters_Same(s) :
    n = len(s)
    for i in range(1,n) :
        if s[i] != s[0] :
            return False
    return True

import pytest

def test_all_characters_same_all_same():
    # All characters in the string are the same
    s = 'aaaaaa'
    expected = True
    assert all_Characters_Same(s) == expected

def test_all_characters_same_different_middle():
    # String with different characters
    s = 'aaabaaa'
    expected = False
    assert all_Characters_Same(s) == expected

def test_all_characters_same_empty_string():
    # Empty string input
    s = ''
    expected = True
    assert all_Characters_Same(s) == expected

def test_all_characters_same_single_character():
    # Single character string
    s = 'z'
    expected = True
    assert all_Characters_Same(s) == expected

def test_all_characters_same_all_different():
    # String with all characters different
    s = 'abcdef'
    expected = False
    assert all_Characters_Same(s) == expected

def test_all_characters_same_all_same_except_last():
    # String with all characters same except last
    s = 'bbbbbbc'
    expected = False
    assert all_Characters_Same(s) == expected

def test_all_characters_same_all_same_except_first():
    # String with all characters same except first
    s = 'cbbbbbb'
    expected = False
    assert all_Characters_Same(s) == expected