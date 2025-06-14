def remove_Char(s,c) :  
    counts = s.count(c) 
    s = list(s) 
    while counts :  
        s.remove(c) 
        counts -= 1 
    s = '' . join(s)   
    return (s)

import pytest

def test_remove_all_occurrences_of_character_present_multiple_times():
    # The character 'a' appears 3 times in 'banana'. Removing all 'a' results in 'bnn'.
    result = remove_Char('banana', 'a')
    assert result == 'bnn'

def test_remove_character_that_appears_twice():
    # The character 'p' appears twice in 'apple'. Removing both 'p's results in 'ale'.
    result = remove_Char('apple', 'p')
    assert result == 'ale'

def test_remove_character_not_present_in_string():
    # The character 'x' does not appear in 'hello', so the original string is returned.
    result = remove_Char('hello', 'x')
    assert result == 'hello'

def test_remove_character_from_empty_string():
    # Empty string has no characters, so nothing is removed and empty string is returned.
    result = remove_Char('', 'a')
    assert result == ''

def test_remove_character_appearing_once_at_start():
    # The character 'c' appears once at the start of 'cat', removing it results in 'at'.
    result = remove_Char('cat', 'c')
    assert result == 'at'

def test_remove_character_appearing_once_at_end():
    # The character 'g' appears once at the end of 'dog', removing it results in 'do'.
    result = remove_Char('dog', 'g')
    assert result == 'do'

def test_remove_character_appearing_multiple_times_consecutively():
    # The character 's' appears 4 times in 'mississippi'. Removing all 's' results in 'miiippi'.
    result = remove_Char('mississippi', 's')
    assert result == 'miiippi'

def test_remove_space_character_from_string():
    # Spaces appear 3 times in 'a b c d' and are all removed, resulting in 'abcd'.
    result = remove_Char('a b c d', ' ')
    assert result == 'abcd'