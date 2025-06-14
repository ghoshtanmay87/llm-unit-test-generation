def first_non_repeating_character(str1):
  char_order = []
  ctr = {}
  for c in str1:
    if c in ctr:
      ctr[c] += 1
    else:
      ctr[c] = 1 
      char_order.append(c)
  for c in char_order:
    if ctr[c] == 1:
      return c
  return None

import pytest

def test_first_non_repeating_unique_characters():
    # All characters appear once, so the first character 'a' is the first non-repeating character.
    assert first_non_repeating_character('abcde') == 'a'

def test_first_non_repeating_first_char_repeats():
    # 'a' and 'b' both repeat, 'c' appears once and is the first non-repeating character.
    assert first_non_repeating_character('aabbc') == 'c'

def test_first_non_repeating_all_repeating_characters():
    # All characters appear more than once, so there is no non-repeating character.
    assert first_non_repeating_character('aabbcc') is None

def test_first_non_repeating_one_unique_in_middle():
    # 'a', 'b', 'd', and 'e' appear more than once except 'c' which appears once and is the first non-repeating character.
    assert first_non_repeating_character('aabbcdde') == 'c'

def test_first_non_repeating_single_character():
    # Only one character which appears once, so it is the first non-repeating character.
    assert first_non_repeating_character('z') == 'z'

def test_first_non_repeating_empty_string():
    # Empty string has no characters, so no non-repeating character exists.
    assert first_non_repeating_character('') is None

def test_first_non_repeating_multiple_unique_characters():
    # 's' repeats multiple times, 'w' appears once and is the first non-repeating character.
    assert first_non_repeating_character('swiss') == 'w'

def test_first_non_repeating_all_repeating_except_last():
    # All characters except 'f' appear twice, so 'f' is the first non-repeating character.
    assert first_non_repeating_character('aabbccddeef') == 'f'