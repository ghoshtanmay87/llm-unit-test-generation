def first_repeated_char(str1):
  for index,c in enumerate(str1):
    if str1[:index+1].count(c) > 1:
      return c 
  return "None"

import pytest

def test_string_with_immediate_repetition():
    # Scenario: String with immediate repetition of a character
    result = first_repeated_char('hello')
    assert result == 'l'

def test_string_with_no_repeated_characters():
    # Scenario: String with no repeated characters
    result = first_repeated_char('abc')
    assert result == 'None'

def test_string_with_repeated_character_at_start():
    # Scenario: String with repeated character at the start
    result = first_repeated_char('aabbcc')
    assert result == 'a'

def test_string_with_repeated_character_later():
    # Scenario: String with repeated character later in the string
    result = first_repeated_char('abca')
    assert result == 'a'

def test_empty_string_input():
    # Scenario: Empty string input
    result = first_repeated_char('')
    assert result == 'None'

def test_string_with_all_characters_same():
    # Scenario: String with all characters the same
    result = first_repeated_char('zzzz')
    assert result == 'z'

def test_string_with_repeated_character_separated_by_others():
    # Scenario: String with repeated character separated by others
    result = first_repeated_char('abcbad')
    assert result == 'b'