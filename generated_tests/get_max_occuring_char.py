def get_max_occuring_char(str1):
  ASCII_SIZE = 256
  ctr = [0] * ASCII_SIZE
  max = -1
  ch = ''
  for i in str1:
    ctr[ord(i)]+=1;
  for i in str1:
    if max < ctr[ord(i)]:
      max = ctr[ord(i)]
      ch = i
  return ch

import pytest

def test_max_occuring_char_distinct_characters():
    # All characters occur once, so the first character 'a' is returned as it has the max count encountered first.
    assert get_max_occuring_char('abcde') == 'a'

def test_max_occuring_char_one_character_repeated():
    # 'd' occurs 3 times, which is more than 'a' and 'b' (2 times each), so 'd' is returned.
    assert get_max_occuring_char('aabbccddd') == 'd'

def test_max_occuring_char_multiple_max_frequency():
    # All 'a', 'b', and 'c' occur twice, but 'a' appears first in the string, so it is returned.
    assert get_max_occuring_char('aabbcc') == 'a'

def test_max_occuring_char_single_character():
    # Only one character 'z' is present, so it is returned.
    assert get_max_occuring_char('z') == 'z'

def test_max_occuring_char_empty_string():
    # Empty string has no characters, so the function returns the initialized empty string.
    assert get_max_occuring_char('') == ''

def test_max_occuring_char_special_characters():
    # '!' occurs 4 times, '@' occurs 2 times, so '!' is returned.
    assert get_max_occuring_char('!@!@!!') == '!'

def test_max_occuring_char_mixed_case_characters():
    # 'a' occurs 4 times (3 lowercase 'a' + 1 lowercase 'a' at start), uppercase letters are distinct characters, so 'a' is max.
    assert get_max_occuring_char('aAbBcCaaa') == 'a'