def are_Rotations(string1,string2): 
    size1 = len(string1) 
    size2 = len(string2) 
    temp = '' 
    if size1 != size2: 
        return False
    temp = string1 + string1 
    if (temp.count(string2)> 0): 
        return True
    else: 
        return False

import pytest

def test_both_strings_empty():
    # Both strings have length 0, so sizes are equal.
    # Concatenating string1 with itself results in an empty string.
    # The count of string2 (empty string) in temp is greater than 0, so the function returns True.
    assert are_Rotations('', '') is True

def test_strings_of_different_lengths():
    # Lengths differ (3 vs 2), so the function immediately returns False without further checks.
    assert are_Rotations('abc', 'ab') is False

def test_string2_is_rotation_of_string1():
    # Lengths are equal (4).
    # temp = 'abcdabcd'.
    # 'cdab' is a substring of 'abcdabcd', so count > 0 and function returns True.
    assert are_Rotations('abcd', 'cdab') is True

def test_string2_is_not_rotation_of_string1():
    # Lengths are equal (4).
    # temp = 'abcdabcd'.
    # 'acbd' is not a substring of 'abcdabcd', so count = 0 and function returns False.
    assert are_Rotations('abcd', 'acbd') is False

def test_identical_strings():
    # Lengths are equal.
    # temp = 'rotationrotation'.
    # Since string2 equals string1, it is obviously a substring of temp, so function returns True.
    assert are_Rotations('rotation', 'rotation') is True

def test_single_character_strings_same_character():
    # Lengths are equal (1).
    # temp = 'aa'.
    # 'a' is a substring of 'aa', so function returns True.
    assert are_Rotations('a', 'a') is True

def test_single_character_strings_different_characters():
    # Lengths are equal (1).
    # temp = 'aa'.
    # 'b' is not a substring of 'aa', so function returns False.
    assert are_Rotations('a', 'b') is False

def test_string2_is_rotation_by_one_character():
    # Lengths are equal (11).
    # temp = 'waterbottlewaterbottle'.
    # 'erbottlewat' is a substring of temp, so function returns True.
    assert are_Rotations('waterbottle', 'erbottlewat') is True

def test_string2_has_same_characters_but_not_rotation():
    # Lengths are equal (5).
    # temp = 'abcdeabcde'.
    # 'abced' is not a substring of temp, so function returns False.
    assert are_Rotations('abcde', 'abced') is False