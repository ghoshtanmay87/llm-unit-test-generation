def count_vowels(test_str):
  res = 0
  vow_list = ['a', 'e', 'i', 'o', 'u']
  for idx in range(1, len(test_str) - 1):
    if test_str[idx] not in vow_list and (test_str[idx - 1] in vow_list or test_str[idx + 1] in vow_list):
      res += 1
  if test_str[0] not in vow_list and test_str[1] in vow_list:
    res += 1
  if test_str[-1] not in vow_list and test_str[-2] in vow_list:
    res += 1
  return (res)

import pytest

def test_count_consonants_surrounded_by_vowels_in_middle():
    # The string 'aba' has length 3. The middle character 'b' (index 1) is not a vowel and is surrounded by vowels 'a' at index 0 and 2, so res increments by 1. The first and last characters are vowels, so no increments there.
    assert count_vowels("aba") == 1

def test_count_consonants_at_start_and_end_adjacent_to_vowels():
    # Length is 3. Middle character 'a' is a vowel, so no increment in loop. First character 'c' is not a vowel and next character 'a' is a vowel, so res += 1. Last character 'b' is not a vowel and previous character 'a' is a vowel, so res += 1. Total 2.
    assert count_vowels("cab") == 2

def test_string_with_no_consonants_adjacent_to_vowels():
    # All characters are vowels, so no consonants to count.
    assert count_vowels("aaa") == 0

def test_string_with_consonants_not_adjacent_to_vowels():
    # All characters are consonants but none are adjacent to vowels, so no increments.
    assert count_vowels("bbb") == 0

def test_longer_string_with_multiple_consonants_adjacent_to_vowels():
    # Check indices 1 to 4:
    # - idx=1: 'e' vowel, skip
    # - idx=2: 'i' vowel, skip
    # - idx=3: 'b' consonant, neighbors 'i' and 'o' vowels, res +=1
    # - idx=4: 'o' vowel, skip
    # First char 'a' vowel, no increment.
    # Last char 'u' vowel, no increment.
    # Total 1.
    assert count_vowels("aeibou") == 1

def test_string_with_consonants_at_edges_adjacent_to_vowels():
    # Length 2, loop does not run (range(10) empty).
    # First char 'u' vowel, no increment.
    # Last char 'b' consonant, previous char 'u' vowel, so res +=1.
    # Total 1.
    assert count_vowels("ub") == 1

def test_string_with_single_character_vowel():
    # Length 1, loop does not run.
    # First and last char same vowel, no increments.
    # Total 0.
    assert count_vowels("a") == 0

def test_string_with_single_character_consonant():
    # Length 1, loop does not run.
    # First and last char same consonant, but no neighbors, so no increments.
    # Total 0.
    assert count_vowels("b") == 0

def test_string_with_consonants_surrounded_by_vowels_and_isolated_consonants():
    # Length 9, loop idx 1 to 7:
    # idx=1:'b' consonant, neighbors 'a' and 'e' vowels, res=1
    # idx=2:'e' vowel, skip
    # idx=3:'c' consonant, neighbors 'e' and 'i' vowels, res=2
    # idx=4:'i' vowel, skip
    # idx=5:'d' consonant, neighbors 'i' and 'o' vowels, res=3
    # idx=6:'o' vowel, skip
    # idx=7:'f' consonant, neighbors 'o' and 'u' vowels, res=4
    # Check edges:
    # idx0:'a' vowel, no increment
    # idx8:'u' vowel, no increment
    # Total 4.
    assert count_vowels("abecidofu") == 4

def test_string_with_consonants_at_edges_and_middle_with_vowels():
    # Length 4, loop idx 1 to 2:
    # idx=1:'b' consonant, neighbors 'u' and 'e' vowels, res=1
    # idx=2:'e' vowel, skip
    # Edges:
    # idx0:'u' vowel, no increment
    # idx3:'c' consonant, previous 'e' vowel, res=2
    # Total 2.
    assert count_vowels("ubec") == 2