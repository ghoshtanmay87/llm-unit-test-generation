def remove_Occ(s,ch): 
    for i in range(len(s)): 
        if (s[i] == ch): 
            s = s[0 : i] + s[i + 1:] 
            break
    for i in range(len(s) - 1,-1,-1):  
        if (s[i] == ch): 
            s = s[0 : i] + s[i + 1:] 
            break
    return s

import pytest

def test_remove_first_and_last_occurrence_multiple_times():
    # Remove first and last occurrence of a character appearing multiple times in the string
    s = 'abracadabra'
    ch = 'a'
    expected = 'bracadabr'
    assert remove_Occ(s, ch) == expected

def test_remove_first_and_last_occurrence_single_occurrence():
    # Remove first and last occurrence of a character appearing once in the string
    s = 'hello'
    ch = 'e'
    expected = 'hllo'
    assert remove_Occ(s, ch) == expected

def test_remove_first_and_last_occurrence_character_not_present():
    # Remove first and last occurrence of a character not present in the string
    s = 'test'
    ch = 'z'
    expected = 'test'
    assert remove_Occ(s, ch) == expected

def test_remove_first_and_last_occurrence_consecutive_characters():
    # Remove first and last occurrence when character appears twice consecutively
    s = 'bookkeeper'
    ch = 'k'
    expected = 'bookeeper'
    assert remove_Occ(s, ch) == expected

def test_remove_first_and_last_occurrence_single_at_end():
    # Remove first and last occurrence when character appears only once at the end
    s = 'python'
    ch = 'n'
    expected = 'pytho'
    assert remove_Occ(s, ch) == expected

def test_remove_first_and_last_occurrence_single_at_start():
    # Remove first and last occurrence when character appears only once at the start
    s = 'apple'
    ch = 'a'
    expected = 'pple'
    assert remove_Occ(s, ch) == expected

def test_remove_first_and_last_occurrence_multiple_non_consecutive():
    # Remove first and last occurrence when character appears multiple times non-consecutively
    s = 'mississippi'
    ch = 's'
    expected = 'misisippi'
    assert remove_Occ(s, ch) == expected