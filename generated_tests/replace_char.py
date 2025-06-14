def replace_char(str1,ch,newch):
 str2 = str1.replace(ch, newch)
 return str2

import pytest

def test_replace_all_occurrences_of_character():
    # Replace all occurrences of a character in a simple string
    result = replace_char('hello world', 'o', 'a')
    assert result == 'hella warld'

def test_replace_character_not_in_string():
    # Replace a character that does not exist in the string
    result = replace_char('hello world', 'x', 'y')
    assert result == 'hello world'

def test_replace_character_with_empty_string():
    # Replace a character with an empty string (removal)
    result = replace_char('banana', 'a', '')
    assert result == 'bnn'

def test_replace_character_with_multi_character_string():
    # Replace a character with a multi-character string
    result = replace_char('abcabc', 'b', 'xy')
    assert result == 'axycaxyc'

def test_replace_space_with_underscore():
    # Replace a space character with underscore
    result = replace_char('a b c d', ' ', '_')
    assert result == 'a_b_c_d'

def test_replace_character_in_empty_string():
    # Replace a character in an empty string
    result = replace_char('', 'a', 'b')
    assert result == ''

def test_replace_character_with_itself():
    # Replace a character with itself (no change)
    result = replace_char('test', 't', 't')
    assert result == 'test'