def is_Two_Alter(s):  
    for i in range (len( s) - 2) : 
        if (s[i] != s[i + 2]) : 
            return False
    if (s[0] == s[1]): 
        return False
    return True

import pytest

def test_string_with_alternating_characters_ababab():
    s = 'ababab'
    expected = True
    assert is_Two_Alter(s) == expected

def test_string_with_non_alternating_characters_aa():
    s = 'aa'
    expected = False
    assert is_Two_Alter(s) == expected

def test_string_with_non_alternating_characters_abcabc():
    s = 'abcabc'
    expected = False
    assert is_Two_Alter(s) == expected

def test_string_with_alternating_characters_xyxyxyx():
    s = 'xyxyxyx'
    expected = True
    assert is_Two_Alter(s) == expected

def test_string_with_all_identical_characters_aaaaaa():
    s = 'aaaaaa'
    expected = False
    assert is_Two_Alter(s) == expected

def test_string_with_length_less_than_2_a():
    s = 'a'
    expected = True
    assert is_Two_Alter(s) == expected

def test_string_with_length_exactly_2_and_different_characters_ab():
    s = 'ab'
    expected = True
    assert is_Two_Alter(s) == expected