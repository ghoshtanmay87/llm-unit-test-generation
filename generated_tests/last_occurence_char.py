def last_occurence_char(string,char):
 flag = -1
 for i in range(len(string)):
     if(string[i] == char):
         flag = i
 if(flag == -1):
    return None
 else:
    return flag + 1

import pytest

def test_character_appears_once_in_string():
    result = last_occurence_char("hello", "e")
    assert result == 2

def test_character_appears_multiple_times_in_string():
    result = last_occurence_char("banana", "a")
    assert result == 5

def test_character_does_not_appear_in_string():
    result = last_occurence_char("world", "a")
    assert result is None

def test_empty_string_input():
    result = last_occurence_char("", "a")
    assert result is None

def test_character_is_last_character_in_string():
    result = last_occurence_char("testcase", "e")
    assert result == 8

def test_character_is_first_character_in_string():
    result = last_occurence_char("apple", "a")
    assert result == 1